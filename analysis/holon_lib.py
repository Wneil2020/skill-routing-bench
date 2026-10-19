#!/usr/bin/env python3
"""Shared deterministic helpers for the holon failure analysis.

Only local files are read. The holon source is imported, not modified.
"""
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BENCH = Path("/workspace/work/bench")
HOLON_REPO = Path("/workspace/work/holon-debate/repo/holon")
sys.path.insert(0, str(HOLON_REPO / "organizer" / "scripts"))
sys.path.insert(0, str(HOLON_REPO / "scripts"))
import organizer_cli as oc  # noqa: E402

WORD_RE = re.compile(r"[a-z0-9]+|[가-힣]+")
STOP = set("""
a an and are as at be been by for from has have how i in into is it its of on or
so that the their them they this to use used using was we what when which will
with you your task skill agent agents workflow workflows process processes
the do does can could should would please help want need
""".split())

# Deliberately small, hand-written synonym groups.  Kept transparent so the
# experiment is reproducible and its optimism is easy to judge.
SYN_GROUPS = [
    ["create", "make", "build", "generate", "produce", "craft", "develop"],
    ["find", "search", "lookup", "locate", "retrieve", "discover"],
    ["analyze", "analyse", "analysis", "analytics", "evaluate", "assess", "review", "audit", "check"],
    ["summarize", "summarise", "summary", "digest", "brief"],
    ["email", "mail", "gmail", "outlook", "inbox"],
    ["calendar", "schedule", "meeting", "event", "appointment"],
    ["weather", "forecast", "climate", "temperature"],
    ["translate", "translation", "convert", "conversion"],
    ["image", "photo", "picture", "visual", "graphic"],
    ["code", "coding", "program", "programming", "software"],
    ["test", "testing", "qa", "validation", "verify"],
    ["data", "dataset", "database"],
    ["report", "reporting", "dashboard"],
    ["security", "secure", "safety"],
    ["finance", "financial", "money", "budget", "accounting"],
    ["customer", "support", "service", "helpdesk"],
    ["document", "docs", "documentation", "readme"],
    ["video", "movie", "film"],
    ["music", "song", "audio"],
    ["travel", "trip", "flight", "hotel"],
    ["health", "medical", "medicine", "doctor"],
    ["legal", "law", "regulation"],
    ["plan", "planning", "roadmap", "strategy"],
    ["optimize", "optimise", "improve", "enhance", "boost"],
    ["automate", "automation", "automatic", "auto"],
    ["monitor", "monitoring", "track", "tracking"],
    ["manage", "management", "organize", "orchestrate", "coordinate"],
    ["write", "writing", "writer", "author"],
    ["design", "designer", "designing"],
    ["researcher", "research", "investigate", "investigation"],
]
SYN_CANON = {}
for group in SYN_GROUPS:
    canon = group[0]
    for w in group:
        SYN_CANON[w] = canon

STEM_EXCEPTIONS = {
    "analysis": "analyz", "analyses": "analyz", "analyze": "analyz", "analyzing": "analyz",
    "analytics": "analyz", "analytical": "analyz",
    "strategy": "strateg", "strategic": "strateg", "strategies": "strateg",
    "research": "research", "researcher": "research", "researchers": "research",
    "email": "email", "emails": "email",
    "news": "news", "business": "business", "businesses": "business",
    "class": "class", "classes": "class", "access": "access",
}


def stem(t):
    """Conservative suffix stripper; stem() is applied to both query and cover words."""
    if t in STEM_EXCEPTIONS:
        return STEM_EXCEPTIONS[t]
    if not re.fullmatch(r"[a-z]+", t) or len(t) <= 3:
        return t
    s = t
    if s.endswith("ization"):
        s = s[:-7] + "ize"
    elif s.endswith("isation"):
        s = s[:-7] + "ise"
    if s.endswith("ation"):
        s = s[:-5] + "ate"
    elif s.endswith("tion") and len(s) > 5:
        s = s[:-4] + "t"
    if s.endswith("ment") and len(s) > 6:
        s = s[:-4]
    if s.endswith("ness") and len(s) > 6:
        s = s[:-4]
    if s.endswith("ity") and len(s) > 5:
        s = s[:-3]
    if s.endswith("ies") and len(s) > 5:
        s = s[:-3] + "y"
    elif s.endswith("es") and len(s) > 5:
        s = s[:-2]
    elif s.endswith("s") and not s.endswith("ss") and len(s) > 4:
        s = s[:-1]
    for suf in ("ing", "ed", "er", "ly"):
        if s.endswith(suf) and len(s) > len(suf) + 3:
            s = s[:-len(suf)]
            break
    if s.endswith("e") and len(s) > 4:
        s = s[:-1]
    return s or t


def norm_tokens(text, use_stem=False, use_syn=False):
    toks = WORD_RE.findall(text.lower())
    out = []
    for t in toks:
        if use_syn:
            t = SYN_CANON.get(t, t)
        if use_stem:
            t = stem(t)
        out.append(t)
    return out


def norm_text(text, use_stem=False, use_syn=False):
    return " ".join(norm_tokens(text, use_stem, use_syn))


def cover_in_text(cover, text):
    """Same convention as holon.contains: ASCII phrase with word boundaries,
    other scripts as a substring.  Both sides are expected to be lower-cased."""
    if not cover:
        return False
    if re.fullmatch(r"[a-z0-9_.\- ]+", cover):
        pat = r"(?<![a-z0-9_])" + re.escape(cover) + r"(?![a-z0-9_])"
        return re.search(pat, text) is not None
    return cover in text


def rel(root, p):
    return p.relative_to(root).as_posix() if p != root else "."


def path_nodes(rel_path):
    return [x for x in rel_path.split("/") if x]


def load_dataset(ds):
    base = BENCH / "ds" / ds
    queries = [json.loads(l) for l in open(base / "queries.jsonl", encoding="utf-8")]
    qmap = {q["qid"]: q for q in queries}
    index = json.load(open(base / "tree_index.json", encoding="utf-8"))
    rel2id = dict(index)
    id2rel = {v: k for k, v in index.items()}
    root = base / "tree"
    skills, errors = oc.find_skills(root)
    syn = oc.load_synonyms(root)
    return {
        "ds": ds, "base": base, "root": root, "queries": queries, "qmap": qmap,
        "rel2id": rel2id, "id2rel": id2rel, "skills": skills, "errors": errors, "syn": syn,
    }


class NormalRouter:
    """A re-implementation of holon's descent with optional stemming/synonyms and
    an optional IDF tie-break instead of stopping on ambiguity."""

    def __init__(self, data, use_stem=False, use_syn=False):
        self.d = data
        self.root = data["root"]
        self.skills = data["skills"]
        self.use_stem = use_stem
        self.use_syn = use_syn
        self.children = {}
        for k in sorted(self.skills):
            self.children.setdefault(k.parent, []).append(k)
        self.own = {}
        self.excl = {}
        self.covers_below = {}
        self._norm_cache = {}
        for k in sorted(self.skills):
            c, e = oc.parse_desc(self.skills[k].meta.get("description", ""))
            self.own[k] = sorted(c, key=str.lower)
            self.excl[k] = sorted(e, key=str.lower)
        for k in sorted(self.skills):
            words = list(self.own[k])
            for p in k.parents:
                self.covers_below.setdefault(p, []).extend((w, k) for w in self.own[k])
        # leaf cover df / idf, over leaves only, deduplicated per leaf
        leaf_docs = []
        for k in sorted(self.skills):
            if not self.children.get(k):
                leaf_docs.append({self.norm(w) for w in self.own[k]})
        n = len(leaf_docs)
        df = Counter()
        for doc in leaf_docs:
            for w in doc:
                df[w] += 1
        self.idf = {w: math.log((n + 1) / (c + 1)) + 1 for w, c in df.items()}
        self.default_idf = math.log(n + 1) + 1

    def norm(self, w):
        key = w
        if key not in self._norm_cache:
            self._norm_cache[key] = norm_text(w, self.use_stem, self.use_syn)
        return self._norm_cache[key]

    def hit(self, text, cover):
        return cover_in_text(self.norm(cover), text)

    def own_hit(self, d, text):
        return [w for w in self.own[d] if self.hit(text, w)]

    def excl_hit(self, d, text):
        return [w for w in self.excl[d] if self.hit(text, w)]

    def node_match(self, d, text):
        return bool(self.own_hit(d, text)) and not self.excl_hit(d, text)

    def match_skill(self, d, text):
        if self.node_match(d, text):
            return True
        if self.excl_hit(d, text):
            return False
        return any(self.hit(text, w) for w, _ in self.covers_below.get(d, ()))

    def hits_under(self, cur, text):
        return [k for k in self.children.get(cur, []) if self.match_skill(k, text)]

    def matched_words(self, d, text):
        out = set()
        for w in self.own[d]:
            if self.hit(text, w):
                out.add(self.norm(w))
        for w, _ in self.covers_below.get(d, ()):
            if self.hit(text, w):
                out.add(self.norm(w))
        return out

    def score(self, d, text):
        words = self.matched_words(d, text)
        return sum(self.idf.get(w, self.default_idf) for w in words), len(words)

    def route_strict(self, query):
        text = norm_text(query, self.use_stem, self.use_syn)
        cur, path = self.root, [self.root]
        while True:
            hits = self.hits_under(cur, text)
            if len(hits) == 1:
                cur = hits[0]
                path.append(cur)
            elif len(hits) > 1 and cur == self.root:
                return path + [("AMBIG", hits)]
            else:
                return path

    def route_score(self, query):
        text = norm_text(query, self.use_stem, self.use_syn)
        cur, path = self.root, [self.root]
        while True:
            kids = self.children.get(cur, [])
            if not kids:
                return path
            scored = [(self.score(k, text), k) for k in kids]
            scored = [(s, k) for s, k in scored if s[1] > 0]
            if not scored:
                return path
            scored.sort(key=lambda sk: (-sk[0][0], -sk[0][1], rel(self.root, sk[1])))
            cur = scored[0][1]
            path.append(cur)

    def rank_leaves(self, query, k=20):
        text = norm_text(query, self.use_stem, self.use_syn)
        scored = []
        for d in self.skills:
            if self.children.get(d):
                continue
            s, n = self.score(d, text)
            if n:
                scored.append((s, n, rel(self.root, d), d))
        scored.sort(key=lambda x: (-x[0], -x[1], x[2]))
        return scored[:k]


def classify_route(data, path):
    """Turn a holon path into one of the mutually exclusive failure classes."""
    root = data["root"]
    skills = data["skills"]
    rel2id = data["rel2id"]
    last = path[-1]
    if isinstance(last, tuple):
        return "ambiguous_root", [rel(root, x) for x in last[1]]
    if last == root:
        return "no_match_root", []
    r = rel(root, last)
    if r in rel2id:
        return "leaf", [r]
    # non-leaf: distinguish zero-hit stop from multiple-hit stop
    text = None
    return "stop_group", [r]


def parent_rel(rel_path):
    parts = path_nodes(rel_path)
    return "/".join(parts[:-1]) if len(parts) > 1 else "."


def gold_paths(data, gold):
    out = []
    for sid in gold:
        r = data["id2rel"].get(sid)
        if r is not None:
            out.append((sid, r))
    return out
