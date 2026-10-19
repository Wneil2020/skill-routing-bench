#!/usr/bin/env python3
"""Build holon tree/ and flat/ libraries for ds/toolret.

Grouping: tool docs carry no category field and ids carry no namespace, so we
cluster BM25 term-score vectors of name+description with KMeans(k=round(sqrt(N)),
seed=0). Cover words: tool name split on -/_/camelCase, then top-IDF description
tokens, k<=5 total. Group names = top-2 tfidf tokens of the cluster; group cover
words = group name tokens.
"""
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans

BASE = Path("/workspace/work/bench/ds/toolret")
TREE = BASE / "tree"
FLAT = BASE / "flat"

STOP = set("""a an the and or of to in for on with by is are be this that it as at from into your you we i
use used using useful when want can will should would could get give make take find return returns
tool input output string should represent represents representing data information via based via per
any all each one two more other own like e.g etc""".split())

WORD_RE = re.compile(r"[a-z][a-z0-9]+")


def camel_split(s):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    return re.split(r"[^A-Za-z0-9]+", s)


def slugify(name, used):
    toks = [t.lower() for t in camel_split(name) if t]
    slug = "-".join(toks) or "tool"
    slug = re.sub(r"[^a-z0-9-]", "", slug).strip("-") or "tool"
    base, n = slug, 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def tokens(text):
    return [t for t in WORD_RE.findall(text.lower()) if t not in STOP and len(t) >= 2]


skills = [json.loads(l) for l in (BASE / "skills.jsonl").open()]
for s in skills:
    s["name_tokens"] = [t.lower() for t in camel_split(s["name"]) if len(t) >= 2 and t.lower() not in STOP]

corpus = [s["name"] + " " + s["description"] for s in skills]
doc_tokens = [tokens(c) for c in corpus]
N = len(skills)
df = Counter()
for ts in doc_tokens:
    for t in set(ts):
        df[t] += 1
idf = {t: math.log(1 + N / (1 + df[t])) for t in df}

# BM25 term-score matrix for KMeans grouping
k1, b = 1.5, 0.75
avgdl = sum(len(ts) for ts in doc_tokens) / N
vocab = sorted(idf)
vidx = {t: i for i, t in enumerate(vocab)}
X = np.zeros((N, len(vocab)))
for di, ts in enumerate(doc_tokens):
    tf = Counter(ts)
    dl = len(ts) or 1
    for t, f in tf.items():
        X[di, vidx[t]] = idf[t] * f * (k1 + 1) / (f + k1 * (1 - b + b * dl / avgdl))
norm = np.linalg.norm(X, axis=1, keepdims=True)
Xn = X / np.where(norm == 0, 1, norm)

k = max(2, round(math.sqrt(N)))
km = KMeans(n_clusters=k, random_state=0, n_init=10).fit(Xn)
labels = km.labels_

# group names: top-2 tokens by summed bm25 within cluster
clusters = defaultdict(list)
for s, lb in zip(skills, labels):
    clusters[lb].append(s)
used_groups = set()
group_of = {}
# group names: cover tokens distinctive to the cluster (in-cluster count minus
# count among members of other clusters)
cover_of = {}
for s in skills:
    cover_of[s["id"]] = [t for t in s["name_tokens"]]
in_count, out_count = {}, Counter()
all_covers = Counter()
for s in skills:
    for t in set(cover_of[s["id"]]):
        all_covers[t] += 1
for lb, members in sorted(clusters.items()):
    inc = Counter()
    for s in members:
        for t in set(cover_of[s["id"]]):
            inc[t] += 1
    distinctive = {t: inc[t] - (all_covers[t] - inc[t]) for t in inc}
    top = [t for t, _ in sorted(distinctive.items(), key=lambda kv: (-kv[1], kv[0]))[:2]]
    in_count[lb] = inc
    gname = "-".join(top)
    base, n = gname, 2
    while gname in used_groups:
        gname = f"{base}-{n}"
        n += 1
    used_groups.add(gname)
    for s in members:
        group_of[s["id"]] = (gname, top)

used_slugs = set()
for s in skills:
    s["slug"] = slugify(s["name"], used_slugs)

# cover words per skill: name tokens first, then top-idf desc tokens, <=5
for s in skills:
    covers = []
    for t in s["name_tokens"]:
        if t not in covers:
            covers.append(t)
    desc_score = sorted(set(tokens(s["description"])), key=lambda t: -idf.get(t, 0))
    for t in desc_score:
        if len(covers) >= 5:
            break
        if t not in covers:
            covers.append(t)
    s["covers"] = covers[:5]


def first_sentence(desc, limit):
    m = re.split(r"(?<=[.!?])\s", desc.strip(), maxsplit=1)
    sent = m[0].rstrip(".")
    return sent[:limit].rstrip(" ,;:")


def make_desc(prefix, covers):
    cov = ", ".join(covers)
    head = f"Use when {prefix}: covers {cov}"
    if len(head) <= 200:
        return head
    room = 200 - len(f"Use when : covers {cov}")
    return f"Use when {first_sentence(prefix, max(room, 10))}: covers {cov}"[:200]


def write_skill(d, name, desc, body):
    d.mkdir(parents=True, exist_ok=True)
    body = body.replace("<!--", "<!-").replace("-->", "->")
    qdesc = desc.replace("\\", "\\\\").replace('"', '\\"')
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: \"{qdesc}\"\n---\n\n{body}\n\n"
        f"<!-- sub-skills -->\n<!-- /sub-skills -->\n",
        encoding="utf-8")


def leaf_body(s):
    return s["body"]


root_desc = "Use when a task needs one of the tools in this library: covers tool, api"

for rootdir, grouped in ((TREE, True), (FLAT, False)):
    write_skill(rootdir, "toolret-root" if False else rootdir.name, root_desc,
                "ToolRet metatool tool library. Route to the tool whose cover words match the task.")
    if grouped:
        for lb, members in sorted(clusters.items()):
            gname, top = group_of[members[0]["id"]]
            write_skill(rootdir / gname, gname,
                        make_desc(f"the task involves {gname.replace('-', ' ')}", top),
                        f"Group of tools related to {gname.replace('-', ' ')}.")
            for s in members:
                write_skill(rootdir / gname / s["slug"], s["slug"],
                            make_desc(first_sentence(s["description"], 120), s["covers"]),
                            leaf_body(s))
    else:
        for s in skills:
            write_skill(rootdir / s["slug"], s["slug"],
                        make_desc(first_sentence(s["description"], 120), s["covers"]),
                        leaf_body(s))

# id <-> slug map
with (BASE / "slug_map.json").open("w") as f:
    json.dump({s["id"]: {"slug": s["slug"], "group": group_of[s["id"]][0],
                         "name": s["name"], "covers": s["covers"]} for s in skills}, f, indent=1)
print(f"tree: {k} groups, {N} leaves; flat: {N} leaves")
