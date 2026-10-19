#!/usr/bin/env python3
"""Run deterministic lexical methods for srb: holon-tree, flat-literal, bm25-desc, bm25-body."""
import json
import re
import sys
from pathlib import Path

BENCH = Path("/workspace/work/bench")
OUT = BENCH / "ds" / "srb"
sys.path.insert(0, str(BENCH / "holon" / "organizer" / "scripts"))
sys.path.insert(0, str(BENCH / "holon" / "scripts"))
import holon  # noqa: E402
import organizer_cli as oc  # noqa: E402

TOKEN_RE = re.compile(r"[a-z0-9]+|[\uac00-\ud7a3]+")


def tok(text):
    return TOKEN_RE.findall(text.lower())


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8")]


def run_tree(libname, queries, dir2id):
    root = (OUT / libname).resolve()
    skills, errors = oc.find_skills(root)
    assert not errors, errors
    syn = oc.load_synonyms(root)
    size = {d: (d / holon.SKILL_FILE).stat().st_size for d in skills}
    recs, stats = [], {"stop_root": 0, "stop_group": 0, "ambig": 0, "leaf": 0}
    for q in queries:
        path = oc.route(q["query"], root, skills, syn)
        last = path[-1]
        dirs = [p for p in path if not isinstance(p, tuple)]
        read_bytes = sum(size[d] for d in dirs)
        ranked = []
        if isinstance(last, tuple):
            stats["ambig"] += 1
        elif last == root:
            stats["stop_root"] += 1
        elif oc.children_of(last, skills):
            stats["stop_group"] += 1
        else:
            stats["leaf"] += 1
            ranked = [dir2id[last.name]]
        recs.append({"qid": q["qid"], "ranked": ranked, "read_bytes": read_bytes})
    return recs, stats


def main():
    skills = load_jsonl(OUT / "skills.jsonl")
    queries = load_jsonl(OUT / "queries.jsonl")
    dir_map = json.load(open(OUT / "dir_map.json"))
    dir2id = {v: k for k, v in dir_map.items()}
    (OUT / "runs").mkdir(exist_ok=True)

    for lib, method in (("tree", "holon-tree"), ("flat", "flat-literal")):
        recs, stats = run_tree(lib, queries, dir2id)
        with open(OUT / "runs" / (method + ".jsonl"), "w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(method, stats)

    # BM25
    from rank_bm25 import BM25Okapi
    desc_bytes = sum(len((s["name"] + s["description"]).encode("utf-8")) for s in skills)
    body_bytes = sum(len((s["name"] + s["description"] + s["body"]).encode("utf-8")) for s in skills)
    ids = [s["id"] for s in skills]
    for method, docfn, rb in (
        ("bm25-desc", lambda s: s["name"] + " " + s["description"], desc_bytes),
        ("bm25-body", lambda s: s["name"] + " " + s["description"] + " " + s["body"], body_bytes),
    ):
        bm25 = BM25Okapi([tok(docfn(s)) for s in skills])
        with open(OUT / "runs" / (method + ".jsonl"), "w", encoding="utf-8") as f:
            for q in queries:
                scores = bm25.get_scores(tok(q["query"]))
                order = sorted(range(len(ids)), key=lambda i: (-scores[i], ids[i]))[:20]
                f.write(json.dumps({"qid": q["qid"], "ranked": [ids[i] for i in order],
                                    "read_bytes": rb}, ensure_ascii=False) + "\n")
        print(method, "read_bytes/query", rb)


if __name__ == "__main__":
    main()
