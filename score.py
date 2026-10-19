#!/usr/bin/env python3
"""Shared scorer. Usage: python3 score.py ds/<ds>

Reads ds/<ds>/queries.jsonl and ds/<ds>/runs/<method>.jsonl, writes
ds/<ds>/results.md with per-method x per-setting Hit@1, Recall@5, MRR,
mean read_bytes, n (plus an "all" row per method).
Hit@1: first ranked id is in gold. Recall@5: fraction of gold covered by top5.
MRR: 1/rank of first gold hit. Methods whose ranked has <5 entries score Recall@5
on what they returned.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8")]


def main():
    ds = Path(sys.argv[1])
    queries = {q["qid"]: q for q in load_jsonl(ds / "queries.jsonl")}
    settings = sorted({q["setting"] for q in queries.values()})
    rows = []
    for run in sorted((ds / "runs").glob("*.jsonl")):
        method = run.stem
        recs = load_jsonl(run)
        agg = defaultdict(lambda: {"n": 0, "hit1": 0.0, "rec5": 0.0, "mrr": 0.0, "bytes": 0})
        for r in recs:
            q = queries[r["qid"]]
            gold = q["gold"]
            ranked = r["ranked"]
            hit1 = 1.0 if ranked and ranked[0] in gold else 0.0
            top5 = ranked[:5]
            rec5 = (sum(1 for g in gold if g in top5) / len(gold)) if gold else 0.0
            mrr = 0.0
            for i, sid in enumerate(ranked):
                if sid in gold:
                    mrr = 1.0 / (i + 1)
                    break
            for key in (q["setting"], "all"):
                a = agg[key]
                a["n"] += 1
                a["hit1"] += hit1
                a["rec5"] += rec5
                a["mrr"] += mrr
                a["bytes"] += r["read_bytes"]
        for key in settings + ["all"]:
            if key not in agg:
                continue
            a = agg[key]
            n = a["n"]
            rows.append((method, key, a["hit1"] / n, a["rec5"] / n, a["mrr"] / n,
                         a["bytes"] / n, n))

    lines = ["# %s results" % ds.name, "",
             "| method | setting | Hit@1 | Recall@5 | MRR | avg read_bytes | n |",
             "|---|---|---:|---:|---:|---:|---:|"]
    for method, setting, h1, r5, mrr, rb, n in rows:
        lines.append("| %s | %s | %.4f | %.4f | %.4f | %d | %d |"
                     % (method, setting, h1, r5, mrr, round(rb), n))
    out = ds / "results.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote %s (%d rows)" % (out, len(rows)))


if __name__ == "__main__":
    main()
