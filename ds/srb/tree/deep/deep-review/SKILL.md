---
name: deep-review
description: "Use when Run 4 parallel domain-expert agents (Frontend, Backend/DB, Security, Test Coverage) to review code from multiple engineering perspectives and auto-fix: covers deep, review, 리뷰, 테스트, scoping"
metadata:
  holon-triggers: |
    full-stack review
    multi-domain review
---

---
name: deep-review
description: >-
  Run 4 parallel domain-expert agents (Frontend, Backend/DB, Security, Test
  Coverage) to review code from multiple engineering perspectives and auto-fix
  findings. Supports diff/today/full scoping. Use when the user runs
  /deep-review, asks for "full-stack review", "multi-domain review", "review
  frontend and backend", or "comprehensive code review". Do NOT use for
  single-domain review (use /refactor, /security, etc.), code quality metrics
  only (use /simplify), or general Q&A. Korean triggers: "리뷰", "테스트", "수정",
  "보안".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Deep Review — Multi-Domain Full-Stack Review

Review code from 4 engineering perspectives simultaneously: frontend, backend/DB, security, and test coverage. Complements `/simplify` (code craftsmanship) with domain expertise.

## Scoping Modes

| Mode | Trigger | Scope |
|------|---------|-------|
| `diff` (default) | `/deep-review` | Git diff (unstaged + staged + HEAD) |
| `today` | `/deep-review today` | All files changed today |
| `full` | `/deep-review full` | All source files in the project |

Combinable with focus: `/deep-review today focus on security`.

## Workflow

### Step 1: Identify and Classify Files

Resolve target files using the same scoping as `/simplify` (git diff, git log --since=midnight, or find).

Classify each file by domain:
- **Frontend**: `*.tsx`, `*.jsx`, `*.vue`, `*.svelte`, `*.css`, `*.scss`, files in `components/`, `pages/`, `views/`, `layouts/`
- **Backend**: `*.py`, `*.go`, `*.rs`, `*.java`, `*.kt`, files in `api/`, `routes/`, `services/`, `middleware/`
- **DB**: `*.sql`, files in `migrations/`, `models/`, `schemas/`, `db/`
- **Test**: `*.test.*`, `*.spec.*`, files in `tests/`, `__tests__/`
- **Shared**: config files, utilities — sent to all agents

### Step 2: Launch 4 Parallel Review Agents

Use the Task tool to spawn 4 sub-agents. Each agent receives all files but focuses on its domain. For deta
