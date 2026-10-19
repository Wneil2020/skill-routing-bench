---
name: role-trading-expert
description: "Use when Analyze a given topic from the Trading Expert perspective — market environment impact, technical analysis, strategy validation, risk: covers role, trading, expert, 트레이딩 전문가 관점, 매매 전문가 분석"
metadata:
  holon-triggers: |
    trading expert perspective
    트레이딩 전문가 관점
---

---
name: role-trading-expert
description: >
  Analyze a given topic from the Trading Expert perspective — market environment impact, technical
  analysis, strategy validation, risk management, and sentiment assessment. Scores topic relevance
  (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes daily-stock-check, trading-technical-analyst, trading-market-environment-analysis,
  trading-backtest-expert, trading-position-sizer, trading-scenario-analyzer, alphaear-deepear-lite,
  trading-us-stock-analysis, alphaear-sentiment, alphaear-news, workflow-miner, semantic-guard,
  and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "trading expert perspective", "트레이딩 전문가 관점", "매매 전문가 분석", "trading impact analysis".
  Do NOT use for running daily stock checks directly (use daily-stock-check),
  backtesting execution (use trading-backtest-expert), or weekly price updates (use weekly-stock-update).
  Korean triggers: "트레이딩 전문가 관점", "매매 전문가 분석", "트레이딩 영향 분석".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "role-analysis"
---

# Trading Expert Perspective Analyzer

Analyzes any business topic from the Trading Expert's viewpoint, covering market environment impact,
technical analysis, fundamental valuation, strategy validation, risk management, scenario planning,
sentiment analysis, and news-driven signal assessment.

## Relevance Criteria

Score the topic 1-10 based on overlap with trading concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Technical analysis | High | chart, SMA, RSI, MACD, Bollinger, Donchian, breakout, support, resistance |
| Market environment | High | macro, FOMC, rate, volatility, VIX, risk-on, risk-off, correlation |
| Trading strategy | High | Turtle, momentum, mean-reversion, backtest, signal, entry, exit |
| Risk management | High | position size, stop-loss, drawdown, Kelly, ATR, risk/reward |
| Fundamental analy
