#!/usr/bin/env python3
"""bm25-desc and bm25-body runs for ds/skillret."""
import json, os, re
from rank_bm25 import BM25Okapi

OUT = "/workspace/work/bench/ds/skillret"
queries = [json.loads(l) for l in open(os.path.join(OUT, "queries.jsonl"))]
skills = [json.loads(l) for l in open(os.path.join(OUT, "skills.jsonl"))]
ids = [s["id"] for s in skills]

TOK = re.compile(r"[a-z0-9]+")

def toks(t):
    return TOK.findall(t.lower())

desc_bytes = sum(len((s["name"] + "\n" + s["description"]).encode("utf-8")) for s in skills)
body_bytes = sum(len((s["name"] + "\n" + s["description"] + "\n" + s["body"]).encode("utf-8")) for s in skills)

def run(name, texts, read_bytes):
    bm25 = BM25Okapi([toks(t) for t in texts])
    with open(os.path.join(OUT, "runs", name + ".jsonl"), "w") as f:
        for qi, q in enumerate(queries):
            scores = bm25.get_scores(toks(q["query"]))
            top = scores.argsort()[::-1][:20]
            f.write(json.dumps({"qid": q["qid"], "ranked": [ids[i] for i in top],
                                "read_bytes": read_bytes}) + "\n")
            if qi % 500 == 0:
                print(name, qi, flush=True)
    print(name, "done", flush=True)

run("bm25-desc", [s["name"] + " " + s["description"] for s in skills], desc_bytes)
run("bm25-body", [s["name"] + " " + s["description"] + " " + s["body"] for s in skills], body_bytes)
