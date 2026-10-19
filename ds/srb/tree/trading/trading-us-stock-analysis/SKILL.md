---
name: trading-us-stock-analysis
description: "Use when Comprehensive US stock analysis including fundamental analysis (financial metrics, business quality, valuation), technical analysis: covers trading, stock, analysis, aapl, american"
metadata:
  holon-triggers: |
    analyze AAPL
    compare TSLA vs NVDA
---

---
name: trading-us-stock-analysis
description: >-
  Comprehensive US stock analysis including fundamental analysis (financial metrics, business quality, valuation),
  technical analysis (indicators, chart patterns, support/resistance), stock comparisons, and investment report generation.
  Use when the user asks to "analyze AAPL", "compare TSLA vs NVDA", "give me a report on Microsoft", "US stock analysis",
  "미국 주식 분석", "AAPL 재무 분석", "주식 비교", or requests investment recommendations for American stocks.
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

# US Stock Analysis

## Overview

Perform comprehensive analysis of US stocks covering fundamental analysis (financials, business quality, valuation), technical analysis (indicators, trends, patterns), peer comparisons, and generate detailed investment reports. Fetch real-time market data via web search tools and apply structured analytical frameworks.

## Data Sources

Always use web search tools to gather current market data:

**Primary Data to Fetch:**
1. **Current stock price and trading data** (price, volume, 52-week range)
2. **Financial statements** (income statement, balance sheet, cash flow)
3. **Key metrics** (P/E, EPS, revenue, margins, debt ratios)
4. **Analyst ratings and price targets**
5. **Recent news and developments**
6. **Peer/competitor data** (for comparisons)
7. **Technical data** (moving averages, RSI, MACD when available)

**Search Strategy:**
- Use ticker symbol + specific data needed (e.g., "AAPL financial metrics 2024")
- For comprehensive data: Search for earnings reports, investor presentations, or SEC filings
- For technical data: Search for "AAPL technical analysis" or use financial data sites
- Always verify data recenc
