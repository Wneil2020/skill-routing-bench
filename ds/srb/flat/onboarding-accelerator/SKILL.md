---
name: onboarding-accelerator
description: "Use when Generate a complete \"new developer kit\" by orchestrating 8 existing skills, architecture analysis, code ownership maps, interactive: covers onboarding, accelerator, joining, getting, member"
metadata:
  holon-triggers: |
    onboarding
    new developer
---

---
name: onboarding-accelerator
description: >-
  Generate a complete "new developer kit" by orchestrating 8 existing skills:
  architecture analysis, code ownership maps, interactive diagrams, study
  materials, getting-started guides, environment setup docs, and infrastructure
  overview. Produces a comprehensive onboarding package in docs/onboarding/. Use
  when the user asks about "onboarding", "new developer", "onboard", "getting
  started kit", "온보딩", "신규 개발자", "new team member", "developer onboarding", or
  wants to create documentation for someone joining the project. Do NOT use for
  code review (use deep-review), running the dev environment (use
  local-dev-runner), or creating study quizzes only (use docs-tutor).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Onboarding Accelerator — New Developer Kit Generator

Turn weeks of onboarding into hours. Automatically generates a comprehensive onboarding package by analyzing the codebase and orchestrating 8 specialized skills.

## Usage

```
/onboarding-accelerator                        # full onboarding kit
/onboarding-accelerator --role frontend        # frontend-focused kit
/onboarding-accelerator --role backend         # backend-focused kit
/onboarding-accelerator --role fullstack       # everything (default)
/onboarding-accelerator --section architecture # specific section only
/onboarding-accelerator --output docs/onboarding/  # custom output path
```

## Pipeline Overview

```
Group A (parallel): Analyze
  ├─ deep-review          → Architecture scan, component boundaries, patterns
  └─ codebase-archaeologist → Code ownership, bus factor, churn hotspots

    ↓

Group B (parallel): Visualize
  ├─ visual-explainer     → Interactive architecture diagrams
  └─ design-architect     → Design system overview, UI patterns

    ↓

Group C (parallel): Document
  ├─ technical-writer     → Getting started guide, conventions doc
  └─ docs-tutor-setup     → StudyVault with concept notes 
