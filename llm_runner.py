import re
"""For deepseek via Cline: CHAT_URL=https://api.cline.bot/api/v1/chat/completions MODEL=cline-pass/deepseek-v4.1-flash OUT_SUFFIX=-deepseek
LLM routing methods over ds/<ds>/ built by the adapters (see SPEC.md).
usage: python3 llm_runner.py <ds> <method: llm-tree|llm-rerank> [threads]
Reads ds/<ds>/sample.jsonl, skills.jsonl, tree/, runs/bm25-desc.jsonl. Writes runs/<method>.jsonl (resumable).
"""
import sys, os, json, re, threading, concurrent.futures as cf
sys.path.insert(0, "/workspace/work/review/v2")
os.environ.setdefault("STREAM", "1"); os.environ.setdefault("RPM5", "600")
os.environ.setdefault("BASE", "https://hub.oaifree.com"); os.environ.setdefault("MODEL", "k3-256k")
import orch
ds, method = sys.argv[1], sys.argv[2]; T = int(sys.argv[3]) if len(sys.argv) > 3 else 16
D = f"/workspace/work/bench/ds/{ds}"
skills = {s["id"]: s for s in map(json.loads, open(f"{D}/skills.jsonl"))}
sample = [json.loads(l) for l in open(f"{D}/sample.jsonl")]
out_p = f"{D}/runs/{method}{os.environ.get('OUT_SUFFIX','')}.jsonl"; done = set()
if os.path.exists(out_p):
    done = {json.loads(l)["qid"] for l in open(out_p)}
lock = threading.Lock()
MO, MC = "<!-- sub-skills -->", "<!-- /sub-skills -->"

import subprocess, time
def ask(prompt, maxtok=4000):
    body = json.dumps({"model": os.environ["MODEL"], "messages": [{"role": "user", "content": orch.clean(prompt)}], "max_tokens": maxtok, "stream": True})
    last = ""
    for i in range(6):
        r = subprocess.run(["curl", "-sN", "--max-time", "600", os.environ.get("CHAT_URL", os.environ["BASE"] + "/v1/chat/completions"), "-H", "Content-Type: application/json", "-d", "@-"], input=body, capture_output=True, text=True)
        last = r.stdout
        out = []
        for ln in r.stdout.splitlines():
            if ln.startswith("data:") and "[DONE]" not in ln:
                try:
                    out.append(json.loads(ln[5:])["choices"][0]["delta"].get("content") or "")
                except Exception:
                    pass
        c = re.sub(r"(?s)<think>.*?</think>", "", "".join(out)).strip()
        if c.strip():
            return c
        print("retry", i, r.returncode, r.stdout[:160].replace("\n", " "), file=sys.stderr, flush=True)
        time.sleep(int(os.environ.get("BACKOFF","5")) * (i + 1))
    raise RuntimeError(last[:200])

# map leaf dir -> skill id: each leaf SKILL.md name == dir name; find id by scanning tree once
leaf2id = {}
idx_p = f"{D}/tree_index.json"
if os.path.exists(idx_p):
    leaf2id = json.load(open(idx_p))

def table(path):
    t = open(os.path.join(path, "SKILL.md"), encoding="utf-8").read()
    i, j = t.find(MO), t.find(MC)
    return t, (t[i + len(MO):j].strip() if i >= 0 and j > i else "")

def children(path):
    return sorted(d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d, "SKILL.md")) and not d.startswith("."))

def llm_tree(q):
    cur = f"{D}/tree"; read = 0; trail = []
    for depth in range(5):
        full, tab = table(cur); read += len(full.encode())
        kids = children(cur)
        if not kids:
            break
        p = ("You route a user request through a skill library organised as a tree. Below is the routing table of the current node: one line per sub-skill, with its folder name and description.\n"
             "Pick the ONE sub-skill folder whose description fits the request; reply with exactly that folder name. If none fits, reply STOP.\n"
             f"Request: {q['query']}\n\nRouting table:\n{tab}\n\nFolder names: {', '.join(kids)}\nAnswer with one folder name or STOP, nothing else.")
        a = ask(p).strip().strip("`'\" .").split()[0] if True else ""
        if a not in kids:
            m = [k for k in kids if k.lower() == a.lower()]
            if not m:
                break
            a = m[0]
        cur = os.path.join(cur, a); trail.append(a)
    rel = "/".join(trail)
    sid = leaf2id.get(rel)
    if sid is None and trail:
        sid = trail[-1] if trail[-1] in skills else None
    is_leaf = not children(cur)
    return {"qid": q["qid"], "ranked": [sid] if (sid and is_leaf) else [], "read_bytes": read, "path": rel}

bm = {}
if method == "llm-rerank":
    bm = {r["qid"]: r for r in map(json.loads, open(f"{D}/runs/bm25-desc.jsonl"))}

def llm_rerank(q, k=30):
    cands = [c for c in bm[q["qid"]]["ranked"][:k] if c in skills]
    lines = "\n".join(f"{c} :: {skills[c]['name']} -- {skills[c]['description'][:300]}" for c in cands)
    p = ("Select skills for a user request. Candidates are listed as `id :: name -- description`.\n"
         "Return the ids of the best-fitting skills, best first, at most 5, as a JSON list of strings. If the request needs several skills in sequence, list each needed one.\n"
         f"Request: {q['query']}\n\nCandidates:\n{lines}\n\nAnswer with the JSON list only.")
    a = ask(p)
    m = re.search(r"\[.*?\]", a, re.S)
    try:
        ids = [x for x in json.loads(m.group(0)) if x in skills] if m else []
    except Exception:
        ids = []
    return {"qid": q["qid"], "ranked": ids, "read_bytes": len(lines.encode())}

FLAT = None
def llm_flat(q):
    global FLAT
    if FLAT is None:
        FLAT = "\n".join(f"{i} :: {s['name']} -- {s['description'][:300]}" for i, s in skills.items())
    p = ("Select skills for a user request from the whole library below, listed as `id :: name -- description`.\n"
         "Return the ids of the best-fitting skills, best first, at most 5, as a JSON list of strings. If the request needs several skills in sequence, list each needed one.\n"
         f"Request: {q['query']}\n\nLibrary:\n{FLAT}\n\nAnswer with the JSON list only.")
    a = ask(p)
    m = re.search(r"\[.*?\]", a, re.S)
    try:
        ids = [x for x in json.loads(m.group(0)) if x in skills] if m else []
    except Exception:
        ids = []
    return {"qid": q["qid"], "ranked": ids, "read_bytes": len(FLAT.encode())}

fn = {"llm-tree": llm_tree, "llm-rerank": llm_rerank, "llm-flat": llm_flat}[method]

def run(q):
    if q["qid"] in done:
        return
    try:
        r = fn(q)
    except Exception as e:
        print("ERR", q["qid"], str(e)[:120], flush=True); return
    with lock:
        with open(out_p, "a") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

with cf.ThreadPoolExecutor(T) as ex:
    list(ex.map(run, sample))
print("done", ds, method, sum(1 for _ in open(out_p)))
