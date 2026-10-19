---
name: notebooklm-research
description: "Use when Run web and Google Drive research through NotebookLM -- start research queries, poll progress, and import discovered sources into: covers notebooklm, research, poll, discovered, querying"
metadata:
  holon-triggers: |
    research a topic in NotebookLM
    start NLM research
---

---
name: notebooklm-research
description: >-
  Run web and Google Drive research through NotebookLM -- start research queries,
  poll progress, and import discovered sources into notebooks.
  Use when the user asks to "research a topic in NotebookLM", "start NLM research",
  "web research and import sources", "Drive research", "deep research in NLM",
  "find sources for notebook", "discover sources", "import research sources",
  "research and build notebook", "NLM deep research", "poll research status",
  "NLM 리서치", "노트북LM 연구", "웹 리서치 시작", "소스 탐색",
  "리서치 시작", "딥 리서치", "드라이브 검색", "소스 발견",
  "NLM 웹 리서치", "리서치 결과 가져오기",
  or any NotebookLM research/discovery workflow.
  Do NOT use for notebook/source/note CRUD or querying -- use notebooklm.
  Do NOT use for content generation (audio, video, reports) -- use notebooklm-studio.
  Do NOT use for general web search without NotebookLM -- use parallel-web-search.
  Do NOT use for finance-specific web search -- use alphaear-search.
metadata:
  author: thaki
  version: 1.0.0
  category: research
---

# NotebookLM Research: Web & Drive Discovery

Run research queries through Google NotebookLM to discover relevant sources from the web or Google Drive, then import them into notebooks. Uses the `notebooklm-mcp` MCP server.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- A target notebook to import discovered sources into

## Available Tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `research_start` | Start web or Drive research | `notebook_id`, `query`, `mode` (web/drive/deep) |
| `research_status` | Poll research progress | `notebook_id`, `task_id`, `max_wait` |
| `research_import` | Import discovered sources | `notebook_id`, `task_id`, `source_ids` (optional) |

## Workflow

### Standard research pipeline

1. **Start research:**

   ```
   research_start(notebook_id, query="semiconductor supply chain trends 2026", mode="web")
   ``
