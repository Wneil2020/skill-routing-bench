---
name: ai-workflow-integrator
description: "Use when Design and orchestrate AI-powered stock analysis workflows that chain data ingestion, LLM analysis, report generation, and Slack: covers integrator, ingestion, seamless, stages, composition"
metadata:
  holon-triggers: |
    design an AI workflow
    build an analysis pipeline
---

---
name: ai-workflow-integrator
description: >-
  Design and orchestrate AI-powered stock analysis workflows that chain data
  ingestion, LLM analysis, report generation, and Slack distribution into
  seamless multi-stage pipelines. Supports daily, weekly, and event-driven
  workflow templates with stage composition, error recovery, and parallel
  execution. Use when the user asks to "design an AI workflow", "build an
  analysis pipeline", "orchestrate stock analysis", "chain analysis stages",
  "AI workflow", "워크플로우 설계", "분석 파이프라인", or wants to compose
  existing skills into a new multi-stage pipeline.
  Do NOT use for running the existing daily pipeline (use today).
  Do NOT use for single-domain stock analysis (use daily-stock-check).
  Do NOT use for orchestrating non-stock multi-skill tasks (use mission-control).
  Do NOT use for building GitHub Actions or cron jobs (use pipeline-builder).
metadata:
  author: thaki
  version: 1.0.0
  category: generation
---

# AI Workflow Integrator

Design and orchestrate AI-powered stock analysis workflows by composing existing skills and scripts into multi-stage pipelines. Each workflow defines stages, data flow between stages, error handling, and output targets.

## Core Concepts

### Workflow Anatomy

A workflow consists of ordered stages, each backed by a skill or script:

```
[Data Source] → [Transform] → [AI Analysis] → [Quality Gate] → [Output]
```

Every stage has:
- **Input**: Data from a previous stage or external source
- **Processor**: A skill, script, or LLM call
- **Output**: Structured data passed to the next stage
- **Error handler**: Retry, skip, or abort behavior

### Available Building Blocks

| Block | Type | Source |
|-------|------|--------|
| DB status check | Script | `backend/scripts/weekly_stock_update.py --status` |
| Yahoo Finance sync | Script | `backend/scripts/weekly_stock_update.py --days N` |
| CSV import | Script | `backend/scripts/import_csv.py` |
| Hot stock discovery | Script | `backend/
