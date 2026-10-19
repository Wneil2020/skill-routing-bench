#!/usr/bin/env python3
"""Run all deterministic methods for ds/toolret and write runs/<method>.jsonl."""
import json
import sys
from pathlib import Path

BENCH = Path("/workspace/work/bench")
BASE = BENCH / "ds" / "toolret"
sys.path.insert(0, str(BENCH / "holon" / "organizer" / "scripts"))
import organizer_cli as oc  # noqa: E402

queries = [json.loads(l) for l in (BASE / "queries.jsonl").open()]
skills = [json.loads(l) for l in (BASE / "skills.jsonl").open()]
slug_map = json.load((BASE / "slug_map.json").open())
id_by_slug = {v["slug"]: k for k, v in slug_map.items()}

(BASE / "runs").mkdir(exist_ok=True)


def run_tree(rootdir, out_name):
    root = rootdir.resolve()
    skmap, errors = oc.find_skills(root)
    assert not errors, errors
    syn = oc.load_synonyms(root)
    children = {d: oc.children_of(d, skmap) for d in skmap}
    sizes = {d: (d / "SKILL.md").stat().st_size for d in skmap}
    stats = {"leaf": 0, "group": 0, "root": 0, "ambig": 0}
    with (BASE / "runs" / out_name).open("w") as f:
        for q in queries:
            path = oc.route(q["query"], root, skmap, syn)
            last = path[-1]
            dirs = [p for p in path if not isinstance(p, tuple)]
            read_bytes = sum(sizes[d] for d in dirs)
            if isinstance(last, tuple):
                stats["ambig"] += 1
                ranked = []
            elif children.get(last):
                stats["group" if last != root else "root"] += 1
                ranked = []
            elif last == root:
                stats["root"] += 1
                ranked = []
            else:
                stats["leaf"] += 1
                ranked = [id_by_slug[last.name]]
            f.write(json.dumps({"qid": q["qid"], "ranked": ranked, "read_bytes": read_bytes}) + "\n")
    return stats


st_tree = run_tree(BASE / "tree", "holon-tree.jsonl")
st_flat = run_tree(BASE / "flat", "flat-literal.jsonl")
print("holon-tree stats:", st_tree)
print("flat-literal stats:", st_flat)

# ---- BM25 ----
from rank_bm25 import BM25Okapi  # noqa: E402

def toks(text):
    return [t for t in __import__("re").findall(r"[a-z0-9]+", text.lower())]

desc_texts = [s["name"] + " " + s["description"] for s in skills]
body_texts = [s["name"] + " " + s["description"] + " " + s["body"] for s in skills]
desc_bytes = sum(len(t.encode()) for t in desc_texts)
body_bytes = sum(len(t.encode()) for t in body_texts)

def run_bm25(texts, rb, out_name):
    bm = BM25Okapi([toks(t) for t in texts])
    with (BASE / "runs" / out_name).open("w") as f:
        for q in queries:
            scores = bm.get_scores(toks(q["query"]))
            order = sorted(range(len(scores)), key=lambda i: (-scores[i], skills[i]["id"]))[:20]
            f.write(json.dumps({"qid": q["qid"], "ranked": [skills[i]["id"] for i in order],
                                "read_bytes": rb}) + "\n")

run_bm25(desc_texts, desc_bytes, "bm25-desc.jsonl")
run_bm25(body_texts, body_bytes, "bm25-body.jsonl")
print("bm25 done, desc_bytes:", desc_bytes, "body_bytes:", body_bytes)

# ---- dense ----
emb_dir = BASE / "emb"
emb_dir.mkdir(exist_ok=True)
import numpy as np  # noqa: E402
from fastembed import TextEmbedding  # noqa: E402

model = TextEmbedding("BAAI/bge-small-en-v1.5")
if (emb_dir / "docs.npy").exists():
    D = np.load(emb_dir / "docs.npy")
    Q = np.load(emb_dir / "queries.npy")
else:
    D = np.array(list(model.embed(desc_texts, batch_size=16)))
    Q = np.array(list(model.embed([q["query"] for q in queries], batch_size=16)))
    np.save(emb_dir / "docs.npy", D)
    np.save(emb_dir / "queries.npy", Q)
Dn = D / np.linalg.norm(D, axis=1, keepdims=True)
Qn = Q / np.linalg.norm(Q, axis=1, keepdims=True)
sims = Qn @ Dn.T
dense_ranked = []
with (BASE / "runs" / "dense.jsonl").open("w") as f:
    for qi, q in enumerate(queries):
        order = sorted(range(D.shape[0]), key=lambda i: (-sims[qi, i], skills[i]["id"]))[:20]
        r = [skills[i]["id"] for i in order]
        dense_ranked.append(r)
        f.write(json.dumps({"qid": q["qid"], "ranked": r, "read_bytes": desc_bytes}) + "\n")
print("dense done")

# ---- hybrid: RRF(k=60) of bm25-desc and dense ----
bm25_ranked = [json.loads(l)["ranked"] for l in (BASE / "runs" / "bm25-desc.jsonl").open()]
K = 60
with (BASE / "runs" / "hybrid.jsonl").open("w") as f:
    for qi, q in enumerate(queries):
        score = {}
        for r, sid in enumerate(bm25_ranked[qi]):
            score[sid] = score.get(sid, 0) + 1 / (K + r + 1)
        for r, sid in enumerate(dense_ranked[qi]):
            score[sid] = score.get(sid, 0) + 1 / (K + r + 1)
        ranked = [sid for sid, _ in sorted(score.items(), key=lambda kv: (-kv[1], kv[0]))[:20]]
        f.write(json.dumps({"qid": q["qid"], "ranked": ranked,
                            "read_bytes": desc_bytes * 2}) + "\n")
print("hybrid done")
