---
name: notebooklm-studio
description: "Use when Generate content from Google NotebookLM notebooks -- audio podcasts, video explainers, reports, quizzes, flashcards, mind maps: covers notebooklm, studio, podcasts, explainers, infographics"
metadata:
  holon-triggers: |
    create a podcast
    make a video
---

---
name: notebooklm-studio
description: >-
  Generate content from Google NotebookLM notebooks -- audio podcasts, video
  explainers, reports, quizzes, flashcards, mind maps, slide decks, infographics,
  and data tables. Download artifacts and export to Google Docs/Sheets.
  Use when the user asks to "create a podcast", "make a video", "create flashcards",
  "generate a report", "make a slide deck", "generate mind map", "generate quiz",
  "download artifact", "export to Google Docs", "NLM studio", "팟캐스트 생성",
  or any NotebookLM content generation request.
  Do NOT use for notebook/source/note CRUD -- use notebooklm. Do NOT use for
  web/Drive research -- use notebooklm-research. Do NOT use for end-to-end slide
  pipelines from local docs -- use nlm-slides. Do NOT use for end-to-end video
  pipelines from local docs -- use nlm-video. Do NOT use for local transcription --
  use transcribee.
metadata:
  author: thaki
  version: 1.0.0
  category: generation
---

# NotebookLM Studio: Content Generation

Generate rich content from Google NotebookLM notebooks -- podcasts, videos, reports, study materials, presentations, and infographics. Download and export artifacts via the `notebooklm-mcp` MCP server.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- A notebook with at least one processed source (required for content generation)

## Available Tools

### Studio Content (4 tools)

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `studio_create` | Create any artifact type | `notebook_id`, `artifact_type`, `confirm=True`, type-specific params |
| `studio_status` | Check generation progress | `notebook_id` |
| `studio_delete` | Delete an artifact | `notebook_id`, `artifact_id`, `confirm=True` |
| `studio_revise` | Revise slides in existing deck | `notebook_id`, `artifact_id`, `instructions`, `confirm=True` |

### Download & Export (2 tools)

| Tool | Description | Key Parameters |
|------
