---
name: pr-to-issue-linker
description: "Use when Automatically detect and maintain bidirectional links between PRs and issues. On PR creation, find related issues from branch names: covers issue, linker, maintain, bidirectional, names"
metadata:
  holon-triggers: |
    link PRs to issues
    bidirectional PR tracking
---

---
name: pr-to-issue-linker
description: >-
  Automatically detect and maintain bidirectional links between PRs and issues.
  On PR creation, find related issues from branch names, commit messages, and
  code changes. Update issues with PR status and auto-close on merge. Use when
  the user asks to "link PRs to issues", "bidirectional PR tracking",
  "PR-이슈 연결", "양방향 PR 추적", "pr-to-issue-linker", or wants automated
  PR-issue relationship management. Do NOT use for creating issues from commits
  (use commit-to-issue), PR review (use deep-review), or sprint triage (use
  sprint-orchestrator).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# PR-to-Issue Linker

Maintain bidirectional links between PRs and issues for complete traceability from requirement to implementation.

## When to Use

- After PR creation to auto-link to related issues
- During sprint tracking to see issue→PR progress
- As part of the release pipeline to verify all issues have PRs

## Workflow

### Step 1: Detect PR-Issue Relationships

On PR creation or update, detect related issues through multiple signals:

**Branch name** (highest confidence):
```
issue/123-add-auth    → Issue #123
feature/PROJ-456      → Issue #456
fix/bug-789           → Issue #789
```

**Commit messages** (high confidence):
```
Resolves #123         → Issue #123
Fixes #456            → Issue #456
Closes #789           → Issue #789
Related to #101       → Issue #101 (soft link)
```

**PR body** (medium confidence):
Parse PR description for issue references (`#NNN`, issue URLs).

**Code analysis** (low confidence):
If no explicit references found, analyze changed files against open issue descriptions to find potential matches.

### Step 2: Classify Link Type

| Type | Signal | Action on Merge |
|------|--------|-----------------|
| `resolves` | "Resolves #N", "Fixes #N", "Closes #N" | Auto-close issue |
| `addresses` | "Addresses #N", "Part of #N" | Update issue, don't close |
| `related` | "Relat
