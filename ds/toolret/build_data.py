#!/usr/bin/env python3
"""Build ds/toolret: skills.jsonl, queries.jsonl from ToolRet metatool parquet."""
import json
from pathlib import Path

import pandas as pd

BASE = Path("/workspace/work/bench")
DATA = BASE / "data" / "toolret"
OUT = BASE / "ds" / "toolret"
OUT.mkdir(parents=True, exist_ok=True)

q = pd.read_parquet(DATA / "metatool_queries.parquet")
tools = pd.read_parquet(DATA / "tools_customized.parquet")

referenced = set()
for lab in q["labels"]:
    for l in json.loads(lab):
        referenced.add(l["id"])

doc_by_id = dict(zip(tools["id"], tools["documentation"]))
keep = sorted(referenced)
assert all(i in doc_by_id for i in keep), "missing tool docs"


def parse_doc(raw):
    d = json.loads(raw)
    name = d.get("name", "").strip()
    desc = d.get("description", "").strip()
    return name, desc, d


skills = []
for tid in keep:
    name, desc, d = parse_doc(doc_by_id[tid])
    body = json.dumps(d, ensure_ascii=False, indent=1)[:8000]
    skills.append({"id": tid, "name": name, "description": desc, "body": body, "group": []})

with (OUT / "skills.jsonl").open("w", encoding="utf-8") as f:
    for s in skills:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

with (OUT / "queries.jsonl").open("w", encoding="utf-8") as f:
    for _, r in q.iterrows():
        gold = [l["id"] for l in json.loads(r["labels"])]
        f.write(json.dumps({"qid": r["id"], "query": r["query"], "gold": gold,
                            "setting": "all", "lang": "en"}, ensure_ascii=False) + "\n")

print(f"skills: {len(skills)}, queries: {len(q)}")
