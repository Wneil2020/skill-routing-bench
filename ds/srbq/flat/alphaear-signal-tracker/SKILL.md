---
name: alphaear-signal-tracker
description: "Use when Tracks finance investment signal evolution — determines if signals are Strengthened, Weakened, or Falsified based on new market info. Use when: covers alphaear, signal, tracker, 체크, 리포트"
metadata:
  holon-triggers: |
    monitoring finance signals
    re-evaluating theses after news/price moves
---

---
name: alphaear-signal-tracker
description: >-
  Tracks finance investment signal evolution — determines if signals are
  Strengthened, Weakened, or Falsified based on new market info. Use when
  monitoring finance signals, re-evaluating theses after news/price moves, or
  updating signal confidence and intensity. Do NOT use for one-time stock price
  checks (use daily-stock-check). Do NOT use for generating reports (use
  alphaear-reporter). Do NOT use for sentiment scoring (use alphaear-sentiment).
  Korean triggers: "체크", "리포트", "모니터링", "주식".
metadata:
  version: "1.0.0"
  category: "analysis"
  author: "alphaear"
---
# AlphaEar Signal Tracker

## Overview

Agentic workflow to track how investment signals evolve over time. The agent performs: (1) Research — gather facts using FinResearcher prompt; (2) Analyze — produce `InvestmentSignal` JSON via FinAnalyst prompt; (3) Track — assess evolution (Strengthened/Weakened/Falsified) using Signal Tracking prompt. All prompts live in `references/PROMPTS.md`. Data sources: `alphaear-news`, `alphaear-stock`. Store signals in project PostgreSQL.

## Prerequisites

- Python 3.10+
- `agno` (agent framework), `sqlite3` (built-in)
- Access to `alphaear-search`, `alphaear-stock` skills for data gathering
- `scripts/fin_agent.py` — `FinUtils.sanitize_signal_output` for JSON cleanup
- `DatabaseManager` initialized (PostgreSQL for project signals)

## Workflow

1. **Research**: Use **FinResearcher** prompt from `references/PROMPTS.md` — gather facts, prices, and industry context for the raw signal. Use `alphaear-search` and `alphaear-stock` for data.
2. **Analyze**: Use **FinAnalyst** prompt — transform research into `InvestmentSignal` JSON (`title`, `impact_tickers`, `transmission_chain`, `summary`, etc.).
3. **Sanitize**: Call `FinUtils.sanitize_signal_output(json_data, research_data, raw_signal)` from `scripts/fin_agent.py` to clean ticker bindings.
4. **Track** (for existing signals): Use **Signal Tracking** prompt — compare
