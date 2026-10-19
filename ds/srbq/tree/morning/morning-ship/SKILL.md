---
name: morning-ship
description: "Use when Start-of-day pipeline, git pull all 5 managed repos (ai-platform-webui via tmp branch), run Google Workspace briefing (calendar + Gmail triage): covers morning, ship, pulling, tmp, webui"
metadata:
  holon-triggers: |
    start my day
    morning ship
---

---
name: morning-ship
description: >-
  Start-of-day pipeline: git pull all 5 managed repos (ai-platform-webui via
  tmp branch), run Google Workspace briefing (calendar + Gmail triage), run the
  daily stock analysis pipeline, and post a consolidated morning briefing to
  Slack. Use when the user runs /morning-ship, asks to "start my day", "morning
  ship", "아침 시작", "출근 파이프라인", "morning pull all", or "pull and brief". Do NOT
  use for pulling a single repo (use git directly), running Google daily only
  (use google-daily), running the stock pipeline only (use today), or end-of-day
  shipping (use eod-ship).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Morning Ship — Start-of-Day Multi-Project Pipeline

Pull latest changes from all managed repos, run Google Workspace briefing, kick off the daily stock pipeline, and post a consolidated morning briefing to Slack.

## Configuration

- **Managed projects**: See [eod-ship project-registry.md](../eod-ship/references/project-registry.md)
- **Slack channel**: `#효정-할일` (Channel ID: `C0AA8NT4T8T`)
- **Upstream skills**: `calendar-daily-briefing`, `gmail-daily-triage`, `today`

## Usage

```
/morning-ship                        # full pipeline (pull + google + stock + Slack)
/morning-ship --skip-pull            # skip git pull, start from Google daily
/morning-ship --skip-google          # skip calendar briefing and Gmail triage
/morning-ship --skip-stock           # skip daily stock pipeline
/morning-ship --targets research     # pull specific projects only (comma-separated)
/morning-ship --no-slack             # skip Slack notification
/morning-ship --dry-run              # preview only (no git pull, no triage, no pipeline)
```

Arguments can be combined freely. Defaults: pull all, run Google daily, run stock pipeline, post to Slack.

## Workflow

### Phase 1: Git Sync (Pull All Managed Projects)

**Skip if** `--skip-pull` or `--dry-run` flag is set.

**If `--targets` is set**, only pull the 
