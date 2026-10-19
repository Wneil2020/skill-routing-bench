---
name: kwp-sales-competitive-intelligence
description: "Use when Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix: covers kwp, sales, competitive, 빌드, 검색"
---

---
name: kwp-sales-competitive-intelligence
description: >-
  Research your competitors and build an interactive battlecard. Outputs an
  HTML artifact with clickable competitor cards and a comparison matrix. Trigger
  with "competitive intel", "research competitors", "how do we compare to
  [competitor]", "battlecard for [competitor]", or "what's new with
  [competitor]". Do NOT use for tasks outside the sales domain. Korean triggers:
  "빌드", "검색", "리서치".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Competitive Intelligence

Research your competitors extensively and generate an **interactive HTML battlecard** you can use in deals. The output is a self-contained artifact with clickable competitor tabs and an overall comparison matrix.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                  COMPETITIVE INTELLIGENCE                        │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone via web search)                        │
│  ✓ Competitor product deep-dive: features, pricing, positioning │
│  ✓ Recent releases: what they've shipped in last 90 days        │
│  ✓ Your company releases: what you've shipped to counter        │
│  ✓ Differentiation matrix: where you win vs. where they win     │
│  ✓ Sales talk tracks: how to position against each competitor   │
│  ✓ Landmine questions: expose their weaknesses naturally        │
├─────────────────────────────────────────────────────────────────┤
│  OUTPUT: Interactive HTML Battlecard                             │
│  ✓ Comparison matrix overview                                    │
│  ✓ Clickable tabs for each competitor                           │
│  ✓ Dark theme, professional styling                             │
│  ✓ Self-contained HTML file — share or host anywhere            │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect
