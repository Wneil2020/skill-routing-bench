---
name: sod-ship
description: "Use when Start-of-day git sync pipeline, commit dirty working directories, push unpushed commits, and pull remote changes for all 5 managed projects: covers sod, ship, along, dirty, resolving"
metadata:
  holon-triggers: |
    sync all projects
    start of day sync
---

---
name: sod-ship
description: >-
  Start-of-day git sync pipeline: commit dirty working directories, push
  unpushed commits, and pull remote changes for all 5 managed projects,
  resolving errors along the way. Use when the user runs /sod-ship, asks to
  "sync all projects", "start of day sync", "pull all repos", "컴퓨터 바꿔서
  작업 시작", "아침 싱크", "프로젝트 동기화", "sod-ship", or needs to ensure all
  repos are clean and up-to-date before starting work. Do NOT use for
  end-of-day shipping (use eod-ship), morning briefing with Google/stock
  pipelines (use morning-ship), or syncing .cursor/ assets only (use
  cursor-sync).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# SOD Ship — Start-of-Day Git Sync Pipeline

Bidirectional git sync for all managed projects: commit dirty repos, push unpushed commits, pull remote changes, and verify everything is in sync. Designed for starting work on a new day or switching to a different computer.

## Configuration

- **Managed projects**: See [eod-ship project-registry.md](../eod-ship/references/project-registry.md)
- **Slack channel**: `#효정-할일` (Channel ID: `C0AA8NT4T8T`)
- **Upstream patterns**: `domain-commit` (commit splitting), `release-ship` (push strategy per repo mode)

## Usage

```
/sod-ship                          # full pipeline (commit + push + pull + Slack)
/sod-ship --skip-push              # pull only, skip committing/pushing local changes
/sod-ship --skip-pull              # commit and push only, skip pulling remote
/sod-ship --targets research       # process specific projects only (comma-separated)
/sod-ship --no-slack               # skip Slack notification
/sod-ship --no-canvas              # skip Slack Canvas update (Phase 7b)
/sod-ship --dry-run                # preview only (show status, no git operations)
```

Arguments can be combined freely. Defaults: commit+push+pull all, post to Slack, update canvas.

## Workflow

### Phase 1: Pre-flight Scan

Scan all managed projects to build a s
