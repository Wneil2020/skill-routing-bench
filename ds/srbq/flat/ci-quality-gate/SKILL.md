---
name: ci-quality-gate
description: "Use when Run the full CI pipeline locally (secret scan, Python lint/test, Go lint/test, frontend lint/test/build, schema check) and produce a pass/fail report: covers quality, gate, 감사, 테스트, pushing"
metadata:
  holon-triggers: |
    run CI locally
    check quality before pushing
---

---
name: ci-quality-gate
description: >-
  Run the full CI pipeline locally (secret scan, Python lint/test, Go
  lint/test, frontend lint/test/build, schema check) and produce a pass/fail
  report. Use when the user asks to run CI locally, check quality before
  pushing, or validate all checks pass. Do NOT use for individual dependency
  audits (use dependency-auditor) or test strategy design (use qa-test-expert).
  Korean triggers: "감사", "테스트", "빌드", "설계".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# CI Quality Gate

Reproduces the GitHub Actions CI pipeline (`.github/workflows/ci.yml`) on the local machine and aggregates results into a single pass/fail report.

## When to Use

- Before pushing commits to verify CI will pass
- After large refactors to catch regressions across stacks
- As part of the `/full-quality-audit` workflow (called by mission-control)

## Prerequisites

Requires Python 3.11+, ruff, black, mypy, Go 1.22+, Node 20+, and gitleaks. Missing tools are marked as `SKIPPED` in the report.

## Execution Steps

Run 8 sequential gates: Secret Scan, Python Lint/Type/Security, Python Tests, Go Build/Test, Frontend Lint/Type/Test/Build, and Schema Check. For detailed commands and per-gate instructions, see [references/execution-steps.md](references/execution-steps.md).

### Step 8: Aggregate Report

Combine all results into a structured report.

## Examples

### Example 1: Pre-push validation
User says: "Run CI checks before I push"
Actions:
1. Execute all 8 gates sequentially (secret scan through schema check)
2. Collect pass/fail/skip status for each gate
3. Generate aggregated report
Result: CI Quality Gate Report showing all gates with pass/fail status

### Example 2: Auto-fix mode
User says: "Run CI and fix what you can"
Actions:
1. Run all gates to identify failures
2. Apply auto-fixes (ruff --fix, black, eslint --fix)
3. Re-run affected gates
Result: Updated report showing fixed items and remaining issues

## Troubles
