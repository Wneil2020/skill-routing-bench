---
name: commit-to-issue
description: "Use when Analyze recent git commits and create GitHub issues with project field setup on ThakiCloud project boards. Use when the user asks to \"create issues from: covers commit, issue, 커밋, 리뷰, boards"
metadata:
  holon-triggers: |
    create issues from commits
    track commits as issues
---

---
name: commit-to-issue
description: >-
  Analyze recent git commits and create GitHub issues with project field setup
  on ThakiCloud project boards. Use when the user asks to "create issues from
  commits", "track commits as issues", "register work to project", "sync commits
  to GitHub project", or "turn commits into issues". Do NOT use for committing
  local changes (use domain-commit), PR creation or review (use
  pr-review-captain), or CI pipeline validation (use ci-quality-gate). Korean
  triggers: "커밋", "리뷰", "분석", "생성".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Commit-to-Issue

Turns git commit history into tracked GitHub issues with full project board integration. Analyzes commits, groups them into logical issue batches, creates issues with structured bodies, adds them to a ThakiCloud project, and configures all project fields (Status, Priority, Size, Sprint, Estimate).

## Prerequisites

- `gh` CLI authenticated with access to the target repository and ThakiCloud org
- For issue templates, see [references/issue-templates.md](references/issue-templates.md)
- For project field IDs and GraphQL, see [references/project-config.md](references/project-config.md)
- For Epic/sub-issue management, see [references/epic-sub-issues.md](references/epic-sub-issues.md)

## Workflow

### Step 1: Gather commit context

Identify the commits to convert into issues. Support three modes:

- **Date range**: `git log --since="YYYY-MM-DD" --until="YYYY-MM-DD" --format="%h %ai %s" --all`
- **Last N commits**: `git log --oneline -N`
- **Branch diff**: `git log --oneline main..HEAD`

Also run `git remote -v` to extract the repo owner and name (e.g., `sylvanus4/call-center-tts`).

### Step 2: Analyze and group commits

Read each commit's changed files with `git show --stat <hash>`. Group related commits into logical issue batches by module or domain. Each batch becomes one issue.

Determine for each issue:
- **Title**: `[TYPE] Summary` per CONTRIB
