---
name: incident-to-improvement
description: "Use when Close the loop from production incident to lasting prevention. Orchestrates 7 existing skills in a pipeline, incident triage, root: covers incident, improvement, blameless, closed, lasting"
metadata:
  holon-triggers: |
    incident
    post-mortem
---

---
name: incident-to-improvement
description: >-
  Close the loop from production incident to lasting prevention. Orchestrates 7
  existing skills in a pipeline: incident triage, root cause analysis, code fix
  with regression tests, knowledge base article, monitoring recommendations, and
  blameless post-mortem document. Ensures every incident produces lasting
  improvements. Use when the user reports an "incident", "post-mortem",
  "production issue", "outage", "인시던트", "장애 대응", "장애 복구", "incident to
  improvement", or wants to run the full incident response lifecycle. Do NOT use
  for non-incident debugging (use diagnose), code review (use deep-review), or
  monitoring setup only (use sre-devops-expert).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Incident to Improvement — Closed-Loop Incident Response

Every incident is a gift — if you learn from it. This skill ensures that production incidents don't just get fixed, they produce regression tests, knowledge base articles, monitoring improvements, and blameless post-mortems.

## Usage

```
/incident-to-improvement "500 errors on /api/users since 14:00"
/incident-to-improvement --severity P1 "Database connection pool exhaustion"
/incident-to-improvement --phase triage       # triage only
/incident-to-improvement --phase fix          # skip to fix (triage already done)
/incident-to-improvement --phase post-mortem  # generate post-mortem from resolved incident
/incident-to-improvement --no-fix             # analysis + post-mortem only, no code changes
```

## Pipeline Overview

```
Group A (parallel): Respond
  ├─ kwp-engineering-incident-response → Severity classification, impact assessment
  └─ diagnose                          → Root cause analysis (3 parallel agents)

    ↓ Gate: root cause identified with medium+ confidence

Group B (sequential): Fix and Test
  ├─ generalPurpose agent              → Apply the fix
  └─ test-suite                        → Generate regression tests,
