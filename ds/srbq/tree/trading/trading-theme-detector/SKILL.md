---
name: trading-theme-detector
description: "Use when Detects and ranks trending market themes across sectors using cross-sector momentum, volume, and breadth signals. Use when the user asks: covers trading, theme, detector, bearish, bullish"
metadata:
  holon-triggers: |
    current market themes
    trending sectors
---

---
name: trading-theme-detector
description: >-
  Detects and ranks trending market themes across sectors using cross-sector momentum, volume, and breadth signals.
  Use when the user asks "current market themes", "trending sectors", "sector rotation", "thematic investing",
  "hot or cold themes", "bullish bearish narratives", "theme lifecycle", "시장 테마", "섹터 로테이션", "테마 투자".
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for sector rotation analysis without theme detection (use trading-sector-analyst).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: optional
---

# Theme Detector

## Overview

This skill detects and ranks trending market themes by analyzing cross-sector momentum, volume, and breadth signals. It identifies both bullish (upward momentum) and bearish (downward pressure) themes, assesses lifecycle maturity (early/mid/late/exhaustion), and provides a confidence score combining quantitative data with narrative analysis.

**3-Dimensional Scoring Model:**
1. **Theme Heat** (0-100): Direction-neutral strength of the theme (momentum, volume, uptrend ratio, breadth)
2. **Lifecycle Maturity**: Stage classification (Early / Mid / Late / Exhaustion) based on duration, extremity clustering, valuation, and ETF proliferation
3. **Confidence** (Low / Medium / High): Reliability of the detection, combining quantitative breadth with narrative confirmation

**Key Features:**
- Cross-sector theme detection using FINVIZ industry data
- Direction-aware scoring (bullish and bearish themes)
- Lifecycle maturity assessment to identify crowded vs. emerging trades
- ETF proliferation scoring (more ETFs = more mature/crowded theme)
- Integration with uptrend-dashboard for 3-point evaluation
- Dual-mode operation: FINVIZ Elite (fast) or public scraping (slower, limited)
- WebSearch-based narrative confirmation for top themes

---

## When to Use This Skill

**Explicit Triggers:**
- "
