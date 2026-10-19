---
name: paper-archive
description: "Use when Central catalog and knowledge hub for all paper-related activities. Manages a searchable JSON index of reviewed, discovered, and scouted: covers paper, archive, central, previously, reviewed"
metadata:
  holon-triggers: |
    archive a paper
    list archived papers
---

---
name: paper-archive
description: >-
  Central catalog and knowledge hub for all paper-related activities. Manages
  a searchable JSON index of reviewed, discovered, and scouted papers with
  deduplication, relationship tracking, and integrations into NotebookLM,
  Notion, and the recall memory system.
  Use when the user asks to "archive a paper", "list archived papers",
  "search papers", "check if paper is archived", "paper archive",
  "논문 아카이브", "논문 목록", "논문 검색", "아카이브된 논문",
  "paper library", "paper catalog", "show paper graph",
  "sync papers to NLM", "sync papers to Notion", "paper stats",
  "export paper archive", "/paper-archive", or any request to catalog,
  search, deduplicate, or browse previously reviewed papers.
  Do NOT use for reviewing a paper (use paper-review).
  Do NOT use for discovering related papers (use related-papers-scout).
  Do NOT use for quick paper overview (use alphaxiv-paper-lookup).
  Do NOT use for arXiv-to-slides (use nlm-arxiv-slides).
metadata:
  author: thaki
  version: 1.0.0
  category: research
---

# Paper Archive

Central catalog that indexes all papers across paper-review,
related-papers-scout, alphaxiv-paper-lookup, and nlm-arxiv-slides into a
single searchable JSON index with relationship tracking and external sync.

## Prerequisites

- `outputs/papers/` directory exists
- `notebooklm-mcp` MCP server authenticated (for `sync-nlm`)
- `plugin-notion-workspace-notion` MCP server connected (for `sync-notion`)
- Semantic Scholar API access (for metadata enrichment during `register`)

## Reference Files

Read these as needed during execution:

- `references/index-schema.md` — JSON schema, field types, validation rules
- `references/workflow-steps.md` — Per-command detailed instructions
- `references/integration-hooks.md` — How paper-review and related-papers-scout auto-register

## Index Location

`outputs/papers/index.json`

If the file does not exist, create it with the empty scaffold:

```json
{
  "version": "1.0.0",
  "
