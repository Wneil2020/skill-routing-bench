---
name: refactor-simulator
description: "Use when Before making any code change, simulate the blast radius by analyzing all call sites, import chains, type dependencies, and: covers refactor, simulator, blast, consequences, generalpurpose"
metadata:
  holon-triggers: |
    blast radius
    impact analysis
---

---
name: refactor-simulator
description: >-
  Before making any code change, simulate the blast radius by analyzing all
  call sites, import chains, type dependencies, and test coverage for the
  affected area. Produces a "what-if" impact report with risk scores — without
  touching any code. Use when the user asks about "blast radius", "impact
  analysis", "refactor simulator", "what if I change", "what if I rename", "what
  if I move", "리팩토링 시뮬레이션", "영향 분석", "before refactoring", or wants to
  understand the consequences of a proposed change before executing it. Do NOT
  use for executing refactors (use simplify or generalPurpose), code review of
  existing code (use deep-review), or debugging (use diagnose).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Refactor Simulator — Pre-Change Blast Radius Analysis

Predict the impact of a code change before you make it. Maps dependencies, counts call sites, checks test coverage, and produces a risk-scored impact report — all without modifying a single file.

## Usage

```
/refactor-simulator "rename getUserById to findUserById"
/refactor-simulator "move src/utils/auth.ts to src/lib/auth/"
/refactor-simulator "delete UserProfile component"
/refactor-simulator "extract validateInput into a shared module"
/refactor-simulator --symbol "useAuth" --action rename
/refactor-simulator --file src/api/handler.ts --action split
```

## Workflow

### Step 1: Parse the Proposed Change

Extract from user input:
- **Target symbol**: function, class, component, type, or file being changed
- **Action type**: `rename | move | delete | extract | split | modify-signature`
- **Source location**: current file/module path
- **Destination**: new name, path, or signature (if applicable)

If ambiguous, ask the user to clarify the exact change.

### Step 2: Build Dependency Graph

For the target symbol, trace all connections:

#### 2a. Downstream Dependencies (what uses this?)

Use `rg -F` (fixed-string / literal) fo
