#!/usr/bin/env python3
"""Incremental dense encoding for ds/skillret.

Encodes skills then queries in shards of 256. Each finished shard is saved
immediately to emb/{skill,query}_shard_%03d.npy. Stops when the time budget
(default 80s) is exhausted; re-invoke to resume. Exits 0 when everything is
encoded, 3 when more shards remain.
"""
import glob, json, os, sys, time
import numpy as np

OUT = "/workspace/work/bench/ds/skillret"
EMB = os.path.join(OUT, "emb")
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 80.0
SHARD = 256

skills = [json.loads(l) for l in open(os.path.join(OUT, "skills.jsonl"))]
queries = [json.loads(l) for l in open(os.path.join(OUT, "queries.jsonl"))]
texts = {
    "skill": [(s["name"] + " " + s["description"])[:2000] for s in skills],
    "query": [q["query"][:4000] for q in queries],
}

from fastembed import TextEmbedding
model = TextEmbedding("BAAI/bge-small-en-v1.5")

t0 = time.time()
remaining = 0
for kind in ("skill", "query"):
    ts = texts[kind]
    n_shards = (len(ts) + SHARD - 1) // SHARD
    fn = model.query_embed if kind == "query" else model.embed
    for si in range(n_shards):
        path = os.path.join(EMB, "%s_shard_%03d.npy" % (kind, si))
        if os.path.exists(path):
            continue
        if time.time() - t0 > BUDGET:
            remaining += n_shards - si
            break
        chunk = ts[si * SHARD:(si + 1) * SHARD]
        vecs = np.array(list(fn(chunk)), dtype=np.float32)
        np.save(path + ".tmp", vecs)
        os.rename(path + ".tmp", path)
        print("saved %s (%d vecs, %.1fs)" % (os.path.basename(path), len(vecs), time.time() - t0), flush=True)
    else:
        continue
    break

left = 0
for kind in ("skill", "query"):
    ts = texts[kind]
    n_shards = (len(ts) + SHARD - 1) // SHARD
    have = len(glob.glob(os.path.join(EMB, "%s_shard_*.npy" % kind)))
    left += n_shards - have
print("shards remaining: %d" % left, flush=True)
sys.exit(3 if left else 0)
