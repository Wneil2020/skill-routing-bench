---
name: trading-sector-analyst
description: "Use when Analyzes sector rotation patterns and market cycle positioning using TraderMonty's public CSV uptrend data. Use when the user asks to: covers trading, sector, analyst, cyclical, overbought"
metadata:
  holon-triggers: |
    run sector rotation analysis
    which sectors are leading
---

---
name: trading-sector-analyst
description: >-
  Analyzes sector rotation patterns and market cycle positioning using TraderMonty's public CSV uptrend data.
  Use when the user asks to "run sector rotation analysis", "which sectors are leading", "cyclical vs defensive",
  "sectors overbought oversold", "market cycle phase", "섹터 로테이션", "시장 사이클", "과매수 과매도 섹터".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for weekly price updates (use weekly-stock-update).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Sector Analyst

## Overview

This skill enables comprehensive analysis of sector rotation and market cycle positioning by fetching uptrend ratio data from TraderMonty's public CSV dataset. It ranks sectors, calculates cyclical vs defensive risk regime scores, identifies overbought/oversold conditions, and estimates the current market cycle phase. Chart images can optionally supplement the data-driven analysis with industry-level detail.

## When to Use This Skill

Use this skill when:
- User requests sector rotation analysis (no chart images required)
- User asks about cyclical vs defensive positioning
- User wants to know which sectors are overbought or oversold
- User requests market cycle phase estimation
- User provides sector performance charts for supplementary analysis
- User asks for sector-based scenario analysis or predictions

Example user requests:
- "Run a sector rotation analysis"
- "Which sectors are leading — cyclical or defensive?"
- "Are any sectors overbought right now?"
- "What phase of the market cycle are we in?"
- "Analyze these sector performance charts and tell me where we are in the market cycle"

## Data Source

Sector uptrend ratios are fetched from TraderMonty's public GitHub repository (no API key required):
- **Sector Summary**: `sector_summary.csv` — uptrend ratio, trend, slope, and status per sector
- **Freshness Check**: `up
