---
name: issue-to-code
description: "Use when Generate code drafts from GitHub issue descriptions. Reads the issue, analyzes codebase context via semantic search, creates an: covers issue, code, resolves, specifications, implementations"
metadata:
  holon-triggers: |
    implement this issue
    issue to code
---

---
name: issue-to-code
description: >-
  Generate code drafts from GitHub issue descriptions. Reads the issue, analyzes
  codebase context via semantic search, creates an implementation plan,
  generates code on a feature branch, and opens a draft PR with "Resolves #N".
  Use when the user asks to "implement this issue", "issue to code", "generate
  code from issue", "이슈에서 코드 생성", "이슈 구현", "issue-to-code", or wants
  automated first-draft implementations from issue specifications. Do NOT use
  for manual coding tasks without an issue, PR review (use deep-review),
  or committing existing changes (use domain-commit).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Issue-to-Code Draft Generator

Automate the first step of development: transform a GitHub issue into a code draft with a ready-to-review PR.

## When to Use

- When a new issue is assigned and needs an initial implementation draft
- As part of the sprint-orchestrator pipeline for auto-drafting low-complexity issues
- When the user provides an issue number or URL and asks for a draft implementation

## Workflow

### Step 1: Fetch Issue Context

Use the GitHub MCP to retrieve the full issue:

```
gh issue view <issue-number> --json title,body,labels,assignees,milestone,comments
```

Extract:
- **Requirements**: From issue body (user stories, acceptance criteria, technical specs)
- **Labels**: For classification (bug, feature, enhancement, documentation)
- **Linked issues/PRs**: For dependency context. Check for existing open PRs referencing this issue — if one exists, report it instead of creating a duplicate.
- **Comments**: For clarifications and discussion history

### Step 2: Classify Complexity

Score the issue complexity (1-5) based on:
- Number of acceptance criteria
- Cross-file impact (single file vs multi-file vs multi-service)
- Test requirements mentioned
- Labels (`good-first-issue` = low, `epic` = high)

If complexity > 3, generate a plan document instead of code. P
