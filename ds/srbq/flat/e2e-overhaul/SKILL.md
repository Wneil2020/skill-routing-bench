---
name: e2e-overhaul
description: "Use when End-to-end Playwright test overhaul pipeline, run full suite across 3 browsers (chromium/firefox/mobile), triage failures by category: covers e2e, overhaul, E2E 전체 점검, E2E 오버홀, browsers"
metadata:
  holon-triggers: |
    overhaul E2E tests
    fix all E2E failures
---

---
name: e2e-overhaul
description: >-
  End-to-end Playwright test overhaul pipeline: run full suite across 3 browsers
  (chromium/firefox/mobile), triage failures by category (selector/mock/timeout/logic),
  fix frontend bugs and test issues with parallel subagents, extend coverage for
  uncovered pages, browser-verify all tabs with screenshots, and produce a final
  pass/fail report. Composes e2e-testing, diagnose, qa-test-expert, and browser-use.
  Use when the user asks to "overhaul E2E tests", "fix all E2E failures",
  "comprehensive E2E", "E2E 전체 점검", "E2E 오버홀", "테스트 전체 수정",
  "E2E 100% 통과", "all tabs browser test", or wants to go from many failing
  tests to 100% pass rate with full coverage. Do NOT use for writing a single
  test file (use e2e-testing). Do NOT use for test strategy planning only (use
  qa-test-expert). Do NOT use for running tests without fixing (use e2e-test
  command). Do NOT use for unit or integration tests (use test-suite).
  Korean triggers: "E2E 전체 점검", "E2E 오버홀", "테스트 전체 수정", "E2E 100% 통과".
metadata:
  author: thaki
  version: "1.0.0"
  category: execution
---

# E2E Overhaul — Comprehensive Test Fix & Extend Pipeline

One command to go from "many E2E tests failing" to "100% pass rate with full page coverage and browser verification."

## Usage

```
/e2e-overhaul                     # full 7-phase pipeline
/e2e-overhaul --skip-browser      # skip browser verification phase
/e2e-overhaul --skip-extend       # skip coverage extension (fix only)
/e2e-overhaul --chromium-only     # run only chromium (faster)
/e2e-overhaul --dry-run           # triage only, no fixes
```

## Prerequisites

Before running, ensure:

1. **OrbStack/Docker** running (for PostgreSQL/Redis)
2. **Database** initialized: `make db-up && make db-migrate`
3. **Backend** running on port 4567: `cd backend && source .venv/bin/activate && uvicorn app.main:app --port 4567`
4. **Frontend** running on port 4501: `cd frontend && npm run dev`

## Workflow

### Phase 1: Config
