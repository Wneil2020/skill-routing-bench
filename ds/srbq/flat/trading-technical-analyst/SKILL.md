---
name: trading-technical-analyst
description: "Use when Analyze weekly price charts for stocks, indices, cryptocurrencies, or forex pairs. Use when the user provides chart images and: covers trading, technical, analyst, cryptocurrencies, indices"
metadata:
  holon-triggers: |
    technical analysis
    chart analysis
---

---
name: trading-technical-analyst
description: >-
  Analyze weekly price charts for stocks, indices, cryptocurrencies, or forex pairs.
  Use when the user provides chart images and requests technical analysis, trend identification,
  support/resistance levels, scenario planning, or probability assessments based purely on chart data.
  Use for "technical analysis", "chart analysis", "지주 분석", "추세 분석", "지지/저항", "시나리오 분석".
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

# Technical Analyst

## Overview

This skill enables comprehensive technical analysis of weekly price charts. Analyze chart images to identify trends, support and resistance levels, moving average relationships, volume patterns, and develop probabilistic scenarios for future price movement. All analysis is conducted objectively using only chart data, without influence from news, fundamentals, or market sentiment.

## Core Principles

1. **Pure Chart Analysis**: Base all conclusions exclusively on technical data visible in the chart
2. **Systematic Approach**: Follow a structured methodology for each chart analysis
3. **Objective Assessment**: Avoid subjective bias; focus on observable patterns and data
4. **Probabilistic Scenarios**: Express future possibilities as probability-weighted scenarios
5. **Sequential Processing**: Analyze each chart individually and document findings immediately

## Analysis Workflow

### Step 1: Receive Chart Images

When the user provides one or more weekly chart images for analysis:

1. Confirm receipt of all chart images
2. Identify the number of charts to analyze
3. Note any specific focus areas requested by the user
4. Proceed to analyze charts sequentially, one at a time

### Step 2: Load Technical A
