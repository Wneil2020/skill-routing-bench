---
name: deep-research-pipeline
description: "Use when End-to-end research pipeline, deep web research (parallel-deep-research), 12-role cross-perspective analysis (role-dispatcher), and: covers deep, research, pipeline, 딥 리서치 파이프라인, 종합 리서치"
metadata:
  holon-triggers: |
    deep research pipeline
    research and analyze
---

---
name: deep-research-pipeline
description: >-
  End-to-end research pipeline: deep web research (parallel-deep-research),
  12-role cross-perspective analysis (role-dispatcher), and Notion publishing
  (md-to-notion) in a single sequential workflow. Produces research reports,
  executive briefings, and structured Notion pages from any business or
  technology topic. Use when the user asks to "deep research pipeline",
  "research and analyze", "deep research to notion", "딥 리서치 파이프라인",
  "종합 리서치", "리서치 후 종합 분석", or wants end-to-end research with
  multi-perspective analysis and Notion delivery.
  Do NOT use for deep research only (use parallel-deep-research), role
  dispatch without research (use role-dispatcher), or publishing existing
  files to Notion (use md-to-notion).
  Korean triggers: "딥 리서치 파이프라인", "종합 리서치", "리서치 분석 노션".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "orchestration"
  composes:
    - parallel-deep-research
    - role-dispatcher
    - md-to-notion
---

# Deep Research Pipeline

Sequential 3-stage pipeline: deep web research, 12-role cross-perspective
analysis with CEO executive briefing, and Notion publishing.

```
Stage 1: Deep Research     → parallel-deep-research → {topic}.md
Stage 2: Role Dispatcher   → role-dispatcher        → role analyses + executive briefing
Stage 3: Notion Publish    → md-to-notion           → structured Notion pages
```

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `<topic>` | Yes | Research topic in natural language |
| `--parent <id>` | No | Notion parent page ID. Defaults to `3239eddc34e680e8a7a5d5b5eac18b38` (AI 자동 정리) |
| `--roles <list>` | No | Whitelist roles for dispatcher (e.g., `cto,pm,cso`) |
| `--skip <list>` | No | Blacklist roles (e.g., `hr,finance`) |
| `--processor <tier>` | No | parallel-cli processor tier: `pro-fast` (default), `ultra-fast`, `ultra` |

## Stage 1: Deep Research

Run `parallel-deep-research` to produce a comprehensive resear
