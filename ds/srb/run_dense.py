#!/usr/bin/env python3
"""Dense (fastembed) + hybrid (RRF of bm25-desc and dense) for srb.

English queries: BAAI/bge-small-en-v1.5. Korean queries:
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2. Skill texts are encoded
with the model of the query being scored (two caches in emb/).
"""
import json
import sys
from pathlib import Path

import numpy as np

BENCH = Path("/workspace/work/bench")
OUT = BENCH / "ds" / "srb"
EMB = OUT / "emb"
EMB.mkdir(exist_ok=True)


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8")]


def encode(model, texts, cache):
    if cache.with_suffix(".npy").exists():
        return np.load(cache.with_suffix(".npy"))
    from fastembed import TextEmbedding
    emb = TextEmbedding(model_name=model)
    vecs = np.array(list(emb.embed(texts, batch_size=16)))
    np.save(cache.with_suffix(".npy"), vecs)
    return vecs


def cos_top(query_vec, mat, ids, k=20):
    q = query_vec / (np.linalg.norm(query_vec) + 1e-12)
    m = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-12)
    scores = m @ q
    order = sorted(range(len(ids)), key=lambda i: (-scores[i], ids[i]))[:k]
    return [ids[i] for i in order]


def main():
    skills = load_jsonl(OUT / "skills.jsonl")
    queries = load_jsonl(OUT / "queries.jsonl")
    ids = [s["id"] for s in skills]
    texts = [s["name"] + ". " + s["description"] for s in skills]
    desc_bytes = sum(len(t.encode("utf-8")) for t in texts)

    EN = "BAAI/bge-small-en-v1.5"
    KO = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    sk_en = encode(EN, texts, EMB / "skills_bge")
    q_en_texts = [q["query"] for q in queries if q["lang"] == "en"]
    q_en = encode(EN, q_en_texts, EMB / "queries_bge")

    sk_ko = encode(KO, texts, EMB / "skills_multi")
    q_ko_texts = [q["query"] for q in queries if q["lang"] == "ko"]
    sk_ko_needed = any(q["lang"] == "ko" for q in queries)
    q_ko = encode(KO, q_ko_texts, EMB / "queries_multi") if sk_ko_needed else None

    iter_en = iter(q_en)
    iter_ko = iter(q_ko) if q_ko is not None else None
    dense_rank = {}
    for q in queries:
        if q["lang"] == "ko":
            dense_rank[q["qid"]] = cos_top(next(iter_ko), sk_ko, ids)
        else:
            dense_rank[q["qid"]] = cos_top(next(iter_en), sk_en, ids)

    with open(OUT / "runs" / "dense.jsonl", "w", encoding="utf-8") as f:
        for q in queries:
            f.write(json.dumps({"qid": q["qid"], "ranked": dense_rank[q["qid"]],
                                "read_bytes": desc_bytes}, ensure_ascii=False) + "\n")
    print("dense done")

    # hybrid: RRF k=60 of bm25-desc and dense (both read name+description once; same pass)
    bm25_rank = {r["qid"]: r["ranked"] for r in load_jsonl(OUT / "runs" / "bm25-desc.jsonl")}
    K = 60
    with open(OUT / "runs" / "hybrid.jsonl", "w", encoding="utf-8") as f:
        for q in queries:
            score = {}
            for src in (bm25_rank[q["qid"]], dense_rank[q["qid"]]):
                for rank, sid in enumerate(src):
                    score[sid] = score.get(sid, 0.0) + 1.0 / (K + rank + 1)
            top = sorted(score, key=lambda s: (-score[s], s))[:20]
            f.write(json.dumps({"qid": q["qid"], "ranked": top,
                                "read_bytes": desc_bytes}, ensure_ascii=False) + "\n")
    print("hybrid done")


if __name__ == "__main__":
    main()
