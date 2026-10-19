---
name: ui-suite
description: "Use when Run a full UI/UX lifecycle pipeline, 3 parallel review agents (Design Audit, Web Standards, UX/Design System) analyze UI code, then a UI Builder agent: covers suite, 감사, 리뷰, uis, elements"
metadata:
  holon-triggers: |
    UI review
    design audit
---

---
name: ui-suite
description: >-
  Run a full UI/UX lifecycle pipeline: 3 parallel review agents (Design Audit,
  Web Standards, UX/Design System) analyze UI code, then a UI Builder agent
  auto-fixes findings and generates missing UI elements. Supports
  diff/today/full scoping. Use when the user runs /ui-suite, asks for "UI
  review", "design audit", "UX check", "frontend quality review", or "fix my
  UI". Do NOT use for building new UIs from scratch without existing code (use
  frontend-design), single-domain code review (use /simplify or /deep-review),
  or backend-only review. Korean triggers: "감사", "리뷰", "빌드", "분석".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# UI Suite — UI/UX Full-Lifecycle Orchestrator

Review UI code from 3 design perspectives simultaneously, aggregate findings, then auto-fix issues and generate missing UI elements. Combines design auditing with hands-on improvement.

## Scoping Modes

| Mode | Trigger | Scope |
|------|---------|-------|
| `diff` (default) | `/ui-suite` | Git diff (unstaged + staged + HEAD) |
| `today` | `/ui-suite today` | All files changed today |
| `full` | `/ui-suite full` | All source files in the project |

Combinable with focus: `/ui-suite today focus on accessibility`.

## Workflow

### Step 1: Identify UI Files

Resolve target files using the scoping mode (same commands as `/simplify`), then filter to UI-relevant files only:

**Include**: `*.tsx`, `*.jsx`, `*.vue`, `*.svelte`, `*.css`, `*.scss`, `*.html`, files in `components/`, `pages/`, `views/`, `layouts/`, `styles/`, `ui/`

**Exclude**: `*.test.*`, `*.spec.*`, pure utility/helper files with no UI exports, config files

If no UI files are found, inform the user and suggest scoping to a UI directory.

### Step 2: Launch 3 Parallel Review Agents

Use the Task tool to spawn 3 read-only sub-agents. Each agent receives the list of UI files and their contents. For detailed prompts, see [references/agent-prompts.md](references/agent-p
