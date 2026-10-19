---
name: trading-options-theta
description: "Use when Run professional-grade options theta trading analysis using 12 quant-firm-style prompts covering 0DTE credit spreads, market regime: covers trading, options, theta, buying, condors"
metadata:
  holon-triggers: |
    options theta
    credit spread setup
---

---
name: trading-options-theta
description: >-
  Run professional-grade options theta trading analysis using 12 quant-firm-style
  prompts covering 0DTE credit spreads, market regime classification, iron condors,
  theta decay tracking, strike selection, pre-market analysis, risk management,
  volatility skew exploitation, weekly income calendars, earnings IV crush, EOD scalping,
  and monthly performance dashboards. Use when the user asks for "options theta",
  "credit spread setup", "iron condor", "0DTE trade", "theta decay", "premium selling",
  "IV crush", "skew trade", "market regime", "theta scalp", "options income",
  "옵션 세타", "세타 매매", "프리미엄 매도", "아이언 콘도르", "크레딧 스프레드",
  or any options premium-selling / theta income strategy request.
  Do NOT use for stock fundamental analysis (use daily-stock-check).
  Do NOT use for futures or commodity trading.
  Do NOT use for crypto options.
  Do NOT use for long options buying strategies (these are short premium / theta strategies only).
metadata:
  author: thaki
  version: 1.0.0
  category: trading
  source: "@heynavtoor X thread (2030242736453169380)"
---

# Options Theta Trading — 12 Quant Firm Prompts

Professional options theta income strategies modeled after methodologies from Tastytrade, Citadel, SIG, Two Sigma, D.E. Shaw, Jane Street, Wolverine Trading, Akuna Capital, Peak6, IMC Trading, and Optiver.

For the full prompt catalog, see [references/prompt-catalog.md](references/prompt-catalog.md).
For source attribution, see [references/source-attribution.md](references/source-attribution.md).

## Input

The user provides:
1. **Strategy type** — specific strategy name, keyword, or "daily"/"full" for combo workflow
2. **Market parameters** — varies by prompt (SPX price, VIX, account size, positions, etc.)

## Workflow

### Step 1: Identify Strategy

Map the user's request to one or more prompts using this routing table:

| User Says | Prompt(s) | File |
|-----------|-----------|------|
| "0DTE", "credit spread", "S
