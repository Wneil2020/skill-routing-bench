---
name: nlm-slides
description: "Use when End-to-end pipeline that transforms a local markdown document into professional NotebookLM slide decks. Splits sections, rewrites each into: covers nlm, slides, rewrites, splits, sections"
metadata:
  holon-triggers: |
    create NLM slides
    NLM 슬라이드
---

---
name: nlm-slides
description: >-
  End-to-end pipeline that transforms a local markdown document into professional
  NotebookLM slide decks. Splits sections, rewrites each into expert-level EN + KO,
  uploads to NotebookLM, generates slide decks, and downloads PDFs.
  Use when the user asks to "create NLM slides", "NLM 슬라이드", "슬라이드 만들어",
  "generate slides from doc", "convert document to slides", or convert a local
  document into NotebookLM slide decks.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use notebooklm-studio.
  Do NOT use for video from local docs -- use nlm-video. Do NOT use for PowerPoint
  without NotebookLM -- use anthropic-pptx. Do NOT use for notebook CRUD -- use
  notebooklm.
metadata:
  author: thaki
  version: 1.1.0
  category: generation
---

# NLM Slides: Local Document to Expert Slide Deck Pipeline

End-to-end pipeline that transforms a local markdown document into professional NotebookLM slide decks in both English and Korean, written in domain-expert tone with white background styling.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- A local markdown file with `##` section headings
- Authentication often expires between sessions; if `notebook_create` fails with "Authentication expired", run `nlm login` in terminal, then call `refresh_auth` MCP tool before retrying

## System Prompt

The expert rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before starting the pipeline. It defines:

- Expert tone and domain authority for each language
- Presentation-friendly formatting rules
- White background tone directive
- Content density requirements

## Pipeline

### Step 1: Read the Local Markdown

Read the user-specified markdown file. Identify the document title (from `#` heading or filename).

### Step 2: Split by Sections

Split the markdown content at `##` heading boundaries. Each section becomes an independent unit fo
