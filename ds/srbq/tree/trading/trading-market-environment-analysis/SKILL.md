---
name: trading-market-environment-analysis
description: "Use when Comprehensive market environment analysis and reporting. Analyzes global markets, US, European, Asian, forex, commodities, economic indicators: covers trading, market, environment, 시장, 분석"
metadata:
  holon-triggers: |
    market analysis
    market environment
---

---
name: trading-market-environment-analysis
description: >-
  Comprehensive market environment analysis and reporting. Analyzes global
  markets: US, European, Asian, forex, commodities, economic indicators. Use
  when the user asks "market analysis", "market environment", "global markets",
  "trading environment", "risk-on risk-off", "market conditions", "investment
  climate", "market sentiment", "相場環境", "市場分析", "マーケット状況", "投資環境". Do NOT use
  for daily stock signals (use daily-stock-check). Do NOT use for AlphaEar news
  aggregation (use alphaear-news). Korean triggers: "시장", "분석", "체크", "리포트".
metadata:
  author: "tradermonty"
  version: "1.0.0"
  category: "analysis"
  source: "claude-trading-skills"
  api_required: "none"
---
# Market Environment Analysis

Comprehensive analysis tool for understanding market conditions and creating professional market reports anytime.

## Core Workflow

### 1. Initial Data Collection
Collect latest market data using web_search tool:
1. Major stock indices (S&P 500, NASDAQ, Dow, Nikkei 225, Shanghai Composite, Hang Seng)
2. Forex rates (USD/JPY, EUR/USD, major currency pairs)
3. Commodity prices (WTI crude, Gold, Silver)
4. US Treasury yields (2-year, 10-year, 30-year)
5. VIX index (Fear gauge)
6. Market trading status (open/close/current values)

### 2. Market Environment Assessment
Evaluate the following from collected data:
- **Trend Direction**: Uptrend/Downtrend/Range-bound
- **Risk Sentiment**: Risk-on/Risk-off
- **Volatility Status**: Market anxiety level from VIX
- **Sector Rotation**: Where capital is flowing

### 3. Report Structure

#### Standard Report Format:
```
1. Executive Summary (3-5 key points)
2. Global Market Overview
   - US Markets
   - Asian Markets
   - European Markets
3. Forex & Commodities Trends
4. Key Events & Economic Indicators
5. Risk Factor Analysis
6. Investment Strategy Implications
```

## Script Usage

### market_utils.py
Provides common functions for report creation:
```bash
# Generate r
