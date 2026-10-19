---
name: hf-trending-intelligence
description: "Use when Autonomous daily intelligence pipeline that cross-references HF papers, models, datasets, and community activity to detect: covers trending, intelligence, browsing, mainstream, ecosystem"
metadata:
  holon-triggers: |
    run daily AI radar
    trending intelligence
---

---
name: hf-trending-intelligence
description: >-
  Autonomous daily intelligence pipeline that cross-references HF papers,
  models, datasets, and community activity to detect emerging AI trends before
  they go mainstream. Produces a scored intelligence report and distributes to
  Slack + Notion. Use when the user asks to "run daily AI radar", "trending
  intelligence", "AI research radar", "detect AI trends", "daily paper
  intelligence", "AI 트렌드 레이더", "일일 AI 인텔리전스", "트렌딩 분석",
  "연구 레이더", or wants to know what's trending across the HF ecosystem today.
  Do NOT use for full paper review with PM analysis (use paper-review).
  Do NOT use for daily stock analysis (use today).
  Do NOT use for general web research only (use parallel-web-search).
  Do NOT use for paper browsing without cross-referencing (use hf-papers).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "research"
---

# Trending Intelligence — Daily AI Research Radar

Autonomous daily pipeline that detects emerging AI trends by cross-referencing
papers, models, datasets, and community buzz on Hugging Face Hub.

## Prerequisites

- `hf` CLI installed and authenticated (see `hf-hub` skill)
- Slack MCP configured for posting (channel: `#deep-research` — `C0A6X68LTN1`)
- Notion MCP configured for page creation
- `jq` for JSON processing

## Required Skills

- `hf-papers` — daily paper listing
- `hf-models` — model search and info
- `hf-collections` — curate trending items
- `hf-discussions` — measure community activity
- `hf-dataset-viewer` — dataset info
- `parallel-web-search` — external signal enrichment
- `md-to-notion` — permanent Notion archive
- `kwp-slack-slack-messaging` — Slack distribution

## Reference Files

- `references/scoring-rubric.md` — composite scoring weights and thresholds
- `references/report-template.md` — intelligence report markdown template
- `references/collection-naming.md` — naming convention for monthly collections

## Input

- **Date** (optional): Defaults to `tod
