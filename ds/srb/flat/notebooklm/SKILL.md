---
name: notebooklm
description: "Use when Manage Google NotebookLM notebooks, sources, notes, queries, and sharing via the notebooklm-mcp MCP server. Use when the user asks: covers notebooklm, infographics, rename, flashcards, mind"
metadata:
  holon-triggers: |
    list notebooks
    create a notebook
---

---
name: notebooklm
description: >-
  Manage Google NotebookLM notebooks, sources, notes, queries, and sharing via
  the notebooklm-mcp MCP server. Use when the user asks to "list notebooks",
  "create a notebook", "add a source", "add URL to notebook", "query notebook",
  "ask notebook", "share notebook", "manage notes", "delete notebook",
  "rename notebook", "sync Drive sources", "get source content",
  "노트북LM", "노트북 생성", "노트북 목록", "소스 추가", "노트북 공유",
  "노트북 질문", "노트북 삭제", "노트 관리", "NLM 노트북",
  "NotebookLM", "NLM", "nlm notebook", "notebook source", "nlm query",
  or any notebook/source/note CRUD operation.
  Do NOT use for content generation (audio, video, reports, quizzes, slides,
  flashcards, mind maps, infographics, data tables) -- use notebooklm-studio.
  Do NOT use for web/Drive research pipelines -- use notebooklm-research.
  Do NOT use for general web search -- use parallel-web-search.
metadata:
  author: thaki
  version: 1.0.0
  category: integration
---

# NotebookLM: Core Notebook Management

Manage Google NotebookLM notebooks, sources, notes, queries, and sharing through the `notebooklm-mcp` MCP server (29 tools total; this skill covers 20 core tools).

## Prerequisites

The `notebooklm-mcp` MCP server must be registered in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "notebooklm-mcp": {
      "command": "notebooklm-mcp"
    }
  }
}
```

Authentication is required before first use:

```bash
nlm login          # launches browser for Google cookie extraction
nlm login --check  # verify auth status
```

Cookies persist for 2-4 weeks. The server auto-refreshes CSRF tokens on failure.

## Available Tools

### Notebooks (6 tools)

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `notebook_list` | List all notebooks | -- |
| `notebook_create` | Create a new notebook | `title` (required) |
| `notebook_get` | Get notebook details with sources | `notebook_id` (required) |
| `notebook_describe` | Get AI summary and sug
