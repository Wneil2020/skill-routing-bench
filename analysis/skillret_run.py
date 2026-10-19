#!/usr/bin/env python3
"""Run the failure classification and ablations for skillret.

Same logic as route_analysis.py / improve_experiment.py, but:
  - load_llm is disabled (the llm-* run files are being written by a live
    llm_runner.py and must not be read),
  - the existing holon-tree run (runs/holon-tree.jsonl, no llm-*) is scored
    with a local scorer so its official Hit@1 is on record.

Usage: python3 analysis/skillret_run.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import route_analysis as RA  # noqa: E402
import improve_experiment as IE  # noqa: E402
import holon_lib as H  # noqa: E402

RA.load_llm = lambda data: {}


def score_holon_run(data):
    p = data["base"] / "runs" / "holon-tree.jsonl"
    hit = n = 0
    mrr = 0.0
    for line in open(p, encoding="utf-8"):
        r = json.loads(line)
        q = data["qmap"].get(r["qid"])
        if q is None:
            continue
        n += 1
        ranked = r.get("ranked") or []
        if ranked and ranked[0] in q["gold"]:
            hit += 1
            mrr += 1.0
        else:
            for i, sid in enumerate(ranked):
                if sid in q["gold"]:
                    mrr += 1.0 / (i + 1)
                    break
    return {"n": n, "hit1": hit / n if n else 0.0, "mrr": mrr / n if n else 0.0}


def main():
    outdir = Path(__file__).resolve().parent
    ds = "skillret"
    print("loading", ds, flush=True)
    data = H.load_dataset(ds)
    run_score = score_holon_run(data)
    print("runs/holon-tree.jsonl:", run_score, flush=True)

    details = []
    for i, q in enumerate(data["queries"]):
        details.append(RA.classify(data, q))
        if (i + 1) % 500 == 0:
            print("  routed", i + 1, flush=True)
    s = RA.summarize(data, details)
    s["examples"] = RA.pick_examples(details)
    s["holon_run"] = run_score
    with open(outdir / ("details_%s.jsonl" % ds), "w", encoding="utf-8") as f:
        for d in details:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    with open(outdir / ("summary_%s.json" % ds), "w", encoding="utf-8") as f:
        json.dump({"summary": s, "examples": s["examples"]}, f, ensure_ascii=False, indent=1)
    print(ds, "hit1=%.4f" % s["hit1"], "classes=", {k: v["n"] for k, v in s["classes"].items()},
          "oracle=", {k: v["n"] for k, v in s["oracle"].items()}, flush=True)

    print("ablations", ds, flush=True)
    ab = IE.run(ds)
    allout = json.load(open(outdir / "improve_results.json"))
    allout[ds] = ab
    with open(outdir / "improve_results.json", "w", encoding="utf-8") as f:
        json.dump(allout, f, ensure_ascii=False, indent=1)
    for k, v in ab.items():
        if k == "llm_sample":
            print("  sample:", {kk: round(vv["hit1"], 4) for kk, vv in v.items()}, flush=True)
        else:
            print("  %-20s hit1=%.4f classes=%s" % (k, v["hit1"], v["classes"]), flush=True)


if __name__ == "__main__":
    main()
