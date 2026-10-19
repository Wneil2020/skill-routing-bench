---
name: md-to-notion
description: "Use when Publish local markdown files as Notion sub-pages under a specified parent page. Reads one file or globs a folder for *.md, extracts H1 as page: covers notion, 노션 업로드, 마크다운 노션, ascii, globs"
metadata:
  holon-triggers: |
    upload markdown to Notion
    publish md to Notion
---

---
name: md-to-notion
description: >-
  Publish local markdown files as Notion sub-pages under a specified parent page.
  Reads one file or globs a folder for *.md, extracts H1 as page title, converts
  pipe tables to Notion <table> HTML blocks for proper rendering, splits large
  documents (>15KB) into linked sub-pages, preserves ASCII diagrams in code blocks,
  and batch-creates pages via the Notion MCP. Use when the user asks to "upload
  markdown to Notion", "publish md to Notion", "push files to Notion", "마크다운
  노션 업로드", "md를 노션에 올려줘", "노션 페이지로 변환", "마크다운 노션
  퍼블리시", "md-to-notion", "노션에 올려", "노션 페이지 만들어", or wants to turn
  local markdown into structured Notion pages.
  Do NOT use for bidirectional Notion sync with YAML config (use notion-docs-sync).
  Do NOT use for meeting digest analysis and upload (use meeting-digest).
  Do NOT use for Notion database operations or page queries (use Notion MCP directly).
  Korean triggers: "노션 업로드", "마크다운 노션", "노션 페이지", "노션에 올려", "노션에 정리".
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "execution"
---
# md-to-notion

Lightweight one-shot publisher: point at local markdown files and a Notion
parent page, get structured sub-pages. Handles pipe-table conversion, large
document splitting, and ASCII art preservation automatically.

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `<path>` | Yes | File path or folder path containing `.md` files |
| `--parent <id>` | No | Notion parent page ID (32-char hex). Defaults to `3239eddc34e680e8a7a5d5b5eac18b38` (AI 자동 정리) |
| `--icon <emoji>` | No | Uniform emoji icon for all created pages (default: 📄) |
| `--skip-meta` | No | Skip README.md, CHANGELOG.md, LICENSE.md |
| `--no-table-convert` | No | Keep pipe tables as-is (skip conversion) |
| `--title-prefix <str>` | No | Prepend string to each page title |
| `--split-threshold <N>` | No | Character limit before auto-splitting (default: 15000) |
| `--dry-run` | No | List files and ti
