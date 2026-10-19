---
name: problem-definition
description: "Use when Guide users through a structured 5D framework (Describe, Decompose, Diagnose, Define, Document) to properly define problems before jumping to: covers problem, definition, 리뷰, 테스트, frame"
metadata:
  holon-triggers: |
    define the problem
    what's the real problem
---

---
name: problem-definition
description: >-
  Guide users through a structured 5D framework (Describe, Decompose, Diagnose,
  Define, Document) to properly define problems before jumping to solutions.
  Produces a Problem Definition Document (PDD) with root cause hypotheses,
  stakeholder perspectives, and testable success criteria. Use when the user
  runs /define-problem, asks to "define the problem", "what's the real problem",
  "frame this problem", "problem statement", or "before we solve this". Do NOT
  use for code review (use simplify or deep-review), generating solutions (use
  diagnose), or project planning (use pm-execution). Korean triggers: "리뷰",
  "테스트", "계획", "진단".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Problem Definition — 5D Framework

Accurate problem definition is the single highest-leverage activity in any project. The 75/25 rule: spend 75% of effort defining the problem (P-code), 25% on the solution (S-code). Most failures trace back to poorly defined problems, not poor solutions.

This skill applies a structured 5-phase process that challenges surface-level framing, decomposes complexity, and produces a testable problem statement.

## Usage

```
/define-problem                                # deep mode (default)
/define-problem quick                          # single-pass problem statement
/define-problem team                           # collaborative workshop template
/define-problem "API latency exceeds SLO"      # with initial problem description
/define-problem deep src/api/                  # deep mode scoped to a directory
```

## Scoping Modes

| Mode | Trigger | Output |
|------|---------|--------|
| `quick` | `/define-problem quick` | One-page problem statement (Steps 1, 4, 5 only) |
| `deep` (default) | `/define-problem` or `/define-problem deep` | Full 5D analysis with PDD |
| `team` | `/define-problem team` | Facilitation template with prompts for team workshops |

## Workflow

### Step 1: D1 
