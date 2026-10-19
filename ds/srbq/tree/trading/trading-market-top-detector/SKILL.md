---
name: trading-market-top-detector
description: "Use when Detects market top probability using O'Neil Distribution Days, Minervini Leading Stock Deterioration, and Monty Defensive Sector: covers trading, market, top, breakdown, deterioration"
metadata:
  holon-triggers: |
    is the market topping
    distribution days
---

---
name: trading-market-top-detector
description: >-
  Detects market top probability using O'Neil Distribution Days, Minervini Leading Stock Deterioration, and Monty Defensive Sector Rotation.
  Use when the user asks "is the market topping", "distribution days", "defensive rotation", "leadership breakdown",
  "reduce equity exposure", "market top risk", "시장 천정", "분배일", "노출 축소 타이밍".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for breadth health scoring (use trading-uptrend-analyzer).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: fmp
---

# Market Top Detector Skill

## Purpose

Detect the probability of a market top formation using a quantitative 6-component scoring system (0-100). Integrates three proven market top detection methodologies:

1. **O'Neil** - Distribution Day accumulation (institutional selling)
2. **Minervini** - Leading stock deterioration pattern
3. **Monty** - Defensive sector rotation signal

Unlike the Bubble Detector (macro/multi-month evaluation), this skill focuses on **tactical 2-8 week timing signals** that precede 10-20% market corrections.

## When to Use This Skill

**English:**
- User asks "Is the market topping?" or "Are we near a top?"
- User notices distribution days accumulating
- User observes defensive sectors outperforming growth
- User sees leading stocks breaking down while indices hold
- User asks about reducing equity exposure timing
- User wants to assess correction probability for the next 2-8 weeks

**Japanese:**
- 「天井が近い？」「今は利確すべき？」
- ディストリビューションデーの蓄積を懸念
- ディフェンシブセクターがグロースをアウトパフォーム
- 先導株が崩れ始めているが指数はまだ持ちこたえている
- エクスポージャー縮小のタイミング判断
- 今後2〜8週間の調整確率を評価したい

## Difference from Bubble Detector

| Aspect | Market Top Detector | Bubble Detector |
|--------|-------------------|-----------------|
| Timeframe | 2-8 weeks | Months to years |
| Target | 10-20% correction | Bubble collapse (30%+) |
| Methodology | O'Neil/Minervini/Mon
