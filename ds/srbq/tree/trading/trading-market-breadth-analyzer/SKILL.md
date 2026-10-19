---
name: trading-market-breadth-analyzer
description: "Use when Quantifies market breadth health using TraderMonty's public CSV data. Generates a 0-100 composite score across 6 components (100 =: covers trading, market, breadth, advance, decline"
metadata:
  holon-triggers: |
    is the market rally broad-based
    how healthy is market breadth
---

---
name: trading-market-breadth-analyzer
description: >-
  Quantifies market breadth health using TraderMonty's public CSV data. Generates a 0-100 composite score across 6 components (100 = healthy).
  Use when the user asks "is the market rally broad-based", "how healthy is market breadth", "market participation rate",
  "advance-decline health", "market narrowing", "마켓 브레드스", "시장 참여율", "상승 폭 분석".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for chart-based breadth analysis (use trading-breadth-chart-analyst).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Market Breadth Analyzer Skill

## Purpose

Quantify market breadth health using a data-driven 6-component scoring system (0-100). Uses TraderMonty's publicly available CSV data to measure how broadly the market is participating in a rally or decline.

**Score direction:** 100 = Maximum health (broad participation), 0 = Critical weakness.

**No API key required** - uses freely available CSV data from GitHub Pages.

## When to Use This Skill

**English:**
- User asks "Is the market rally broad-based?" or "How healthy is market breadth?"
- User wants to assess market participation rate
- User asks about advance-decline indicators or breadth thrust
- User wants to know if the market is narrowing (fewer stocks participating)
- User asks about equity exposure levels based on breadth conditions

**Japanese:**
- 「マーケットブレッドスはどうですか？」「市場の参加率は？」
- 「上昇は広がっている？」「一部の銘柄だけの上昇？」
- ブレッドス指標に基づくエクスポージャー判断
- 市場の健康度をデータで確認したい

## Difference from Breadth Chart Analyst

| Aspect | Market Breadth Analyzer | Breadth Chart Analyst |
|--------|------------------------|----------------------|
| Data Source | CSV (automated) | Chart images (manual) |
| API Required | None | None |
| Output | Quantitative 0-100 score | Qualitative chart analysis |
| Components | 6 scored dimensions | Visual pattern recognition |
| Repeatability | Fu
