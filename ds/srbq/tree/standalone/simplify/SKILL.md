---
name: simplify
description: "Use when Run parallel code review agents to analyze code for reuse opportunities, code quality, tech debt, and performance issues, then auto-fix findings: covers simplify, 리뷰, 분석, individually, reuse"
metadata:
  holon-triggers: |
    simplify code
    review and fix changes
---

---
name: simplify
description: >-
  Run parallel code review agents to analyze code for reuse opportunities, code
  quality, tech debt, and performance issues, then auto-fix findings by
  priority. Supports 3 scoping modes: diff (changed files), today (daily work),
  and full (entire project). Use when the user runs /simplify, asks to "simplify
  code", "review and fix changes", "clean up my code", or "review today's work".
  Do NOT use for single-domain review (use /refactor, /performance, etc.
  individually), creating new features, or general Q&A. Korean triggers: "리뷰",
  "분석", "수정", "성능".
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "execution"
---
# Simplify — Parallel Code Review & Auto-Fix

Analyze code through 4 parallel review agents, aggregate findings, and auto-fix issues by priority. Supports 3 scoping modes: changed files, daily work, or full project.

## Scoping Modes

Determine the scope from the user's input:

| Mode | Trigger | Scope |
|------|---------|-------|
| `diff` (default) | `/simplify` or `/simplify diff` | Git diff (unstaged + staged + HEAD) |
| `today` | `/simplify today` | All files changed today (`--since=midnight`) |
| `full` | `/simplify full` or `/simplify project` | All source files in the project |

Mode keywords can be combined with other arguments: `/simplify today focus on performance`.

## Workflow

### Step 1: Identify Target Files

Resolve files based on the scoping mode:

**Mode: diff (default)**
```bash
git diff --name-only          # unstaged
git diff --cached --name-only # staged
git diff HEAD --name-only     # combined
```
If no changes found, fall back to `git diff HEAD~1 HEAD --name-only`.
If still empty, inform the user and stop.

**Mode: today**
```bash
git log --since=midnight --name-only --pretty=format: | sort -u
```
Shows all files touched in today's commits plus current uncommitted changes.
Combine with `git diff --name-only` for uncommitted work.

**Mode: full**
```bash
find . -type f \( -name "*
