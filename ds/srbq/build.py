#!/usr/bin/env python3
"""Build ds/srb/{skills.jsonl,queries.jsonl,tree/,flat/} from data/srb.

Cover-word rule (deterministic, k<=5):
  1. name tokens: skill_id split on [-_], keep len>=3, drop stopwords, order kept -> up to 3
  2. korean_triggers: in given order, up to 2 (so Korean queries can match)
  3. IDF fill: tokenize (skill_name + description + trigger_phrases), keep [a-z0-9]
     tokens len>=4 not stopwords; IDF over the 501 per-skill docs; take highest-IDF
     tokens (ties broken alphabetically) not already covers, until 5 covers total.
  trigger_phrases are a cover-word candidate source through step 3 (their content
  words enter the IDF candidate pool of that skill).
Group nodes: covers = group name split on [-_] (len>=3 else the name itself).
Categories (skill.category == skill_id prefix, see statistics.skills_per_category)
with exactly 1 member are merged into "misc".
"""
import json
import math
import os
import re
import sys
from pathlib import Path

BENCH = Path("/workspace/work/bench")
DATA = BENCH / "data" / "srb" / "data"
OUT = BENCH / "ds" / "srb"
sys.path.insert(0, str(BENCH / "holon" / "scripts"))
import holon  # noqa: E402

STOPWORDS = set("""
a an and are as at be been by for from has have how i in into is it its of on or
so that the their them they this to use used using was we what when which will
with you your task skill agent agents workflow workflows process processes
""".split())

TOKEN_RE = re.compile(r"[a-z][a-z0-9]{2,}")


def en_tokens(text):
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS]


def name_tokens(skill_id):
    out = []
    for t in re.split(r"[-_]+", skill_id.lower()):
        if len(t) >= 3 and t not in STOPWORDS and t not in out:
            out.append(t)
    return out


def main():
    corpus = json.load(open(DATA / "skill_corpus.json"))
    queries = json.load(open(DATA / "skillretbench_queries.json"))
    skills = corpus["skills"]
    assert len(skills) == 501

    # --- checks ---
    bad_ids = [s["skill_id"] for s in skills
               if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,62}[a-z0-9]", s["skill_id"] or "")]
    print("invalid ids:", bad_ids)
    ids = [s["skill_id"] for s in skills]
    assert len(set(ids)) == len(ids), "duplicate skill ids"
    cat_mismatch = [s["skill_id"] for s in skills if not s["skill_id"].startswith(s["category"] + "-")]
    print("category!=prefix count:", len(cat_mismatch), cat_mismatch[:5])

    # --- groups: category, singletons -> misc ---
    cat_counts = {}
    for s in skills:
        cat_counts[s["category"]] = cat_counts.get(s["category"], 0) + 1
    group_of = {s["skill_id"]: (s["category"] if cat_counts[s["category"]] > 1 else "misc")
                for s in skills}
    groups = sorted(set(group_of.values()))
    print("groups:", len(groups), {g: sum(1 for v in group_of.values() if v == g) for g in groups})

    # --- IDF over per-skill docs ---
    docs = {}
    for s in skills:
        text = " ".join([s["skill_name"], s["description"], " ".join(s["trigger_phrases"])])
        docs[s["skill_id"]] = en_tokens(text)
    N = len(docs)
    df = {}
    for toks in docs.values():
        for t in set(toks):
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log((N + 1) / (c + 1)) + 1 for t, c in df.items()}

    # --- cover words per skill ---
    covers_of = {}
    for s in skills:
        sid = s["skill_id"]
        covers = name_tokens(sid)[:3]
        for kt in s.get("korean_triggers") or []:
            kt = kt.strip()
            if kt and len(kt) >= 2 and kt not in covers and len(covers) < 5:
                covers.append(kt)
                if sum(1 for c in covers if re.search(r"[가-힣]", c)) >= 2:
                    break
        cands = sorted(set(docs[sid]), key=lambda t: (-idf[t], t))
        for t in cands:
            if len(covers) >= 5:
                break
            if t not in [c.lower() for c in covers] and not re.search(r"[가-힣]", t):
                covers.append(t)
        if len(covers) < 2:
            covers.append(sid)
        covers_of[sid] = covers[:5]

    # --- skills.jsonl ---
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "skills.jsonl", "w", encoding="utf-8") as f:
        for s in skills:
            f.write(json.dumps({
                "id": s["skill_id"],
                "name": s["skill_name"],
                "description": s["description"],
                "body": s["full_text"][:8000],
                "group": [group_of[s["skill_id"]]],
                "covers": covers_of[s["skill_id"]],
            }, ensure_ascii=False) + "\n")

    # --- queries.jsonl ---
    n_ko = 0
    with open(OUT / "queries.jsonl", "w", encoding="utf-8") as f:
        for q in queries["queries"]:
            lang = "ko" if re.search(r"[가-힣]", q["query"]) else "en"
            n_ko += lang == "ko"
            f.write(json.dumps({
                "qid": q["query_id"],
                "query": q["query"],
                "gold": q["gold_skills"],
                "setting": q["setting"],
                "lang": lang,
            }, ensure_ascii=False) + "\n")
    print("queries: %d (ko=%d)" % (len(queries["queries"]), n_ko))

    # --- holon libraries ---
    # dir/name-safe form of skill_id (one id, "mission-control copy", has a space)
    dir_of = {}
    for s in skills:
        sid = s["skill_id"]
        d = re.sub(r"[^a-z0-9]+", "-", sid.lower()).strip("-")
        assert re.fullmatch(r"[a-z0-9][a-z0-9-]{0,62}[a-z0-9]", d), d
        assert d not in dir_of.values() or dir_of.get(sid) == d
        dir_of[sid] = d

    def yq(v):
        return holon._yaml_string(v)

    def clean_mid(text, budget):
        mid = re.sub(r"[:;]", ",", text).strip()
        mid = re.sub(r"\s+", " ", mid)
        if len(mid) > budget:
            mid = mid[:budget].rsplit(" ", 1)[0].rstrip(",. ")
        return mid

    def leaf_skillmd(s):
        sid = s["skill_id"]
        covers = covers_of[sid]
        suffix = ": covers " + ", ".join(covers)
        budget = 200 - len("Use when ") - len(suffix)
        desc = "Use when " + clean_mid(s["description"], max(budget, 20)) + suffix
        trig = [t.strip().replace("\n", " ") for t in (s.get("trigger_phrases") or [])][:2]
        lines = ["---", "name: %s" % yq(dir_of[sid]), "description: %s" % yq(desc)]
        if trig:
            lines += ["metadata:", "  holon-triggers: |"] + ["    " + t for t in trig]
        lines += ["---", "", s["full_text"][:2000], ""]
        return "\n".join(lines)

    def group_skillmd(gname, members_desc):
        gtoks = [t for t in re.split(r"[-_]+", gname.lower()) if t] or [gname]
        gtoks = [t if len(t) >= 3 else t for t in gtoks]
        desc = ("Use when the request concerns the %s category of skills: covers %s"
                % (gname, ", ".join(gtoks)))
        return "\n".join(["---", "name: %s" % yq(gname), "description: %s" % yq(desc), "---", "",
                          "Grouping node for the %d skills of the %s category. %s"
                          % (len(members_desc), gname, members_desc), ""])

    def root_skillmd(title):
        return "\n".join([
            "---", "name: %s" % yq(title),
            "description: %s" % yq("Root of the SkillRetBench routing library; pick the child whose cover words match the request."),
            "---", "",
            "Route each request to exactly one sub-skill. Report routing misses to _feedback.md.",
            ""])

    for lib, grouped in (("tree", True), ("flat", False)):
        root = OUT / lib
        if root.exists():
            import shutil
            shutil.rmtree(root)
        root.mkdir(parents=True)
        (root / "SKILL.md").write_text(root_skillmd("srb-%s" % lib), encoding="utf-8")
        (root / "_feedback.md").write_text("# routing misses\n", encoding="utf-8")
        if grouped:
            for g in groups:
                members = [sid for sid, gg in group_of.items() if gg == g]
                gdir = root / g
                gdir.mkdir()
                (gdir / "SKILL.md").write_text(group_skillmd(g, members_desc=""), encoding="utf-8")
                for s in skills:
                    if group_of[s["skill_id"]] == g:
                        d = gdir / dir_of[s["skill_id"]]
                        d.mkdir()
                        (d / "SKILL.md").write_text(leaf_skillmd(s), encoding="utf-8")
        else:
            for s in skills:
                d = root / dir_of[s["skill_id"]]
                d.mkdir()
                (d / "SKILL.md").write_text(leaf_skillmd(s), encoding="utf-8")

    # --- sync + validate ---
    for lib in ("tree", "flat"):
        root = str(OUT / lib)
        rc = holon.main(["sync", root])
        print("sync %s rc=%d" % (lib, rc))
        rc = holon.main(["validate", root])
        print("validate %s rc=%d" % (lib, rc))

    covers_dump = {sid: covers_of[sid] for sid in sorted(covers_of)}
    json.dump(covers_dump, open(OUT / "covers.json", "w"), indent=0, ensure_ascii=False)
    json.dump(dir_of, open(OUT / "dir_map.json", "w"), indent=0, ensure_ascii=False)
    print("done")


if __name__ == "__main__":
    main()
