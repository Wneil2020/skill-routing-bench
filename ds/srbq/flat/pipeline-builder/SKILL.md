---
name: pipeline-builder
description: "Use when Build and manage automated data pipelines using existing Python scripts, GitHub Actions, and cron schedules without writing new: covers pipeline, builder, makefile, repeatable, schedules"
metadata:
  holon-triggers: |
    build a pipeline
    automate this process
---

---
name: pipeline-builder
description: >-
  Build and manage automated data pipelines using existing Python scripts,
  GitHub Actions, and cron schedules without writing new code. Generates YAML
  pipeline definitions, GitHub Actions workflows, script chains, and Makefile
  targets for the stock analytics project. Use when the user asks to "build a
  pipeline", "automate this process", "create a GitHub Action", "chain these
  scripts", "schedule this task", "파이프라인 빌드", "자동화", "스크립트 체인",
  "GitHub Actions 워크플로우 생성", or wants to compose existing scripts into
  repeatable automated pipelines.
  Do NOT use for designing AI-powered analysis workflows (use ai-workflow-integrator).
  Do NOT use for running the existing daily pipeline (use today).
  Do NOT use for CI/CD pipeline review (use sre-devops-expert).
  Do NOT use for deployment or infrastructure (use sre-devops-expert).
metadata:
  author: thaki
  version: 1.0.0
  category: execution
---

# Pipeline Builder

Build automated data pipelines by composing existing Python scripts, Makefile targets, and GitHub Actions workflows. No new code required -- pipelines are defined as YAML configurations or shell script chains.

## Available Scripts

These are the building blocks for pipelines:

| Script | Path | Purpose | Key Args |
|--------|------|---------|----------|
| Weekly stock update | `backend/scripts/weekly_stock_update.py` | Fetch prices from Yahoo Finance | `--status`, `--days N`, `--ticker T` |
| CSV import | `backend/scripts/import_csv.py` | Import CSV files into DB | `PATH --directory` |
| Daily stock check | `backend/scripts/daily_stock_check.py` | Run technical analysis | `--source db`, `--dir DIR`, `--tickers T` |
| Hot stock discovery | `backend/scripts/discover_hot_stocks.py` | Find trending untracked stocks | (none) |
| Report generator | `outputs/generate-report.js` | Generate .docx report | `{date}` |

## Existing Pipelines

Review these before creating new ones to avoid duplication:

| Pipeline | Loca
