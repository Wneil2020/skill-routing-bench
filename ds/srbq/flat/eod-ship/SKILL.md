---
name: eod-ship
description: "Use when End-of-day shipping pipeline, cursor-sync assets across projects, then release-ship the current project and 5 managed projects, posting a consolidated: covers eod, ship, scrum, wrap, managed"
metadata:
  holon-triggers: |
    wrap up for the day
    end of day ship
---

---
name: eod-ship
description: >-
  End-of-day shipping pipeline: cursor-sync assets across projects, then
  release-ship the current project and 5 managed projects, posting a
  consolidated summary to Slack. Use when the user runs /eod-ship, asks to "wrap
  up for the day", "end of day ship", "하루 마무리", "퇴근 전 커밋", or "EOD push all
  projects". Do NOT use for syncing .cursor/ assets only (use cursor-sync),
  shipping a single repo (use release-ship), or daily standup/scrum automation
  (use daily-scrum).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# EOD Ship — End-of-Day Multi-Project Shipping Pipeline

Chain cursor-sync and release-ship across all managed projects in a single flow. Syncs `.cursor/` assets first, ships uncommitted changes in the current project and 5 managed repos, then posts a consolidated report to Slack.

## Configuration

- **Managed projects**: See [references/project-registry.md](references/project-registry.md)
- **Slack channel**: `#효정-할일` (Channel ID: `C0AA8NT4T8T`)
- **Upstream skills**: `cursor-sync`, `release-ship`

## Usage

```
/eod-ship                        # full pipeline (sync + ship all + Slack)
/eod-ship --skip-sync            # skip cursor-sync, ship only
/eod-ship --targets research     # ship specific project only (comma-separated)
/eod-ship --dry-run              # preview what would be shipped (no commits/push)
/eod-ship --no-slack             # skip Slack notification
```

Arguments can be combined freely. Defaults: sync all, ship all projects, post to Slack.

## Workflow

### Phase 1: Cursor Sync

**Skip if** `--skip-sync` flag is set.

Follow the `cursor-sync` skill (`.cursor/skills/cursor-sync/SKILL.md`).

```bash
# Sync .cursor/{commands,skills,rules} to all target projects
```

1. Read target paths from `cursor-sync/references/sync-targets.md`
2. Run rsync dry-run preview for each target
3. Execute sync
4. Capture per-target summary: `{target: {new: N, updated: N}}`

### Phase 1½: Dev Bra
