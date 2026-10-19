---
name: trading-breadth-chart-analyst
description: "Use when Analyzes market breadth charts, S&P 500 Breadth Index (200-Day MA) and US Stock Market Uptrend Stock Ratio. Use when the user asks for: covers trading, breadth, chart, tactical, outlook"
metadata:
  holon-triggers: |
    market breadth assessment
    breadth chart analysis
---

---
name: trading-breadth-chart-analyst
description: >-
  Analyzes market breadth charts: S&P 500 Breadth Index (200-Day MA) and US Stock Market Uptrend Stock Ratio.
  Use when the user asks for "market breadth assessment", "breadth chart analysis", "positioning strategy",
  "strategic tactical market outlook", "마켓 브레드스", "차트 분석", "포지셔닝 전략".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for AlphaEar news aggregation (use alphaear-news).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Breadth Chart Analyst

## Overview

This skill enables specialized analysis of two complementary market breadth charts that provide strategic (medium to long-term) and tactical (short-term) market perspectives. Analyze breadth chart images to assess market health, identify trading signals based on backtested strategies, and develop positioning recommendations. All thinking and output are conducted exclusively in English.

## When to Use

Use this skill when:
- User provides S&P 500 Breadth Index (200-Day MA based) chart images for analysis
- User provides US Stock Market Uptrend Stock Ratio chart images for analysis
- User requests market breadth assessment or market health evaluation
- User asks about medium-term strategic positioning based on breadth indicators
- User needs short-term tactical timing signals for swing trading
- User wants combined strategic and tactical market outlook

Do NOT use this skill when:
- User asks about individual stock analysis (use `us-stock-analysis` skill instead)
- User needs sector rotation analysis without breadth charts (use `trading-sector-analyst` skill instead)
- User wants news-based market analysis (use `alphaear-news` skill instead)

## Prerequisites

- **Chart Images Required**: User must provide one or both breadth chart images:
  - Chart 1: S&P 500 Breadth Index (200-Day MA based)
  - Chart 2: US Stock Market Uptrend Stock Ratio
- 
