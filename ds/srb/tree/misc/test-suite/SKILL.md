---
name: test-suite
description: "Use when Run a full test lifecycle pipeline, 2 parallel review agents (Test Coverage, Test Quality) analyze existing tests, then a Test Generator creates: covers test, suite, 테스트, 감사, executes"
metadata:
  holon-triggers: |
    test review
    check test coverage
---

---
name: test-suite
description: >-
  Run a full test lifecycle pipeline: 2 parallel review agents (Test Coverage,
  Test Quality) analyze existing tests, then a Test Generator creates missing
  tests, and a Test Runner executes the suite with retry logic. Supports
  diff/today/full scoping. Use when the user runs /test-suite, asks for "test
  review", "check test coverage", "generate missing tests", "run and fix tests",
  or "full test audit". Do NOT use for single-file test writing, manual test
  execution only (use shell), or code review without test focus (use /simplify).
  Korean triggers: "테스트", "감사", "리뷰", "분석".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Test Suite — Test Full-Lifecycle Orchestrator

Analyze test coverage and quality from 2 perspectives simultaneously, auto-generate missing tests, then execute the suite and fix failures. Covers the entire test lifecycle from audit to green CI.

## Scoping Modes

| Mode | Trigger | Scope |
|------|---------|-------|
| `diff` (default) | `/test-suite` | Source + test files from git diff |
| `today` | `/test-suite today` | All files changed today |
| `full` | `/test-suite full` | All source and test files |

Optional flags:
- `--no-gen`: skip test generation (review only)
- `--no-run`: skip test execution
- Combinable: `/test-suite today --no-gen`

## Workflow

### Step 1: Identify Target Files

Resolve files using the scoping mode, then classify:

**Source files**: `*.ts`, `*.tsx`, `*.js`, `*.jsx`, `*.py`, `*.go`, `*.rs`, `*.java`, `*.kt` (excluding test files)
**Test files**: `*.test.*`, `*.spec.*`, files in `tests/`, `__tests__/`, `test/`
**Config files**: `jest.config.*`, `vitest.config.*`, `pytest.ini`, `pyproject.toml`, `playwright.config.*`

Build a source-to-test mapping by matching file names and directory structure.

### Step 2: Launch 2 Parallel Review Agents

Use the Task tool to spawn 2 read-only sub-agents. Each receives source files, test files, and the source-to
