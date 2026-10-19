---
name: trading-backtest-expert
description: "Use when Expert guidance for systematic backtesting of trading strategies. Use when developing, testing, stress-testing, or validating quantitative: covers trading, backtest, expert, beating, death"
metadata:
  holon-triggers: |
    beating ideas to death
    backtesting
---

---
name: trading-backtest-expert
description: >-
  Expert guidance for systematic backtesting of trading strategies. Use when developing, testing,
  stress-testing, or validating quantitative trading strategies. Covers "beating ideas to death" methodology,
  parameter robustness testing, slippage modeling, bias prevention, and interpreting backtest results.
  Use for "backtesting", "strategy validation", "로버스트니스 테스트", "백테스트", "전략 검증", "과적합 방지".
  Do NOT use for daily stock signals (use daily-stock-check).
  Do NOT use for AlphaEar analysis (use alphaear-deepear-lite).
  Do NOT use for weekly price updates (use weekly-stock-update).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Backtest Expert

Systematic approach to backtesting trading strategies based on professional methodology that prioritizes robustness over optimistic results.

## Core Philosophy

**Goal**: Find strategies that "break the least", not strategies that "profit the most" on paper.

**Principle**: Add friction, stress test assumptions, and see what survives. If a strategy holds up under pessimistic conditions, it's more likely to work in live trading.

## When to Use This Skill

Use this skill when:
- Developing or validating systematic trading strategies
- Evaluating whether a trading idea is robust enough for live implementation
- Troubleshooting why a backtest might be misleading
- Learning proper backtesting methodology
- Avoiding common pitfalls (curve-fitting, look-ahead bias, survivorship bias)
- Assessing parameter sensitivity and regime dependence
- Setting realistic expectations for slippage and execution costs

## Prerequisites

- Python 3.9+ (for evaluation script)
- No API keys required
- No external data dependencies — metrics are user-provided

## Workflow

### 1. State the Hypothesis

Define the edge in one sentence.

**Example**: "Stocks that gap up >3% on earnings and pull back to previous day's 
