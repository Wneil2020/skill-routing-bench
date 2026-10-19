---
name: trading-stanley-druckenmiller-investment
description: "Use when Apply Stanley Druckenmiller's investment philosophy for macro positioning, liquidity analysis, and asymmetric risk/reward: covers trading, stanley, druckenmiller, asymmetric, conviction"
metadata:
  holon-triggers: |
    macro positioning
    conviction level
---

---
name: trading-stanley-druckenmiller-investment
description: >-
  Apply Stanley Druckenmiller's investment philosophy for macro positioning, liquidity analysis,
  and asymmetric risk/reward assessment. Use when the user asks about "macro positioning",
  "conviction level", "Druckenmiller analysis", "asymmetric trades", "portfolio conviction",
  "드러큰밀러", "매크로 포지셔닝", "비대칭 리스크", or wants high-conviction macro trade assessment.
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for AlphaEar analysis (use alphaear-deepear-lite).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Druckenmiller Strategy Synthesizer

## Purpose

Synthesize outputs from 8 upstream analysis skills (5 required + 3 optional) into a single composite conviction score (0-100), classify the market into one of 4 Druckenmiller patterns, and generate actionable allocation recommendations. This is a **meta-skill** that consumes structured JSON outputs from other skills — it requires no API keys of its own.

## When to Use This Skill

**English:**
- User asks "What's my overall conviction?" or "How should I be positioned?"
- User wants a unified view synthesizing breadth, uptrend, top risk, macro, and FTD signals
- User asks about Druckenmiller-style portfolio positioning
- User requests strategy synthesis after running individual analysis skills
- User asks "Should I increase or decrease exposure?"
- User wants pattern classification (policy pivot, distortion, contrarian, wait)

**Japanese:**
- 「総合的な市場判断は？」「今のポジショニングは？」
- ブレッドス、アップトレンド、天井リスク、マクロの統合判断
- 「エクスポージャーを増やすべき？減らすべき？」
- 「ドラッケンミラー分析を実行して」
- 個別スキル実行後の戦略統合レポート

---

## Input Requirements

### Required Skills (5)

| # | Skill | JSON Prefix | Role |
|---|-------|-------------|------|
| 1 | Market Breadth Analyzer | `market_breadth_` | Market participation breadth |
| 2 | Uptrend Analyzer | `uptrend_analysis_` | Sector uptrend ratios |
| 3 | Mark
