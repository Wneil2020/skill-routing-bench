---
name: trading-options-strategy-advisor
description: "Use when Options trading strategy analysis and simulation tool. Provides Black-Scholes theoretical pricing, Greeks calculation, strategy P/L: covers trading, options, strategy, advisor, black"
metadata:
  holon-triggers: |
    options strategy
    covered call
---

---
name: trading-options-strategy-advisor
description: >-
  Options trading strategy analysis and simulation tool. Provides Black-Scholes theoretical pricing, Greeks calculation, strategy P/L simulation, and risk management guidance. Use when the user asks for "options strategy", "covered call", "protective put", "iron condor", "bull call spread", "options Greeks", "옵션 전략", "커버드콜", "옵션 P/L 분석", "Greeks 계산", or earnings-based options recommendations. Educational focus with practical trade simulation. Do NOT use for stock-only analysis (use trading-us-stock-analysis).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: execution
  source: claude-trading-skills
  api_required: fmp
---

# Options Strategy Advisor

## Overview

Comprehensive options strategy analysis using theoretical pricing. Black-Scholes pricing, Greeks, P/L simulation, earnings strategies, risk management. FMP API for prices/HV; user provides IV from broker when available.

**Core Capabilities:** Black-Scholes pricing, strategy simulation, earnings strategies, risk management, educational focus.

## When to Use

- Options strategy questions ("What's a covered call?", "How does an iron condor work?")
- Strategy P/L simulation ("Max profit on bull call spread?")
- Greeks analysis ("Delta exposure?")
- Earnings strategies ("Straddle before NVDA earnings?")
- Strategy comparison ("Covered call vs protective put?")
- Position sizing, volatility ("Is IV high?")

## Supported Strategies

For full strategy descriptions, see [references/strategies_guide.md](references/strategies_guide.md).

**Summary:** Income (Covered Call, Cash-Secured Put, Poor Man's Covered Call), Protection (Protective Put, Collar), Directional (Bull/Bear Call/Put Spreads), Volatility (Long/Short Straddle/Strangle), Range-Bound (Iron Condor, Iron Butterfly), Advanced (Calendar, Diagonal, Ratio Spread).

## Analysis Workflow

### Step 1: Gather Input

**Required:** Ticker, strategy type, strikes, expiration(s), contracts. **Op
