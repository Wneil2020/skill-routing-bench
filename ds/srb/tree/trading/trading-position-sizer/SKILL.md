---
name: trading-position-sizer
description: "Use when Calculate risk-based position sizes for long stock trades using Fixed Fractional, ATR-Based, or Kelly Criterion methods. Supports: covers trading, position, sizer, atr, concentration"
metadata:
  holon-triggers: |
    position size
    how many shares to buy
---

---
name: trading-position-sizer
description: >-
  Calculate risk-based position sizes for long stock trades using Fixed Fractional, ATR-Based, or Kelly Criterion methods. Supports stop-loss distance calculation, volatility scaling, and sector concentration checks. Use when the user asks to "position size", "how many shares to buy", "risk per trade", "Kelly criterion", "ATR-based sizing", "포트폴리오 리스크 배분", "포지션 사이징", "몇 주 살까", or wants portfolio risk allocation guidance. Do NOT use for stock analysis (use daily-stock-check or trading-technical-analyst).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: execution
  source: claude-trading-skills
  api_required: none
---

# Position Sizer

## Overview

Calculate the optimal number of shares to buy for a long stock trade based on risk management principles. Supports three sizing methods:

- **Fixed Fractional**: Risk a fixed percentage of account equity per trade (default: 1%)
- **ATR-Based**: Use Average True Range to set volatility-adjusted stop distances
- **Kelly Criterion**: Calculate mathematically optimal risk allocation from historical win/loss statistics

All methods apply portfolio constraints (max position %, max sector %) and output a final recommended share count with full risk breakdown.

## When to Use

- User asks "how many shares should I buy?"
- User wants to calculate position size for a specific trade setup
- User mentions risk per trade, stop-loss sizing, or portfolio allocation
- User asks about Kelly Criterion or ATR-based position sizing
- User wants to check if a position fits within portfolio concentration limits

## Prerequisites

- No API keys required
- Python 3.9+ with standard library only

## Workflow

### Step 1: Gather Trade Parameters

Collect from the user:
- **Required**: Account size (total equity)
- **Mode A (Fixed Fractional)**: Entry price, stop price, risk percentage (default 1%)
- **Mode B (ATR-Based)**: Entry price, ATR value, ATR multiplier (default 2.0x), risk per
