---
name: trading-data-quality-checker
description: "Use when Validate data quality in market analysis documents and blog articles before publication. Use when the user asks to \"check data quality\": covers trading, data, quality, advisory, etf"
metadata:
  holon-triggers: |
    check data quality
    validate market data
---

---
name: trading-data-quality-checker
description: >-
  Validate data quality in market analysis documents and blog articles before publication. Use when the user asks to "check data quality", "validate market data", "proofread financial doc", "데이터 품질 검사", "재무 데이터 검증", or needs validation of price scale consistency (ETF vs futures), instrument notation errors, date/day-of-week mismatches, allocation total errors, and unit mismatches. Supports English and Japanese content. Advisory mode — flags issues as warnings for human review, not blockers. Do NOT use for code quality review (use simplify or deep-review).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: execution
  source: claude-trading-skills
  api_required: none
---

## Overview

Detect common data quality issues in market analysis documents before
publication. The checker validates five categories: price scale consistency,
instrument notation, date/weekday accuracy, allocation totals, and unit usage.
All findings are advisory -- they flag potential issues for human review rather
than blocking publication.

## When to Use

- Before publishing a weekly strategy blog or market analysis report
- After generating automated market summaries
- When reviewing translated documents (English/Japanese) for data accuracy
- When combining data from multiple sources (FRED, FMP, FINVIZ) into one report
- As a pre-flight check for any document containing financial data

## Prerequisites

- Python 3.9+
- No external API keys required
- No third-party Python packages required (uses only standard library)

## Workflow

### Step 1: Receive Input Document

Accept the target markdown file path and optional parameters:
- `--file`: Path to the markdown document to validate (required)
- `--checks`: Comma-separated list of checks to run (optional; default: all)
- `--as-of`: Reference date for year inference in YYYY-MM-DD format (optional)
- `--output-dir`: Directory for report output (optional; default: `outputs/reports/
