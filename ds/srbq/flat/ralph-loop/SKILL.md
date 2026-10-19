---
name: ralph-loop
description: "Use when Set up and run the Ralph Loop — a continuous AI agent loop that completes tasks one-by-one from a structured task list, persisting state in text files: covers ralph, loop, 리뷰, 설계, completes"
metadata:
  holon-triggers: |
    run ralph loop
    set up ralph loop
---

---
name: ralph-loop
description: >-
  Set up and run the Ralph Loop — a continuous AI agent loop that completes
  tasks one-by-one from a structured task list, persisting state in text files
  and git commits so each iteration starts with a fresh context window. Use when
  the user asks to "run ralph loop", "set up ralph loop", "continuous agent
  loop", "long-running agent", "AFK coding", "batch task execution", or wants to
  run an AI agent autonomously for many iterations without context window
  limits. Do NOT use for single-task execution (just run the task directly),
  interactive pair-programming sessions (use normal agent mode), or tasks
  requiring pixel-perfect design review (Ralph Loop excels at functional code,
  not visual polish). Korean triggers: "리뷰", "설계", "커밋".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Ralph Loop

Run an AI coding agent in a continuous loop, completing a structured task list one task per iteration. Each iteration gets a fresh context window; state is persisted in `.agent/` text files and git commits.

Named after Ralph Wiggum from The Simpsons. Originated from [PageAI-Pro/ralph-loop](https://github.com/PageAI-Pro/ralph-loop).

## Prerequisites

- **Docker Desktop** with AI sandbox support (`docker sandbox run`)
- **Claude Code** CLI (or alternative: Codex, Gemini CLI, Copilot CLI, Kiro)
- **Git** initialized repository
- **Test infrastructure**: Playwright (E2E) + Vitest/Jest (unit) recommended

## Workflow

### Step 1: Bootstrap Project

Verify the project has test infrastructure. If missing, scaffold it:

```bash
# Check for existing test setup
ls package.json vitest.config.* playwright.config.* 2>/dev/null

# If missing, install
npm install -D vitest @testing-library/react playwright @playwright/test
npx playwright install chromium
```

### Step 2: Install Ralph Loop

```bash
npx @pageai/ralph-loop
```

This creates the `.agent/` directory. Verify the structure:

```bash
ls -la .agent/
# Expec
