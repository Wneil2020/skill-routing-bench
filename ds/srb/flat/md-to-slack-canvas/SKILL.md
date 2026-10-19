---
name: md-to-slack-canvas
description: "Use when Publish local markdown files as Slack Canvas documents. Reads one file or globs a folder for *.md, extracts H1 as canvas title, transforms: covers slack, canvas, 슬랙 캔버스, 캔버스 업로드, blockquote"
metadata:
  holon-triggers: |
    upload markdown to Slack Canvas
    publish md to Slack Canvas
---

---
name: md-to-slack-canvas
description: >-
  Publish local markdown files as Slack Canvas documents. Reads one file
  or globs a folder for *.md, extracts H1 as canvas title, transforms
  markdown to Slack Canvas flavor (header depth truncation, blockquote-to-callout
  conversion, table pipe escaping), and creates or updates canvases via Slack MCP.
  Use when the user asks to "upload markdown to Slack Canvas",
  "publish md to Slack Canvas", "create canvas from file", "push to canvas",
  "마크다운 슬랙 캔버스", "슬랙 캔버스 업로드", "md-to-slack-canvas",
  "캔버스에 올려", "캔버스로 변환", "슬랙 캔버스에 올려줘".
  Do NOT use for Slack message posting (use kwp-slack-slack-messaging).
  Do NOT use for Notion page publishing (use md-to-notion).
  Do NOT use for channel messaging or thread replies (use Slack MCP slack_send_message).
  Korean triggers: "슬랙 캔버스", "캔버스 업로드", "마크다운 캔버스", "캔버스에 올려".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---

# md-to-slack-canvas

Lightweight publisher: point at local markdown files and get Slack Canvas
documents. Handles header depth truncation, blockquote-to-callout conversion,
and table escaping automatically.

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `<path>` | Yes | File path or folder path containing `.md` files |
| `--channel <id>` | No | Post canvas link to this Slack channel after creation |
| `--update <canvas_id>` | No | Update an existing canvas instead of creating new |
| `--append` | No | Append content to end of existing canvas (requires `--update`) |
| `--skip-meta` | No | Skip README.md, CHANGELOG.md, LICENSE.md |
| `--title-prefix <str>` | No | Prepend string to each canvas title |
| `--dry-run` | No | List files and titles without creating canvases |

## Workflow

```
Step 1: Resolve   → Collect .md file paths from input
Step 2: Transform → Convert standard markdown to Canvas markdown flavor
Step 3: Publish   → Create or update canvases via Slack MCP
Step 4: Verify    → Read ba
