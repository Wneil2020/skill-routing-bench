#!/usr/bin/env python3
"""Deterministic ablations: stemming, hand synonym folding, IDF tie-break, flat scoring.

Usage: python3 analysis/improve_experiment.py [srb toolret]

The baseline is exactly organizer_cli.route().  Every other row is a diagnostic
variant built on the same tree and the same cover words.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import holon_lib as H


def classify(data, path, router, query_text):
    root = data["root"]
    last = path[-1]
    if isinstance(last, tuple):
        return "ambiguous_root"
    if last == root:
        return "no_match_root"
    if not router.children.get(last):
        return "leaf"
    hits = router.hits_under(last, query_text)
    return "ambiguous_group" if len(hits) > 1 else "stop_group"


def eval_route(data, fn, router):
    classes = Counter()
    hit = 0
    for q in data["queries"]:
        path = fn(q["query"])
        cls = classify(data, path, router, router.norm(q["query"]))
        classes[cls] += 1
        if cls == "leaf":
            leaf = data["rel2id"].get(H.rel(data["root"], path[-1]))
            if leaf in q["gold"]:
                hit += 1
    n = len(data["queries"])
    return {"n": n, "hit1": hit / n, "hit": hit, "classes": dict(classes)}


def eval_flat(data, router, k=20):
    classes = Counter()
    hit = 0
    for q in data["queries"]:
        ranked = router.rank_leaves(q["query"], k=k)
        if ranked:
            classes["leaf"] += 1
            if data["rel2id"].get(ranked[0][2]) in q["gold"]:
                hit += 1
        else:
            classes["no_match_root"] += 1
    n = len(data["queries"])
    return {"n": n, "hit1": hit / n, "hit": hit, "classes": dict(classes)}


def run(ds):
    data = H.load_dataset(ds)
    out = {}

    base = {"n": len(data["queries"]), "hit1": 0.0, "hit": 0, "classes": {}}
    cls = Counter()
    for q in data["queries"]:
        path = H.oc.route(q["query"], data["root"], data["skills"], data["syn"])
        last = path[-1]
        if isinstance(last, tuple):
            c = "ambiguous_root"
        elif last == data["root"]:
            c = "no_match_root"
        else:
            r = H.rel(data["root"], last)
            if r in data["rel2id"]:
                c = "leaf"
                if data["rel2id"][r] in q["gold"]:
                    base["hit"] += 1
            else:
                text = H.oc.canonicalize(q["query"], data["syn"])
                hits = H.oc.hits_under(last, text, data["skills"], data["syn"])
                c = "ambiguous_group" if len(hits) > 1 else "stop_group"
        cls[c] += 1
    base["classes"] = dict(cls)
    base["hit1"] = base["hit"] / base["n"]
    out["exact_strict"] = base

    for name, stem, syn in (
        ("stem_strict", True, False),
        ("stem_syn_strict", True, True),
        ("score_exact", False, False),
        ("score_stem", True, False),
        ("score_stem_syn", True, True),
    ):
        router = H.NormalRouter(data, use_stem=stem, use_syn=syn)
        if name.startswith("score"):
            fn = router.route_score
        else:
            fn = router.route_strict
        out[name] = eval_route(data, fn, router)

    for name, stem, syn in (
        ("flat_score_exact", False, False),
        ("flat_score_stem_syn", True, True),
    ):
        router = H.NormalRouter(data, use_stem=stem, use_syn=syn)
        out[name] = eval_flat(data, router)

    # Same ablation restricted to the 300 qids the LLM tree run actually saw.
    llm_p = data["base"] / "runs" / "llm-tree.jsonl"
    if llm_p.exists():
        qids = {json.loads(l)["qid"] for l in open(llm_p, encoding="utf-8")}
        sub = dict(data)
        sub["queries"] = [q for q in data["queries"] if q["qid"] in qids]
        subout = {}
        cls = Counter()
        hit = 0
        for q in sub["queries"]:
            path = H.oc.route(q["query"], data["root"], data["skills"], data["syn"])
            last = path[-1]
            if isinstance(last, tuple):
                c = "ambiguous_root"
            elif last == data["root"]:
                c = "no_match_root"
            else:
                r = H.rel(data["root"], last)
                if r in data["rel2id"]:
                    c = "leaf"
                    if data["rel2id"][r] in q["gold"]:
                        hit += 1
                else:
                    text = H.oc.canonicalize(q["query"], data["syn"])
                    hits = H.oc.hits_under(last, text, data["skills"], data["syn"])
                    c = "ambiguous_group" if len(hits) > 1 else "stop_group"
            cls[c] += 1
        n = len(sub["queries"])
        subout["exact_strict"] = {"n": n, "hit1": hit / n, "hit": hit, "classes": dict(cls)}
        for name, stem_use, syn_use in (
            ("stem_syn_strict", True, True),
            ("score_exact", False, False),
            ("score_stem_syn", True, True),
        ):
            router = H.NormalRouter(data, use_stem=stem_use, use_syn=syn_use)
            fn = router.route_score if name.startswith("score") else router.route_strict
            subout[name] = eval_route(sub, fn, router)
        for name, stem_use, syn_use in (("flat_score_stem_syn", True, True),):
            router = H.NormalRouter(data, use_stem=stem_use, use_syn=syn_use)
            subout[name] = eval_flat(sub, router)
        out["llm_sample"] = subout
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="*", default=["srb", "toolret"])
    args = ap.parse_args()
    outdir = Path(__file__).resolve().parent
    allout = {}
    for ds in args.datasets:
        print("experiment", ds, flush=True)
        allout[ds] = run(ds)
        for k, v in allout[ds].items():
            if k == "llm_sample":
                print(" sample:", {kk: round(vv["hit1"], 4) for kk, vv in v.items()}, flush=True)
            else:
                print(" %-20s hit1=%.4f hit=%d classes=%s" % (k, v["hit1"], v["hit"], v["classes"]), flush=True)
    with open(outdir / "improve_results.json", "w", encoding="utf-8") as f:
        json.dump(allout, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
