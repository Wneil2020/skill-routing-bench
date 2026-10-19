---
name: recall
description: "Use when Restore cross-session context from the project's long-term memory store. Searches extracted session transcripts, decisions, patterns, and glossary: covers recall, bm25, hybrid, prime, prior"
metadata:
  holon-triggers: |
    recall
    what did we work on
---

---
name: recall
description: >-
  Restore cross-session context from the project's long-term memory store.
  Searches extracted session transcripts, decisions, patterns, and glossary
  using BM25, semantic, or hybrid search. Use when the user says "recall", "what
  did we work on", "load context about", "remember when we", "prime context",
  "yesterday's session", "restore context", "이전 작업", "맥락 복원", "recall topic",
  "recall yesterday", "what was the decision about", "이전에 뭐 했지", "컨텍스트 복원", "지난
  세션", or needs to resume prior work. Do NOT use for general web search (use
  WebSearch), code search in the current codebase (use Grep/SemanticSearch), or
  creating new memory entries (update MEMORY.md directly).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Recall: Long-Term Memory Search

Restore context from prior sessions, decisions, and patterns stored in the project's `memory/` directory.

## Prerequisite

Before first use, ensure sessions have been extracted:

```bash
python scripts/memory/extract-sessions.py --verbose
python scripts/memory/build-index.py --skip-embeddings
```

## Query Routing

Classify the user's request into one of three modes:

### 1. Temporal Mode

**Triggers**: date references — "yesterday", "last week", "March 5", "오늘", "어제", "지난주"

```bash
python scripts/memory/search.py --mode temporal --date "yesterday" --top 10 --verbose
python scripts/memory/search.py --mode temporal --date "2026-03-05" --days 3 --top 10 --verbose
```

### 2. Topic Mode

**Triggers**: conceptual queries — "trading agent design", "CI/CD setup", "stock analysis", any topic name

Use BM25 first (fast). If results are insufficient (<3 results or low relevance), escalate to hybrid.

**Query expansion**: Before searching, generate 2-3 synonyms or related terms for the user's query. Run parallel BM25 searches for each variant and merge results.

```bash
# Fast BM25 search
python scripts/memory/search.py --mode bm25 "trading agent guard pipeline" 
