---
name: critical-review
description: "Use when End-to-end CTO/CEO critical review and remediation pipeline, parallel technical and strategic critiques (4 review sections x 4 issues: covers critical, review, critiques, dual, remediation"
metadata:
  holon-triggers: |
    critical review
    CTO CEO review
---

---
name: critical-review
description: >-
  End-to-end CTO/CEO critical review and remediation pipeline: parallel
  technical and strategic critiques (4 review sections x 4 issues each),
  PM documentation (PRD, OKRs, Lean Canvas, SWOT), 3-sprint remediation
  execution, and executive summary .docx generation. Use when the user
  asks to "critical review", "CTO CEO review", "platform review",
  "run critical review", "critical-review", "CTO 리뷰", "CEO 리뷰",
  "신랄한 비판", "플랫폼 리뷰", "전체 리뷰 후 개선", or wants a comprehensive
  dual-perspective project audit with remediation. Do NOT use for
  single-domain code review (use deep-review or simplify), release
  preparation (use release-commander), daily stock analysis (use today),
  or role-dispatch without remediation (use role-dispatcher).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Critical Review — CTO/CEO Dual-Perspective Audit and Remediation Pipeline

One command to produce brutally honest CTO and CEO critiques of the entire project, generate PM strategy documents from the findings, execute a prioritized 3-sprint remediation, and deliver a professional executive summary. Orchestrates 12+ specialized skills across 4 sequential phases.

## Usage

```
/critical-review                      # full pipeline (all 4 phases)
/critical-review review-only          # Phase 1 only — CTO + CEO reviews
/critical-review with-implementation  # Phases 1-3 — reviews + PM docs + sprints
/critical-review docs-only            # Phase 4 only — generate docs from existing reviews
```

## Pipeline Overview

```
Phase 1 (parallel): Critical Reviews
  ├─ role-cto    → Architecture, Code Quality, Tests, Performance (4 issues each)
  └─ role-ceo    → Product-Market Fit, Business Model, UX Quality, Differentiation

    ↓ Output: cto-review-{YYYY-MM}.md + ceo-review-{YYYY-MM}.md

Phase 2 (sequential): PM Document Generation
  ├─ pm-execution       → PRD + OKRs + Sprint Plan
  └─ pm-product-strategy → Lean Canvas + SWOT +
