---
name: release-ship
description: "Use when Lightweight shipping pipeline, domain-split commits, git push, and PR creation/update in one flow. Use when the user asks to: covers release, ship, included, lightweight, trivial"
metadata:
  holon-triggers: |
    release-ship
    commit and push
---

---
name: release-ship
description: >-
  Lightweight shipping pipeline: domain-split commits, git push, and PR
  creation/update in one flow. Use when the user asks to "release-ship", "commit
  and push", "commit and PR", "push and create PR", "커밋하고 PR", "커밋하고 푸시", "ship
  without review", or wants to go from uncommitted changes to an open PR without
  code review. Do NOT use for review-included shipping (use ship), full release
  validation pipeline (use release-commander), domain-split commits only without
  push/PR (use domain-commit), or single-file trivial commits.
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Release Ship — Commit, Push, Issue, PR, and Merge Pipeline

Lightweight pipeline to go from uncommitted changes to a merged PR. Chains domain-split commits, push, issue creation with project linking, PR creation, and auto-merge without code review overhead.

## Repository-Specific Behavior

### ai-platform-webui (ThakiCloud/ai-platform-webui)

**Exception**: This repo works exclusively on the `tmp` branch. PR creation and merge steps are **always skipped**. The pipeline is:

```
commit → push → issue → report
```

No cross-branch merges. No PRs targeting `dev` or `main`. All work stays on `tmp`.

### Other repos

Full pipeline applies: `commit → push → issue → PR → merge`.

## Usage

```
/release-ship                    # full pipeline (webui: commit→push→issue→report)
/release-ship --no-pr            # commit → push → issue (skip PR and merge)
/release-ship --no-issue         # commit → push → PR → merge (skip issue creation)
/release-ship --no-merge         # commit → push → issue → PR (skip merge)
/release-ship --base dev         # specify PR base branch (default: auto-detect)
/release-ship --update           # force-update existing PR body
```

## Workflow

### Step 1: Pre-flight

```bash
git status --short
git branch --show-current
git log --oneline -5
```

1. If working directory is clean, stop and inform the user.
2. 
