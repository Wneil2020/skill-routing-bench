---
name: morning
description: "Use when Morning routine orchestrator that runs google-daily (calendar briefing, Gmail triage, Drive upload, Slack notification) then: covers morning, notification, sequence, shipping, consolidated"
metadata:
  holon-triggers: |
    start my morning
    morning routine
---

---
name: morning
description: >-
  Morning routine orchestrator that runs google-daily (calendar briefing, Gmail
  triage, Drive upload, Slack notification) then today (stock data sync,
  screening, analysis, report) in sequence. Posts a consolidated morning
  briefing to Slack.
  Use when the user asks to "start my morning", "morning routine", "morning",
  "아침 루틴", "아침", "모닝", "하루 시작", "start the day", "/morning".
  Do NOT use for google-daily only (use google-daily), today pipeline only
  (use today), or end-of-day shipping (use eod-ship).
metadata:
  author: thaki
  version: 1.0.0
  category: execution
---

# Morning — Daily Morning Routine Orchestrator

Runs Google Workspace automation and the stock analysis pipeline as a
single morning sequence. Google Daily handles personal productivity
(calendar, email, documents); Today handles market data and analysis.

## Prerequisites

- `gws` CLI installed and authenticated (`gws auth login -s drive,gmail,calendar`)
- PostgreSQL running with migrated schema
- Stock CSV files in `data/latest/` (seed via `stock-csv-downloader` if empty)
- Slack MCP server (`plugin-slack-slack`) connected
- Node.js with `docx` package installed (`cd outputs && npm install`)

## Pipeline Overview

```
Phase 1: Google Daily   (calendar → gmail → drive → slack → memory)
Phase 2: Today Pipeline  (data sync → fundamentals → discovery → screening → analysis → report)
Phase 3: Morning Briefing (consolidated Slack summary to #효정-할일)
```

Estimated time: 15–25 minutes total (Google Daily ~5min, Today ~10–20min).

## Phase 1: Google Daily

Read and execute `.cursor/skills/google-daily/SKILL.md`.

Skip this phase if `--skip-google` is set.

The Google Daily skill runs 5 sub-phases:
1. Calendar briefing (today's schedule)
2. Gmail triage (spam removal, notification labeling, colleague email summaries)
3. Drive upload (generated documents)
4. Slack notification (main summary + threaded replies to `#효정-할일`)
5. Memory sync (append daily entry to `MEMORY.
