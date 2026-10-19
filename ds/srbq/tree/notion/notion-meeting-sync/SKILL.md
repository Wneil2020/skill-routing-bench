---
name: notion-meeting-sync
description: "Use when Sync meeting notes from a Notion database, analyze with PM skills, generate comprehensive Korean summaries with detailed action items: covers notion, meeting, sync, summarizing, powerpoint"
metadata:
  holon-triggers: |
    sync meetings from Notion
    notion meeting sync
---

---
name: notion-meeting-sync
description: >-
  Sync meeting notes from a Notion database, analyze with PM skills, generate
  comprehensive Korean summaries with detailed action items, produce a
  PowerPoint deck, and post the final digest to Slack. Use when the user asks
  to "sync meetings from Notion", "notion meeting sync", "회의록 동기화",
  "회의 요약", "노션 회의록", "meeting digest", "meeting to PPTX",
  "meeting summary from Notion", "노션 회의 요약", or any request to pull Notion
  meeting data, analyze it, and produce summaries or presentations. Do NOT use
  for summarizing a meeting transcript without Notion source (use pm-execution
  summarize-meeting). Do NOT use for syncing markdown docs to Notion (use
  notion-docs-sync). Do NOT use for GitHub-to-Notion project sync (use the
  project's sync scripts). Do NOT use for ad-hoc PPTX creation without Notion
  source (use anthropic-pptx).
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# Notion Meeting Sync

Pull meeting notes from a Notion database, analyze them with PM skills,
generate comprehensive Korean summaries with detailed action items,
produce a PowerPoint presentation, and post the final digest to Slack
— all in a single sequential pipeline.

## Configuration

| Key | Value |
|-----|-------|
| Notion Database ID | `22c9eddc34e680d5beb9d2cf6c8403b4` |
| Notion View URL | `https://www.notion.so/thakicloud/22c9eddc34e680d5beb9d2cf6c8403b4?v=22c9eddc34e6805a8b50000c969ed362` |
| Output Directory | `output/meetings/` |
| Sync State File | `output/meetings/.sync-state.json` |
| Language | Korean |
| MCP Server (Notion) | `plugin-notion-workspace-notion` |
| MCP Server (Slack) | `plugin-slack-slack` |
| Slack Channel | `#ai-platform-chapter-기획` (ID: `C0AL6D32Z7W`) |

## Scoping Modes

| Mode | Trigger | Behavior |
|------|---------|----------|
| **all** | `/notion-meeting-sync` | Sync all new/updated meetings since last sync |
| **latest** | `/notion-meeting-sync latest` | Sync only the most recen
