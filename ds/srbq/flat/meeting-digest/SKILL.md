---
name: meeting-digest
description: "Use when Analyze any meeting content (Notion page, raw transcript, or local file) with multi-perspective PM sub-skills and produce structured Korean: covers meeting, digest, basic, parent, under"
metadata:
  holon-triggers: |
    digest a meeting
    meeting digest
---

---
name: meeting-digest
description: >-
  Analyze any meeting content (Notion page, raw transcript, or local file) with
  multi-perspective PM sub-skills and produce structured Korean summaries with
  detailed action items. Always uploads results to Notion as two sub-pages
  (summary + action items) under the default meeting parent page. Optionally
  generates PPTX and Slack posts. Use when the user asks to "digest a meeting",
  "meeting digest", "analyze meeting", "summarize meeting from Notion",
  "회의 분석", "회의 다이제스트", "미팅 요약", "미팅 분석", "회의록 분석",
  "회의 정리", "meeting analysis", "analyze this transcript", "meeting action
  items", "회의 액션 아이템", or shares a Notion meeting page URL for analysis.
  Do NOT use for batch-syncing a Notion meeting database (use notion-meeting-sync).
  Do NOT use for basic meeting transcript-to-notes without PM analysis,
  simple meeting notes, "메모만 정리", "간단 정리", or "요약만" requests (use
  pm-execution summarize-meeting).
  Do NOT use for syncing markdown docs to Notion (use notion-docs-sync).
  Do NOT use for ad-hoc PPTX creation without meeting content (use anthropic-pptx).
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "execution"
---
# Meeting Digest

Single-meeting orchestrator that accepts flexible input (Notion page, raw
transcript, or local file), runs multi-perspective PM analysis with meeting-type
detection, and produces structured Korean summaries with detailed action items.

## Configuration

| Key | Value |
|-----|-------|
| Output Directory | `output/meetings/` |
| Language | Korean |
| MCP Server (Notion) | `plugin-notion-workspace-notion` |
| MCP Server (Slack) | `plugin-slack-slack` |
| Default Slack Channel | `#ai-platform-chapter-기획` (ID: `C0AL6D32Z7W`) |
| Default Notion Parent | `3239eddc34e680e8a7a5d5b5eac18b38` (meetings) |
| Table Conversion Script | `.cursor/skills/md-to-notion/scripts/convert_tables.py` |

## Input Modes

| Mode | Detection | Handling |
|------|-----------|----------|
| **Notion URL/ID** |
