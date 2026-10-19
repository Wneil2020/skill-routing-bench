---
name: nlm-video
description: "Use when End-to-end pipeline that transforms a local markdown document into professional NotebookLM video explainers. Splits sections, rewrites into: covers nlm, video, mp4, narration, explainers"
metadata:
  holon-triggers: |
    create NLM video
    NLM 비디오
---

---
name: nlm-video
description: >-
  End-to-end pipeline that transforms a local markdown document into professional
  NotebookLM video explainers. Splits sections, rewrites into expert-level EN + KO
  narration, uploads to NotebookLM, generates videos, and downloads MP4 files.
  Use when the user asks to "create NLM video", "NLM 비디오", "비디오 만들어",
  "generate video from doc", "convert document to video", or convert a local
  document into NotebookLM videos.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use notebooklm-studio.
  Do NOT use for slides from local docs -- use nlm-slides. Do NOT use for local
  video transcription -- use transcribee. Do NOT use for notebook CRUD -- use
  notebooklm.
metadata:
  author: thaki
  version: 1.1.0
  category: generation
---

# NLM Video: Local Document to Expert Video Pipeline

End-to-end pipeline that transforms a local markdown document into professional NotebookLM video explainers in both English and Korean, written in domain-expert narrative tone with white background styling.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- A local markdown file with `##` section headings
- Authentication often expires between sessions; if `notebook_create` fails with "Authentication expired", run `nlm login` in terminal, then call `refresh_auth` MCP tool before retrying

## System Prompt

The expert rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before starting the pipeline. It defines:

- Expert narrative tone optimized for spoken delivery
- Transition cues and flow structure
- White background tone directive
- Content density and pacing requirements

## Pipeline

### Step 1: Read the Local Markdown

Read the user-specified markdown file. Identify the document title (from `#` heading or filename).

### Step 2: Split by Sections

Split the markdown content at `##` heading boundaries. Each section becomes an independ
