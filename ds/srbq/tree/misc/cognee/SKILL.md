---
name: cognee
description: "Use when Build persistent AI memory and knowledge graphs from documents using the cognee knowledge engine (CLI + Python API). Ingest text, PDF, DOCX: covers cognee, 지식 그래프, AI 메모리, cognify, enhanced"
metadata:
  holon-triggers: |
    build knowledge graph
    create AI memory
---

---
name: cognee
description: >-
  Build persistent AI memory and knowledge graphs from documents using the
  cognee knowledge engine (CLI + Python API). Ingest text, PDF, DOCX, CSV,
  images, and audio; extract entities and relationships; search with
  graph-enhanced RAG. Use when the user asks to "build knowledge graph",
  "create AI memory", "semantic search over documents", "cognee add",
  "cognee cognify", "cognee search", "ingest documents", "index documents
  for RAG", or wants to convert documents into a searchable knowledge base.
  Do NOT use for general web search (use WebSearch).
  Do NOT use for stock-specific data pipelines (use today).
  Do NOT use for paper review (use paper-review).
  Do NOT use for general web scraping (use scrapling or defuddle).
  Korean triggers: "지식 그래프", "AI 메모리", "시맨틱 검색", "문서 인덱싱",
  "cognee", "지식 엔진".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---

# Cognee — Knowledge Engine

Build persistent, learnable AI memory from diverse data sources. Cognee combines vector search + graph DB + cognitive science to create knowledge graphs that enable semantic search, entity-relationship extraction, and agent memory.

## Prerequisites

1. **Python 3.10+** required
2. **Install cognee**:

```bash
pip install cognee
# or with uv
uv pip install cognee
```

3. **Set environment variables** (minimal):

```bash
export LLM_API_KEY="your-openai-api-key"  # pragma: allowlist secret
export LLM_MODEL="openai/gpt-4o-mini"
export LLM_PROVIDER="openai"
```

See [references/configuration.md](references/configuration.md) for the full env var registry and [references/api-reference.md](references/api-reference.md) for detailed Python/REST API documentation.

4. **Optional extras** — install only what you need:

| Extra | Command | Purpose |
|-------|---------|---------|
| `postgres` | `pip install cognee[postgres]` | PostgreSQL + pgvector backend |
| `neo4j` | `pip install cognee[neo4j]` | Neo4j graph database |
| `anthropic` |
