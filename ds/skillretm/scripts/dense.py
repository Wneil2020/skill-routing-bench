#!/usr/bin/env python3
"""Encode skill (name+description) and query texts with fastembed bge-small-en-v1.5.
Caches to ds/skillret/emb/. Then writes runs/dense.jsonl."""
import json, os, sys
import numpy as np

OUT = "/workspace/work/bench/ds/skillret"
EMB = os.path.join(OUT, "emb")

skills = [json.loads(l) for l in open(os.path.join(OUT, "skills.jsonl"))]
queries = [json.loads(l) for l in open(os.path.join(OUT, "queries.jsonl"))]

from fastembed import TextEmbedding
model = TextEmbedding("BAAI/bge-small-en-v1.5")

def encode(texts, path, query=False):
    if os.path.exists(path):
        return np.load(path)
    fn = model.query_embed if query else model.embed
    vecs = []
    batch = 64
    for i in range(0, len(texts), batch):
        vecs.extend(fn(texts[i:i + batch]))
        if (i // batch) % 20 == 0:
            print("%s %d/%d" % (os.path.basename(path), i, len(texts)), flush=True)
    arr = np.array(vecs, dtype=np.float32)
    np.save(path, arr)
    return arr

skill_texts = [(s["name"] + " " + s["description"])[:2000] for s in skills]
query_texts = [q["query"][:4000] for q in queries]

se = encode(skill_texts, os.path.join(EMB, "skill_emb.npy"))
qe = encode(query_texts, os.path.join(EMB, "query_emb.npy"), query=True)

se_n = se / np.linalg.norm(se, axis=1, keepdims=True)
qe_n = qe / np.linalg.norm(qe, axis=1, keepdims=True)

desc_bytes = sum(len((s["name"] + "\n" + s["description"]).encode("utf-8")) for s in skills)
ids = [s["id"] for s in skills]

with open(os.path.join(OUT, "runs/dense.jsonl"), "w") as f:
    for qi, q in enumerate(queries):
        sims = se_n @ qe_n[qi]
        top = np.argpartition(-sims, 20)[:20]
        top = top[np.argsort(-sims[top])]
        ranked = [ids[i] for i in top]
        f.write(json.dumps({"qid": q["qid"], "ranked": ranked, "read_bytes": desc_bytes}) + "\n")
print("dense done")
