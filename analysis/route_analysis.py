#!/usr/bin/env python3
"""Classify every holon-tree failure and compare it with the LLM tree run.

Usage: python3 analysis/route_analysis.py [srb toolret skillret]

Reads only local files.  Writes analysis/summary_<ds>.json and
analysis/details_<ds>.jsonl.  The LLM run files are read, never written.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import holon_lib as H

CLASS_ORDER = [
    "ambiguous_root", "no_match_root", "stop_group", "ambiguous_group",
    "wrong_branch", "leaf_wrong", "leaf",
]
CLASS_ZH = {
    "ambiguous_root": "根级多分支歧义",
    "no_match_root": "根级无匹配",
    "stop_group": "停在组/父节点(下级0命中)",
    "ambiguous_group": "组/父节点内多分支歧义",
    "wrong_branch": "走错分支(落到非gold组)",
    "leaf_wrong": "到叶子但选错(同组)",
    "leaf": "到叶子且命中gold",
}


def root_hits(data, text):
    return H.oc.hits_under(data["root"], text, data["skills"], data["syn"])


def matched_words_for(data, d, text):
    """Cover words of d or any descendant that the query hits."""
    skills, syn = data["skills"], data["syn"]
    words = set()
    covers, _ = H.oc.parse_desc(skills[d].meta.get("description", ""))
    for w in covers:
        if H.oc.contains(text, H.oc.canonicalize(w, syn)):
            words.add(w.lower())
    for w, _owner in H.oc.inherited_covers(d, skills):
        if H.oc.contains(text, H.oc.canonicalize(w, syn)):
            words.add(w.lower())
    return words


def oracle_status(data, q):
    """Could a correct group/leaf choice be made if sibling ties were broken?
    Returns one of ambiguity_only / leaf_cover_miss / group_cover_miss /
    sub_cover_miss / no_gold_path.
    """
    root, skills, syn = data["root"], data["skills"], data["syn"]
    text = H.oc.canonicalize(q["query"], syn)
    statuses = []
    for sid, r in H.gold_paths(data, q["gold"]):
        comps = H.path_nodes(r)
        cur, ok, miss = root, True, None
        for i, comp in enumerate(comps[:-1]):
            node = root.joinpath(*comps[:i + 1])
            hits = H.oc.hits_under(cur, text, skills, syn)
            if node not in hits:
                ok = False
                miss = "group_cover_miss" if i == 0 else "sub_cover_miss"
                break
            cur = node
        if not ok:
            statuses.append(miss)
            continue
        leaf = root.joinpath(*comps)
        lhits = H.oc.hits_under(cur, text, skills, syn)
        statuses.append("ambiguity_only" if leaf in lhits else "leaf_cover_miss")
    for s in ("ambiguity_only", "leaf_cover_miss", "sub_cover_miss", "group_cover_miss"):
        if s in statuses:
            return s
    return "no_gold_path"


def path_covers(data, rel_path, mode):
    """Unique covers written on the nodes of a gold path, and which the query hits."""
    skills, syn = data["skills"], data["syn"]
    covers = []
    seen = set()
    for i in range(len(H.path_nodes(rel_path))):
        node = data["root"].joinpath(*H.path_nodes(rel_path)[:i + 1])
        if node not in skills:
            continue
        cs, _ = H.oc.parse_desc(skills[node].meta.get("description", ""))
        for c in sorted(cs, key=str.lower):
            k = c.lower()
            if k not in seen:
                seen.add(k)
                covers.append(c)
    return covers


def overlap_metrics(data, q, mode):
    """mode: exact | stem | stem_syn.  Returns cover recall and query-token coverage."""
    use_stem = mode in ("stem", "stem_syn")
    use_syn = mode in ("stem_syn",)
    if mode == "exact":
        qtext = H.oc.canonicalize(q["query"], data["syn"])
    else:
        qtext = H.norm_text(q["query"], use_stem, use_syn)
    qtoks = H.norm_tokens(q["query"], use_stem, use_syn)
    qtoks = {t for t in qtoks if len(t) >= 3 and t not in H.STOP}
    best = None
    for sid, r in H.gold_paths(data, q["gold"]):
        covers = path_covers(data, r, mode)
        nc = len(covers)
        hit = 0
        norms = []
        for c in covers:
            cn = H.oc.canonicalize(c, data["syn"]) if mode == "exact" else H.norm_text(c, use_stem, use_syn)
            norms.append(cn)
            if H.cover_in_text(cn, qtext):
                hit += 1
        if qtoks:
            covered = 0
            for t in qtoks:
                if any(H.cover_in_text(t, cn) if re.fullmatch(r"[a-z0-9]+", t)
                       else (t in cn) for cn in norms):
                    covered += 1
            qcov = covered / len(qtoks)
        else:
            qcov = 0.0
        rec = (hit / nc) if nc else 0.0
        cand = (rec, qcov, int(hit > 0))
        if best is None or cand > best:
            best = cand
    if best is None:
        return {"cover_recall": 0.0, "query_token_coverage": 0.0, "any_cover": 0}
    return {"cover_recall": best[0], "query_token_coverage": best[1], "any_cover": best[2]}


def classify(data, q):
    root = data["root"]
    text = H.oc.canonicalize(q["query"], data["syn"])
    path = H.oc.route(q["query"], root, data["skills"], data["syn"])
    last = path[-1]

    if isinstance(last, tuple):
        cls = "ambiguous_root"
        root_hit_nodes = last[1]
        path_rel = ["AMBIG:" + ",".join(H.rel(root, x) for x in last[1])]
    elif last == root:
        cls = "no_match_root"
        root_hit_nodes = []
        path_rel = ["."]
    else:
        r = H.rel(root, last)
        root_hit_nodes = root_hits(data, text)
        path_rel = [H.rel(root, x) for x in path]
        if r in data["rel2id"]:
            cls = "leaf"
        else:
            hits_at = H.oc.hits_under(last, text, data["skills"], data["syn"])
            cls = "ambiguous_group" if len(hits_at) > 1 else "stop_group"

    leaf_id = data["rel2id"].get(path_rel[-1]) if path_rel[-1] in data["rel2id"] else None
    hit1 = bool(leaf_id and leaf_id in q["gold"])
    if cls == "leaf" and not hit1:
        # split "reached the right branch but the wrong leaf" from a wrong branch
        sel_parent = H.parent_rel(path_rel[-1])
        gold_parents = {H.parent_rel(r) for _sid, r in H.gold_paths(data, q["gold"])}
        cls = "leaf_wrong" if sel_parent in gold_parents else "wrong_branch"

    # words/rels behind root ambiguity
    root_hit_rels = [H.rel(root, x) for x in root_hit_nodes]
    bridge = {}
    if len(root_hit_nodes) > 1:
        per = []
        for g in root_hit_nodes:
            per.append(matched_words_for(data, g, text))
        shared = Counter()
        for ws in per:
            for w in ws:
                shared[w] += 1
        bridge = {
            "shared_words": [w for w, n in shared.most_common() if n >= 2][:10],
            "all_hit_by_one_word": sorted(set.intersection(*per))[:10] if per else [],
        }

    return {
        "qid": q["qid"], "setting": q.get("setting"), "lang": q.get("lang"),
        "query": q["query"], "gold": q["gold"], "class": cls, "hit1": hit1,
        "path": path_rel, "leaf_id": leaf_id,
        "n_root_hits": len(root_hit_nodes), "root_hit_rels": root_hit_rels,
        "oracle": oracle_status(data, q), "bridge": bridge,
        "overlap": {m: overlap_metrics(data, q, m) for m in ("exact", "stem", "stem_syn")},
    }


def load_llm(data):
    p = data["base"] / "runs" / "llm-tree.jsonl"
    if not p.exists():
        return {}
    out = {}
    for line in open(p, encoding="utf-8"):
        r = json.loads(line)
        out[r["qid"]] = r
    return out


def summarize(data, details):
    n = len(details)
    counts = Counter(d["class"] for d in details)
    hit = sum(d["hit1"] for d in details)
    oracle = Counter(d["oracle"] for d in details)
    root_n = [d["n_root_hits"] for d in details]
    amb = [d for d in details if len(d["root_hit_rels"]) > 1]

    # aggregate "bridge" words
    word_q = Counter()
    word_groups = defaultdict(set)
    one_word_all = 0
    for d in amb:
        if d["bridge"].get("all_hit_by_one_word"):
            one_word_all += 1
        for w in d["bridge"].get("shared_words", []):
            word_q[w] += 1
        for g in d["root_hit_rels"]:
            for w in d["bridge"].get("shared_words", []):
                word_groups[w].add(g)
    top_words = [
        {"word": w, "queries": c, "groups": len(word_groups[w])}
        for w, c in word_q.most_common(20)
    ]

    llm = load_llm(data)
    cross = Counter()
    llm_wrong_holon_right = []
    llm_right_holon_wrong = []
    for d in details:
        if d["qid"] not in llm:
            continue
        lr = llm[d["qid"]]
        lhit = bool(lr.get("ranked") and lr["ranked"][0] in d["gold"])
        key = ("llm_hit" if lhit else "llm_miss") + "__" + ("holon_hit" if d["hit1"] else "holon_miss")
        cross[key] += 1
        if lhit and not d["hit1"]:
            llm_right_holon_wrong.append(d)
        if not lhit and d["hit1"]:
            llm_wrong_holon_right.append(d)

    def overlap_avg(items, mode, field):
        if not items:
            return None
        vals = [d["overlap"][mode][field] for d in items]
        return sum(vals) / len(vals)

    def oracle_counts(items):
        c = Counter(d["oracle"] for d in items)
        return dict(c)

    return {
        "dataset": data["ds"], "n": n, "hit1": hit / n if n else 0.0,
        "classes": {k: {"n": counts.get(k, 0), "pct": counts.get(k, 0) / n if n else 0.0}
                    for k in CLASS_ORDER},
        "oracle": {k: {"n": v, "pct": v / n if n else 0.0} for k, v in oracle.items()},
        "root_hits": {
            "mean": sum(root_n) / n if n else 0.0,
            "max": max(root_n) if root_n else 0,
            "ge2": sum(1 for x in root_n if x >= 2),
            "hist": {str(k): root_n.count(k) for k in sorted(set(root_n))},
        },
        "ambiguity": {
            "n": len(amb), "one_word_explains_all": one_word_all,
            "top_bridge_words": top_words,
        },
        "llm_cross": dict(cross),
        "llm_n": sum(cross.values()),
        "llm_right_holon_wrong": {
            "n": len(llm_right_holon_wrong),
            "oracle": oracle_counts(llm_right_holon_wrong),
            "exact": {
                "cover_recall": overlap_avg(llm_right_holon_wrong, "exact", "cover_recall"),
                "query_token_coverage": overlap_avg(llm_right_holon_wrong, "exact", "query_token_coverage"),
                "any_cover": overlap_avg(llm_right_holon_wrong, "exact", "any_cover"),
            },
            "stem": {
                "cover_recall": overlap_avg(llm_right_holon_wrong, "stem", "cover_recall"),
                "query_token_coverage": overlap_avg(llm_right_holon_wrong, "stem", "query_token_coverage"),
                "any_cover": overlap_avg(llm_right_holon_wrong, "stem", "any_cover"),
            },
            "stem_syn": {
                "cover_recall": overlap_avg(llm_right_holon_wrong, "stem_syn", "cover_recall"),
                "query_token_coverage": overlap_avg(llm_right_holon_wrong, "stem_syn", "query_token_coverage"),
                "any_cover": overlap_avg(llm_right_holon_wrong, "stem_syn", "any_cover"),
            },
        },
        "holon_wrong_all_overlap": {
            "exact": {
                "cover_recall": overlap_avg([d for d in details if not d["hit1"]], "exact", "cover_recall"),
                "query_token_coverage": overlap_avg([d for d in details if not d["hit1"]], "exact", "query_token_coverage"),
                "any_cover": overlap_avg([d for d in details if not d["hit1"]], "exact", "any_cover"),
            },
            "stem_syn": {
                "cover_recall": overlap_avg([d for d in details if not d["hit1"]], "stem_syn", "cover_recall"),
                "query_token_coverage": overlap_avg([d for d in details if not d["hit1"]], "stem_syn", "query_token_coverage"),
                "any_cover": overlap_avg([d for d in details if not d["hit1"]], "stem_syn", "any_cover"),
            },
        },
    }


def pick_examples(details, n=3):
    by = defaultdict(list)
    for d in details:
        by[d["class"]].append(d)
    out = {}
    for cls, items in by.items():
        items = sorted(items, key=lambda d: (len(d["query"]), d["qid"]))
        out[cls] = items[:n]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("datasets", nargs="*", default=["srb", "toolret"])
    args = ap.parse_args()
    outdir = Path(__file__).resolve().parent
    combined = {}
    for ds in args.datasets:
        print("loading", ds, flush=True)
        data = H.load_dataset(ds)
        details = []
        for i, q in enumerate(data["queries"]):
            details.append(classify(data, q))
            if (i + 1) % 500 == 0:
                print("  routed", i + 1, flush=True)
        s = summarize(data, details)
        s["examples"] = pick_examples(details)
        combined[ds] = s
        with open(outdir / ("details_%s.jsonl" % ds), "w", encoding="utf-8") as f:
            for d in details:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
        with open(outdir / ("summary_%s.json" % ds), "w", encoding="utf-8") as f:
            json.dump({"summary": s, "examples": s["examples"]}, f, ensure_ascii=False, indent=1)
        print(ds, "hit1=%.4f" % s["hit1"], "classes=", {k: v["n"] for k, v in s["classes"].items()},
              "oracle=", {k: v["n"] for k, v in s["oracle"].items()}, flush=True)
    with open(outdir / "summary_all.json", "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
