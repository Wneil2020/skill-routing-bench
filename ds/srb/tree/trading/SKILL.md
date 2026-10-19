---
name: trading
description: "Use when the request concerns the trading category of skills: covers trading"
---

Grouping node for the 0 skills of the trading category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **trading-backtest-expert** (`trading-backtest-expert/`): Use when Expert guidance for systematic backtesting of trading strategies. Use when developing, testing, stress-testing, or validating quantitative: covers trading, backtest, expert, beating, death
- **trading-breadth-chart-analyst** (`trading-breadth-chart-analyst/`): Use when Analyzes market breadth charts, S&P 500 Breadth Index (200-Day MA) and US Stock Market Uptrend Stock Ratio. Use when the user asks for: covers trading, breadth, chart, tactical, outlook
- **trading-data-quality-checker** (`trading-data-quality-checker/`): Use when Validate data quality in market analysis documents and blog articles before publication. Use when the user asks to "check data quality": covers trading, data, quality, advisory, etf
- **trading-edge-candidate-agent** (`trading-edge-candidate-agent/`): Use when Generate and prioritize US equity long-side edge research tickets from EOD observations, then export pipeline-ready candidate specs for: covers trading, edge, candidate, finder, observations
- **trading-finviz-screener** (`trading-finviz-screener/`): Use when Build and open FinViz screener URLs from natural language requests. Use when the user asks to "screen stocks", "find stocks matching criteria": covers trading, finviz, screener, caps, roe
- **trading-market-breadth-analyzer** (`trading-market-breadth-analyzer/`): Use when Quantifies market breadth health using TraderMonty's public CSV data. Generates a 0-100 composite score across 6 components (100 =: covers trading, market, breadth, advance, decline
- **trading-market-environment-analysis** (`trading-market-environment-analysis/`): Use when Comprehensive market environment analysis and reporting. Analyzes global markets, US, European, Asian, forex, commodities, economic indicators: covers trading, market, environment, 시장, 분석
- **trading-market-news-analyst** (`trading-market-news-analyst/`): Use when Analyze recent market-moving news events and their impact on equity markets and commodities. Use when the user asks to "analyze market news", "FOMC: covers trading, market, news, cap, fomc
- **trading-market-top-detector** (`trading-market-top-detector/`): Use when Detects market top probability using O'Neil Distribution Days, Minervini Leading Stock Deterioration, and Monty Defensive Sector: covers trading, market, top, breakdown, deterioration
- **trading-options-strategy-advisor** (`trading-options-strategy-advisor/`): Use when Options trading strategy analysis and simulation tool. Provides Black-Scholes theoretical pricing, Greeks calculation, strategy P/L: covers trading, options, strategy, advisor, black
- **trading-options-theta** (`trading-options-theta/`): Use when Run professional-grade options theta trading analysis using 12 quant-firm-style prompts covering 0DTE credit spreads, market regime: covers trading, options, theta, buying, condors
- **trading-position-sizer** (`trading-position-sizer/`): Use when Calculate risk-based position sizes for long stock trades using Fixed Fractional, ATR-Based, or Kelly Criterion methods. Supports: covers trading, position, sizer, atr, concentration
- **trading-scenario-analyzer** (`trading-scenario-analyzer/`): Use when Analyze news headlines for 18-month investment scenarios. Orchestrates scenario-analyst (main analysis) and strategy-reviewer (second: covers trading, scenario, analyzer, headlines, impacts
- **trading-sector-analyst** (`trading-sector-analyst/`): Use when Analyzes sector rotation patterns and market cycle positioning using TraderMonty's public CSV uptrend data. Use when the user asks to: covers trading, sector, analyst, cyclical, overbought
- **trading-stanley-druckenmiller-investment** (`trading-stanley-druckenmiller-investment/`): Use when Apply Stanley Druckenmiller's investment philosophy for macro positioning, liquidity analysis, and asymmetric risk/reward: covers trading, stanley, druckenmiller, asymmetric, conviction
- **trading-technical-analyst** (`trading-technical-analyst/`): Use when Analyze weekly price charts for stocks, indices, cryptocurrencies, or forex pairs. Use when the user provides chart images and: covers trading, technical, analyst, cryptocurrencies, indices
- **trading-theme-detector** (`trading-theme-detector/`): Use when Detects and ranks trending market themes across sectors using cross-sector momentum, volume, and breadth signals. Use when the user asks: covers trading, theme, detector, bearish, bullish
- **trading-trade-hypothesis-ideator** (`trading-trade-hypothesis-ideator/`): Use when Generate falsifiable trade strategy hypotheses from market data, trade logs, and journal snippets. Use when the user asks to: covers trading, trade, hypothesis, falsifiable, ideator
- **trading-uptrend-analyzer** (`trading-uptrend-analyzer/`): Use when Analyzes market breadth using Monty's Uptrend Ratio Dashboard to diagnose market environment. Generates 0-100 composite score from 5: covers trading, uptrend, analyzer, ratios, healthy
- **trading-us-market-bubble-detector** (`trading-us-market-bubble-detector/`): Use when Evaluates market bubble risk through quantitative data-driven analysis using the Minsky/Kindleberger framework v2.1. Prioritizes: covers trading, market, bubble, evaluates, impressions
- **trading-us-stock-analysis** (`trading-us-stock-analysis/`): Use when Comprehensive US stock analysis including fundamental analysis (financial metrics, business quality, valuation), technical analysis: covers trading, stock, analysis, aapl, american

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
