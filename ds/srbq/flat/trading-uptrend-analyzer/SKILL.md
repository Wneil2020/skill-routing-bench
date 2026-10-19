---
name: trading-uptrend-analyzer
description: "Use when Analyzes market breadth using Monty's Uptrend Ratio Dashboard to diagnose market environment. Generates 0-100 composite score from 5: covers trading, uptrend, analyzer, ratios, healthy"
metadata:
  holon-triggers: |
    market breadth healthy
    how broad is the rally
---

---
name: trading-uptrend-analyzer
description: >-
  Analyzes market breadth using Monty's Uptrend Ratio Dashboard to diagnose market environment. Generates 0-100 composite score from 5 components.
  Use when the user asks "market breadth healthy", "how broad is the rally", "uptrend ratios", "market participation",
  "exposure guidance based on breadth", "마켓 브레드스", "업트렌드 비율", "시장 참여도".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for market top risk assessment (use trading-market-top-detector).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Uptrend Analyzer Skill

## Purpose

Diagnose market breadth health using Monty's Uptrend Ratio Dashboard, which tracks ~2,800 US stocks across 11 sectors. Generates a 0-100 composite score (higher = healthier) with exposure guidance.

Unlike the Market Top Detector (API-based risk scorer), this skill uses free CSV data to assess "participation breadth" - whether the market's advance is broad or narrow.

## When to Use This Skill

**English:**
- User asks "Is the market breadth healthy?" or "How broad is the rally?"
- User wants to assess uptrend ratios across sectors
- User asks about market participation or breadth conditions
- User needs exposure guidance based on breadth analysis
- User references Monty's Uptrend Dashboard or uptrend ratios

**Japanese:**
- 「市場のブレドスは健全？」「上昇の裾野は広い？」
- セクター別のアップトレンド比率を確認したい
- 相場参加率・ブレドス状況を診断したい
- ブレドス分析に基づくエクスポージャーガイダンスが欲しい
- Montyのアップトレンドダッシュボードについて質問

## Difference from Market Top Detector

| Aspect | Uptrend Analyzer | Market Top Detector |
|--------|-----------------|-------------------|
| Score Direction | Higher = healthier | Higher = riskier |
| Data Source | Free GitHub CSV | FMP API (paid) |
| Focus | Breadth participation | Top formation risk |
| API Key | Not required | Required (FMP) |
| Methodology | Monty Uptrend Ratios | O'Neil/Minervini/Monty |

---

## Execution Workf
