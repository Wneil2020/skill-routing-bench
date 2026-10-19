---
name: codebase-archaeologist
description: "Use when Analyze git history to create ownership maps, churn hotspot analysis, \"bus factor\" reports, pattern evolution timelines, and dead: covers codebase, archaeologist, archaeology, bus, churn"
metadata:
  holon-triggers: |
    who owns this code
    code archaeology
---

---
name: codebase-archaeologist
description: >-
  Analyze git history to create ownership maps, churn hotspot analysis, "bus
  factor" reports, pattern evolution timelines, and dead code detection through
  commit frequency decay. Adds the TIME dimension to code understanding. Use
  when the user asks "who owns this code", "code archaeology", "bus factor",
  "churn analysis", "what's the riskiest module", "dead code", "코드 히스토리", "코드
  소유자", "위험 분석", "who should review this", or any question about code ownership,
  history, or temporal risk patterns. Do NOT use for static code review (use
  simplify or deep-review), debugging (use diagnose), or git commit/PR
  operations (use domain-commit or ship).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Codebase Archaeologist — Temporal Code Analysis

Unearth the hidden history of your codebase. While code review tools see a snapshot, this skill sees the full timeline — who wrote what, what's decaying, what's risky, and what's been forgotten.

## Usage

```
/codebase-archaeologist                           # full project analysis
/codebase-archaeologist src/api/                  # scope to directory
/codebase-archaeologist --mode ownership          # ownership map only
/codebase-archaeologist --mode churn              # churn hotspots only
/codebase-archaeologist --mode bus-factor         # bus factor report only
/codebase-archaeologist --mode dead-code          # dead code candidates only
/codebase-archaeologist --mode risk               # composite risk heatmap
/codebase-archaeologist --since "6 months ago"    # custom time window
```

## Workflow

### Step 1: Determine Scope and Mode

Parse user input for:
- **Target path**: directory or file (default: entire repo)
- **Mode**: `ownership | churn | bus-factor | dead-code | risk | full` (default: `full`)
- **Time window**: `--since` value (default: 12 months). Accepts any git date format: `"6 months ago"`, `"2024-01-01"`, `"1 year ago"`

### S
