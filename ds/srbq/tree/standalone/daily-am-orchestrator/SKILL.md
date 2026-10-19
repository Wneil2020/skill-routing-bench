---
name: daily-am-orchestrator
description: "Use when Morning Pipeline orchestrator, 8 phases covering pre-flight, git sync, Google Workspace, email intelligence, market intelligence: covers daily, orchestrator, evening, routines, covering"
metadata:
  holon-triggers: |
    run morning pipeline
    morning automation
---

---
name: daily-am-orchestrator
description: >-
  Morning Pipeline orchestrator: 8 phases covering pre-flight, git sync, Google
  Workspace, email intelligence, market intelligence, news/content, AI research,
  and dev intelligence — with a consolidated Slack briefing. Runs at 7:00 AM
  daily. Use when the user runs /daily-am, asks to "run morning pipeline",
  "morning automation", "아침 파이프라인", "모닝 오케스트레이터", "daily-am", "daily
  morning", or wants to run the full morning automation. Do NOT use for partial
  morning routines (use morning-ship), individual skills (invoke them directly),
  or evening pipeline (use daily-pm-orchestrator).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "orchestration"
---
# Daily AM Orchestrator — Morning Pipeline (7:00 AM)

Orchestrate 8 phases of morning automation across 15+ skills with parallel execution where possible, consolidated Slack briefing, and robust error handling.

## Configuration

- **Slack channel**: `#효정-할일` (Channel ID: `C0AA8NT4T8T`)
- **Stock Slack**: `#h-report` (Channel ID: `C0AKHQWJBLZ`)
- **Research Slack**: `#deep-research` (Channel ID: `C0A6X68LTN1`)
- **Design doc**: `docs/daily-automation-guide.md`
- **Pipeline state**: `outputs/pipeline-state/YYYY-MM-DD-am.json`

## Usage

```
/daily-am                         # full morning pipeline
/daily-am --skip-phase 4          # skip Market Intelligence
/daily-am --only-phase 2,3        # run only Google + Email phases
/daily-am --skip-market           # skip market (auto on weekends)
/daily-am --skip-email            # skip email intelligence
/daily-am --skip-research         # skip AI research
/daily-am --no-slack              # suppress Slack notifications
/daily-am --dry-run               # preview plan without execution
```

## Workflow

### Initialization

1. Record start time: `pipeline_start = now()`
2. Initialize results tracker:
   ```python
   results = {
     "date": "YYYY-MM-DD",
     "pipeline": "am",
     "phases": {},
     "start_time": pip
