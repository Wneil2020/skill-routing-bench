#!/usr/bin/env python3
"""Build ds/skillret: skills.jsonl, queries.jsonl, tree/, flat/ from data/skillret.

Cover-word rule (reproducible, deterministic):
  covers = name_words + top_idf_desc_words, total <= 5
  - name_words: skill name split on -/_ (and non-alnum), lowercased, len>=3, not stopword
  - desc words: tokens [a-z0-9._-]+ (len>=3, start with letter, not stopword) from the
    description; df over all skills' (name+description); idf=ln((N+1)/(df+1))+1;
    score=tf*idf; ties broken by (-score, word). Fill remaining slots up to 5 total.
  - group nodes (major/sub): covers = group name split on non-alnum, lowercased, len>=2.
"""
import json, math, os, re, sys, collections

BENCH = "/workspace/work/bench"
RAW = os.path.join(BENCH, "data/skillret/data")
OUT = os.path.join(BENCH, "ds/skillret")

STOP = set("""a an the and or of to in for on with by from at as is are was were be been being
this that these those it its you your we our they their he she his her not no nor but if then
than so such can could will would should may might must do does did done have has had having
use used using user users when what which who whom how why where all any each other more most
some own same only very just also into over under again further once here there about above
below between through during before after up down out off i me my mine ours theirs them him
""".split())

WORD_RE = re.compile(r"[a-z][a-z0-9._-]*")


def sanitize(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:64].strip("-") or "skill"


def tokens(text):
    return [t for t in WORD_RE.findall(text.lower())
            if len(t) >= 3 and t not in STOP and not t.isdigit()]


def name_words(name):
    out = []
    for w in re.split(r"[^a-z0-9]+", name.lower()):
        if len(w) >= 3 and w not in STOP and not w.isdigit() and w not in out:
            out.append(w)
    return out


def group_words(name):
    return [w for w in re.split(r"[^a-z0-9]+", name.lower()) if len(w) >= 2]


def main():
    skills = [json.loads(l) for l in open(os.path.join(RAW, "skills_test.jsonl"))]
    queries = [json.loads(l) for l in open(os.path.join(RAW, "queries/test.jsonl"))]
    gold = collections.defaultdict(list)
    for l in open(os.path.join(RAW, "qrels/test.jsonl")):
        d = json.loads(l)
        if d.get("relevance", 1) >= 1:
            gold[d["query_id"]].append(d["skill_id"])
    tax = json.load(open(os.path.join(RAW, "taxonomy.json")))["taxonomy"]
    sub_desc = {(m["major"], s["sub"]): s.get("sub_description", "") for m in tax for s in m["subs"]}
    maj_desc = {m["major"]: m.get("major_description", "") for m in tax}

    N = len(skills)
    df = collections.Counter()
    for s in skills:
        df.update(set(tokens(s["name"] + " " + s["description"])))
    idf = {w: math.log((N + 1) / (c + 1)) + 1 for w, c in df.items()}

    def covers_for(s):
        cov = name_words(s["name"])
        tf = collections.Counter(tokens(s["description"]))
        cand = sorted(((-tf[w] * idf[w], w) for w in tf if w not in cov))
        for _, w in cand:
            if len(cov) >= 5:
                break
            cov.append(w)
        return [w for w in cov if re.fullmatch(r"[a-z0-9._-]+", w)][:5]

    # unique dir names per parent
    used = collections.defaultdict(set)   # parent key -> used dir names
    def uniq(parent, base, sid):
        u = used[parent]
        d = base
        if d in u:
            d = (base[:55].strip("-") + "-" + sid[:8])
        u.add(d)
        return d

    maj_dir, sub_dir = {}, {}
    for m in tax:
        maj_dir[m["major"]] = uniq("", sanitize(m["major"]), m["major"])
        for s in m["subs"]:
            sub_dir[(m["major"], s["sub"])] = uniq(maj_dir[m["major"]], sanitize(s["sub"]), s["sub"])

    skills_out, tree_map = [], {}
    leaf_dir = {}
    for s in skills:
        pa = (maj_dir[s["major"]], sub_dir[(s["major"], s["sub"])])
        d = uniq("/".join(pa), sanitize(s["name"]), s["id"])
        leaf_dir[s["id"]] = d
        tree_map[s["id"]] = [maj_dir[s["major"]], sub_dir[(s["major"], s["sub"])], d]
        skills_out.append({
            "id": s["id"], "name": s["name"], "description": s["description"],
            "body": (s.get("body") or "")[:8000],
            "group": [s["major"], s["sub"]],
            "covers": covers_for(s),
        })

    with open(os.path.join(OUT, "skills.jsonl"), "w") as f:
        for s in skills_out:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    with open(os.path.join(OUT, "queries.jsonl"), "w") as f:
        for q in queries:
            f.write(json.dumps({"qid": q["id"], "query": q["query"],
                                "gold": gold.get(q["id"], []),
                                "setting": "all", "lang": "en"}, ensure_ascii=False) + "\n")
    json.dump(tree_map, open(os.path.join(OUT, "tree_map.json"), "w"), indent=0)

    covers_by_id = {s["id"]: s["covers"] for s in skills_out}

    def q(s):  # yaml-safe double-quoted scalar
        return json.dumps(s, ensure_ascii=False)

    def skill_md(name, desc, body, root=False, parent=False):
        fm = "---\nname: %s\ndescription: %s\n" % (q(name), q(desc))
        if root:
            fm += 'metadata:\n  holon-archive-count: "0"\n'
        fm += "---\n\n"
        text = fm + body.rstrip() + "\n"
        if parent or root:
            text += "\n<!-- sub-skills -->\n<!-- /sub-skills -->\n"
        return text

    raw = {s["id"]: s for s in skills}

    def leaf_desc(sid):
        r = raw[sid]
        desc = "Use when the task involves %s %s: covers %s" % (
            r.get("primary_action") or "handle", r.get("primary_object") or "tasks",
            ", ".join(covers_by_id[sid]))
        return desc[:200]

    def write_tree(base, flat=False):
        os.makedirs(base, exist_ok=True)
        root_desc = ("Use for every task: root of the skill tree; read the sub-skills list "
                     "and descend to the branch the task matches: covers skill, task, routing")
        with open(os.path.join(base, "SKILL.md"), "w") as f:
            f.write(skill_md("skillret-root", root_desc, "# skillret-root\n\nRoot of the skillret benchmark tree.", root=True))
        if flat:
            usedf = {}
            flat_map = {}
            for s in skills_out:
                base_d = leaf_dir[s["id"]]
                d = base_d
                if d in usedf:
                    d = (base_d[:55].strip("-") + "-" + s["id"][:8])
                usedf[d] = True
                flat_map[s["id"]] = d
                os.makedirs(os.path.join(base, d), exist_ok=True)
                with open(os.path.join(base, d, "SKILL.md"), "w") as f:
                    f.write(skill_md(d, leaf_desc(s["id"]), "# %s\n\n%s" % (d, s["description"][:300])))
            json.dump(flat_map, open(os.path.join(OUT, "flat_map.json"), "w"), indent=0)
            return
        for m in tax:
            md = maj_dir[m["major"]]
            os.makedirs(os.path.join(base, md), exist_ok=True)
            desc = "Use when the task involves %s: covers %s" % (m["major"], ", ".join(group_words(m["major"])))
            with open(os.path.join(base, md, "SKILL.md"), "w") as f:
                f.write(skill_md(md, desc, "# %s\n\n%s" % (m["major"], maj_desc[m["major"]][:300]), parent=True))
            for sb in m["subs"]:
                sdp = sub_dir[(m["major"], sb["sub"])]
                os.makedirs(os.path.join(base, md, sdp), exist_ok=True)
                desc = "Use when the task involves %s: covers %s" % (sb["sub"], ", ".join(group_words(sb["sub"])))
                with open(os.path.join(base, md, sdp, "SKILL.md"), "w") as f:
                    f.write(skill_md(sdp, desc, "# %s\n\n%s" % (sb["sub"], sub_desc[(m["major"], sb["sub"])][:300]), parent=True))
        for s in skills_out:
            maj, sub, d = tree_map[s["id"]]
            p = os.path.join(base, maj, sub, d)
            os.makedirs(p, exist_ok=True)
            with open(os.path.join(p, "SKILL.md"), "w") as f:
                f.write(skill_md(d, leaf_desc(s["id"]), "# %s\n\n%s" % (d, s["description"][:300])))

    write_tree(os.path.join(OUT, "tree"))
    # flat needs its own covers in desc; rebuild desc there the same way
    write_tree(os.path.join(OUT, "flat"), flat=True)
    print("built: %d skills, %d queries" % (len(skills_out), len(queries)))

if __name__ == "__main__":
    main()
