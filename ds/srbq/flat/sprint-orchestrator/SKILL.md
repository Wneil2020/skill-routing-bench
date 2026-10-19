---
name: sprint-orchestrator
description: "Use when Auto-triage incoming GitHub issues and PRs, classify by type, assign priority (P0-P3), suggest assignees from CODEOWNERS/git blame: covers sprint, orchestrator, assignees, blame, codeowners"
metadata:
  holon-triggers: |
    triage issues
    auto-assign sprint items
---

---
name: sprint-orchestrator
description: >-
  Auto-triage incoming GitHub issues and PRs: classify by type, assign priority
  (P0-P3), suggest assignees from CODEOWNERS/git blame, update GitHub Project
  fields, and generate per-user digests. Use when the user asks to "triage
  issues", "auto-assign sprint items", "sprint orchestrator", "스프린트 관리",
  "이슈 자동 분류", "sprint-orchestrator", or wants overnight issue/PR triage
  and assignment. Do NOT use for creating issues from commits (use
  commit-to-issue), daily GitHub activity digests only (use
  github-sprint-digest), or manual sprint planning (use agency-sprint-prioritizer).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Sprint Orchestrator

Automated sprint triage: classify, prioritize, assign, and organize incoming issues and PRs overnight so the team starts each day with a clean, prioritized backlog.

## When to Use

- As part of the morning pipeline (after `sod-ship`, before sprint digest)
- When a batch of new issues/PRs needs triage
- At sprint boundaries to organize the incoming backlog

## Workflow

### Step 1: Fetch New Items

Query GitHub for untriaged items since last run:

```bash
gh issue list --repo <repo> --state open --label "" --json number,title,body,labels,createdAt,author
gh pr list --repo <repo> --state open --json number,title,body,labels,createdAt,author,reviewRequests
```

Filter to items created since last triage timestamp (stored in `.sprint-orchestrator-state.json`).

### Step 2: Classify Each Item

For each issue/PR, use LLM classification:

| Type | Criteria |
|------|----------|
| `bug` | Error reports, regression, "doesn't work", stack traces |
| `feature` | New functionality, user stories, "as a user I want" |
| `enhancement` | Improvements to existing features, UX tweaks |
| `chore` | Dependencies, CI/CD, documentation, refactoring |
| `security` | Vulnerability reports, CVEs, access control |

Apply the classified label via GitHub API.

### Step 3: As
