---
name: bespin-news-digest
description: "Use when Fetch the latest Bespin Global news email from Gmail, extract all article URLs, apply the full x-to-slack research pipeline (Jina content: covers bespin, news, digest, clipping, jina"
metadata:
  holon-triggers: |
    process Bespin news
    뉴스 클리핑 분석
---

---
name: bespin-news-digest
description: >-
  Fetch the latest Bespin Global news email from Gmail, extract all article URLs,
  apply the full x-to-slack research pipeline (Jina content extraction + WebSearch
  + AI GPU Cloud classification + 3-message Slack thread) to EACH article
  sequentially, generate a rich DOCX with all findings, upload to Google Drive,
  and post a summary to #효정-할일. Use when the user runs /bespin-news, asks to
  "process Bespin news", "뉴스 클리핑 분석", "bespin-news-digest", "베스핀 뉴스",
  or wants a detailed analysis of the latest Bespin Global news clipping.
  Do NOT use for general Gmail triage (use gmail-daily-triage).
  Do NOT use for single article analysis (use x-to-slack).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Bespin News Digest

Fetch the latest Bespin News email, research each article with the full x-to-slack
pipeline, post a 3-message Slack thread per article to `#press`, generate a
comprehensive DOCX, and post a Drive-linked summary to `#효정-할일`.

> **Pattern**: mirrors `twitter-timeline-to-slack` — sequential processing with
> mandatory WebSearch per item. No shortcuts.

## Slack Channel Registry

| Channel | ID | Purpose |
|---|---|---|
| `press` | `C0A7NCP33LG` | Per-article threads (news/media) |
| `효정-할일` | `C0AA8NT4T8T` | Final summary post |
| `효정-insight` | `C0A8SSPC9RU` | (optional override for high-impact articles) |
| `효정-의사결정` | `C0ANBST3KDE` | Personal decision items (decision-router) |
| `7층-리더방` | `C0A6Q7007N2` | Team/CTO decision items (decision-router) |

## Phase 1 — Gmail Fetch

Find the most recent email from `bespin_news@bespinglobal.com`:

```bash
gws gmail +triage \
  --query "from:bespin_news@bespinglobal.com" \
  --max 3 \
  --format json 2>&1
```

Skip the first line (`Using keyring backend: keyring`), parse JSON, and take
`messages[0]` (the most recent). Extract `id` and `subject` (date reference).

If no messages found → report error and exit.

Fetch the full message body
