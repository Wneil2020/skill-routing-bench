---
name: md-enhance-publish
description: "Use when Enhance markdown documents with Mermaid diagrams, decision matrices, quantitative evidence, and industry comparisons, then publish to Notion: covers enhance, publish, 문서 보강, 마크다운 보강, aids"
metadata:
  holon-triggers: |
    enhance and publish markdown
    enrich docs and upload to Notion
---

---
name: md-enhance-publish
description: >-
  Enhance markdown documents with Mermaid diagrams, decision matrices,
  quantitative evidence, and industry comparisons, then publish to Notion
  and post a summary thread to Slack. Sequential pipeline: discover → analyze
  → enhance → convert → publish → distribute. Use when the user asks to
  "enhance and publish markdown", "enrich docs and upload to Notion",
  "add diagrams and publish", "마크다운 보강 후 노션", "문서 보강해서 노션에 올려",
  "그래프 추가하고 노션", "도표 보강해서 슬랙에 공유", "md-enhance-publish",
  or wants to enrich existing markdown with visual aids and distribute to
  Notion + Slack. Do NOT use for uploading markdown as-is (use md-to-notion).
  Do NOT use for creating documents from scratch (use anthropic-docx).
  Do NOT use for Notion database operations (use Notion MCP directly).
  Korean triggers: "문서 보강", "마크다운 보강", "그래프 추가 퍼블리시",
  "도표 추가 노션", "보강해서 올려".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# md-enhance-publish

Enrich markdown → convert for Notion → publish → Slack thread.

## Input

| Parameter | Required | Default |
|-----------|----------|---------|
| `<path>` | Yes | — |
| `--parent <id>` | No | `3239eddc34e680e8a7a5d5b5eac18b38` |
| `--slack <channel_id>` | No | `C0AA8NT4T8T` (#효정-할일) |
| `--icon <emoji>` | No | Auto-assigned per doc |
| `--skip-slack` | No | false |
| `--skip-notion` | No | false (enhance only) |
| `--dry-run` | No | false (show plan, no edits) |
| `--lang <ko\|en>` | No | `ko` |

## Subagent Strategy

Use parallel subagents to maximize throughput:

| Phase | Parallelizable | Strategy |
|-------|---------------|----------|
| Discover + Analyze | No | Sequential — need file list first |
| Enhance | Yes | 1 subagent per file (max 4 concurrent) |
| Convert | Yes | Batch via script |
| Publish | Partially | 2 pages per MCP call, sequential calls |
| Distribute | No | Sequential — need all page IDs |

For ≤3 files, run enhancement sequentially in main context.
For 4+ files,
