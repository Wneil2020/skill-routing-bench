---
name: ship
description: "Use when End-to-end pre-merge pipeline that reviews code with 4 parallel agents, auto-fixes findings, verifies with linting, creates domain-split commits, and: covers ship, 출시, 리뷰, linting, opens"
metadata:
  holon-triggers: |
    ship it
    prepare for merge
---

---
name: ship
description: >-
  End-to-end pre-merge pipeline that reviews code with 4 parallel agents,
  auto-fixes findings, verifies with linting, creates domain-split commits, and
  opens a PR. Use when the user runs /ship, asks to "ship it", "prepare for
  merge", "create a PR with review", or "commit and PR". Do NOT use for
  review-only (use /simplify or /deep-review), manual commits (use
  /domain-commit), or PR management (use /pr-create, /pr-review). Korean
  triggers: "출시", "리뷰", "생성", "파이프라인".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Ship — Pre-Merge Pipeline

One command to go from "code is done" to "PR is ready". Runs parallel code review, auto-fixes issues, creates domain-split commits, and opens a PR.

## Usage

```
/ship                           # full pipeline: review → fix → commit → PR
/ship --no-pr                   # review → fix → commit (skip PR creation)
/ship --dry-run                 # review only, show what would happen
/ship --base main               # specify PR base branch (default: main)
/ship --no-fix                  # review → commit → PR (skip auto-fix)
```

Arguments can be combined: `/ship --base dev --no-fix`.

## Workflow

For detailed step configuration, see [references/pipeline-steps.md](references/pipeline-steps.md).

### Step 1: Identify Changed Files

```bash
git diff --name-only
git diff --cached --name-only
git diff HEAD --name-only
```

If no changes, fall back to `git diff HEAD~1 HEAD --name-only`.
If still empty, inform the user and stop.

### Step 2: Parallel Review (4 Agents)

Launch 4 sub-agents via the Task tool (same pattern as `/simplify`):

```
Agent 1: Refactor Agent        → Code structure, SOLID, duplication
Agent 2: Quality Agent         → Readability, naming, patterns
Agent 3: Tech Debt + Analyzer  → TODO/FIXME, root cause, structural issues
Agent 4: Performance Agent     → Efficiency, Big-O, redundant operations
```

Sub-agent config: `subagent_type: generalPurpose`,
