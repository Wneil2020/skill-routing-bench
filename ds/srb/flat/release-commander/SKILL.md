---
name: release-commander
description: "Use when Full release lifecycle orchestrator that chains 10 existing skills into a single pipeline, code review, security scan, test validation: covers release, commander, changelog, i18n, split"
metadata:
  holon-triggers: |
    prepare release
    release pipeline
---

---
name: release-commander
description: >-
  Full release lifecycle orchestrator that chains 10 existing skills into a
  single pipeline: code review, security scan, test validation, performance
  check, i18n sync, dependency audit, changelog generation, domain-split
  commits, PR summary, and PR creation. Use when the user asks to "prepare
  release", "release pipeline", "full release check", "release commander",
  "릴리즈", "릴리즈 준비", or wants a comprehensive pre-release validation. Do NOT use
  for code review only (use deep-review or simplify), commit only (use
  domain-commit), PR only (use ship), or individual checks (use the specific
  skill directly).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Release Commander — Full Release Lifecycle Pipeline

One command to take code from "feature complete" to "release-ready PR" with comprehensive validation. Orchestrates 10 specialized skills across 4 sequential groups.

## Usage

```
/release-commander                              # full pipeline
/release-commander --skip security,i18n         # skip specific checks
/release-commander --dry-run                    # validation only, no commits/PR
/release-commander --base release-v1.2          # specify PR base branch
/release-commander --changelog-only             # generate changelog from recent commits
```

## Pipeline Overview

```
Group A (parallel): Review
  ├─ deep-review       → Full-stack code review (4 agents)
  ├─ security-expert   → Threat model + vulnerability scan
  └─ performance-profiler → Latency, queries, bundle size

    ↓ Gate: all reviews pass or findings are Low/Medium only

Group B (parallel): Validate
  ├─ test-suite        → Run tests, generate missing, fix failures
  ├─ i18n-sync         → Translation key completeness
  └─ dependency-auditor → CVE scan, outdated packages

    ↓ Gate: tests pass, no critical CVEs, translations complete

Group C (sequential): Package
  ├─ technical-writer  → Generate CHANGELOG entry

