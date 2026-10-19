#!/usr/bin/env python3
"""holon-tree and flat-literal runs for ds/skillret.

Faithful to organizer_cli.route(): same descent rules (1 hit -> descend,
>1 hit at root -> AMBIG, >1 below root -> stop at parent), but cover-word
presence per query is computed once with one combined regex (same word set
and boundary semantics as organizer_cli.contains) so 6006-node libraries
route in reasonable time. Synonyms table is empty in this library, so
canonicalize() is just lowercasing.
"""
import json, os, re, sys, time
from pathlib import Path

sys.path.insert(0, "/workspace/work/bench/holon/organizer/scripts")
import organizer_cli as oc

OUT = "/workspace/work/bench/ds/skillret"
queries = [json.loads(l) for l in open(os.path.join(OUT, "queries.jsonl"))]
skills = {s["id"]: s for s in
          (json.loads(l) for l in open(os.path.join(OUT, "skills.jsonl")))}

desc_bytes = sum(len((s["name"] + "\n" + s["description"]).encode("utf-8"))
                 for s in skills.values())


def piece(w):
    if re.fullmatch(r"[A-Za-z0-9_.\-]+", w):
        return r"(?<![A-Za-z0-9_])" + re.escape(w) + r"(?![A-Za-z0-9_])"
    return re.escape(w)


def run_library(root, path_map, out_name, flat):
    root = Path(root)
    sk, errors = oc.find_skills(root)
    assert not errors, errors
    syn = oc.load_synonyms(root)
    assert not syn

    covers = {}   # dir -> (own cover set, exclude set)
    words = set()
    for d, s in sk.items():
        cov, excl = oc.parse_desc(s.meta.get("description", ""))
        covers[d] = (cov, excl)
        words.update(cov)
        words.update(excl)
    big = re.compile("|".join(piece(w) for w in sorted(words, key=len, reverse=True)), re.I)

    children = {}
    for d in sk:
        children.setdefault(d.parent, []).append(d)

    # match_skill(): a node also answers to the cover words of its whole subtree
    # (inherited_covers), blocked only by its own excludes.
    sub_covers = {}
    for d in sorted(sk, key=lambda p: len(p.parts), reverse=True):
        agg = set(covers[d][0])
        for c in children.get(d, ()):
            agg |= sub_covers[c]
        sub_covers[d] = agg

    size = {d: os.path.getsize(d / "SKILL.md") for d in sk}
    dir2sid = {tuple(v): k for k, v in path_map.items()}

    stats = {"leaf": 0, "group": 0, "root": 0, "ambig": 0}
    t0 = time.time()
    with open(os.path.join(OUT, "runs", out_name), "w") as f:
        for qi, q in enumerate(queries):
            sent = q["query"].lower()
            matched = set(m.group(0).lower() for m in big.finditer(sent))

            def node_hit(d):
                _, excl = covers[d]
                return bool(sub_covers[d] & matched) and not (excl & matched)

            cur, path = root, [root]
            while True:
                hits = [c for c in children.get(cur, ()) if node_hit(c)]
                if len(hits) == 1:
                    cur = hits[0]
                    path.append(cur)
                elif len(hits) > 1 and cur == root:
                    path.append(("AMBIG", hits))
                    break
                else:
                    break

            last = path[-1]
            ranked = []
            if isinstance(last, tuple):
                stats["ambig"] += 1
            elif cur == root:
                stats["root"] += 1
            elif not children.get(cur):
                key = (cur.relative_to(root).as_posix(),) if flat else tuple(
                    cur.relative_to(root).parts)
                sid = dir2sid.get(key if not flat else (key[0],))
                if sid:
                    ranked = [sid]
                    stats["leaf"] += 1
                else:
                    stats["group"] += 1
            else:
                stats["group"] += 1

            if flat:
                rb = desc_bytes
            else:
                rb = sum(size[d] for d in path if not isinstance(d, tuple))
            f.write(json.dumps({"qid": q["qid"], "ranked": ranked,
                                "read_bytes": rb}) + "\n")
            if qi % 500 == 0:
                print(out_name, qi, "%.1fs" % (time.time() - t0), flush=True)
    print(out_name, "stats:", stats, "%.1fs" % (time.time() - t0), flush=True)


which = sys.argv[1] if len(sys.argv) > 1 else "both"
if which in ("tree", "both"):
    tree_map = json.load(open(os.path.join(OUT, "tree_map.json")))
    run_library(os.path.join(OUT, "tree"), {k: tuple(v) for k, v in tree_map.items()},
                "holon-tree.jsonl", flat=False)

if which in ("flat", "both"):
    flat_map = json.load(open(os.path.join(OUT, "flat_map.json")))
    run_library(os.path.join(OUT, "flat"), {k: (v,) for k, v in flat_map.items()},
                "flat-literal.jsonl", flat=True)
