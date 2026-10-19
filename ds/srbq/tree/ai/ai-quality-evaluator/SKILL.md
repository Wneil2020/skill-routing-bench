---
name: ai-quality-evaluator
description: "Use when Score and validate AI-generated financial reports for accuracy, hallucination detection, data consistency, coverage: covers quality, evaluator, actionability, completeness, hallucination"
metadata:
  holon-triggers: |
    check report quality
    validate AI output
---

---
name: ai-quality-evaluator
description: >-
  Score and validate AI-generated financial reports for accuracy, hallucination
  detection, data consistency, coverage completeness, and actionability.
  Implements a 5-dimension quality gate before Slack distribution. Use when the
  user asks to "check report quality", "validate AI output", "score this
  report", "detect hallucinations", "quality gate", "ai quality", "AI 품질
  평가", "리포트 검증", "환각 감지", or wants to verify AI-generated stock
  analysis before publishing.
  Do NOT use for evaluating LLM prompts or judge prompts (use evals-skills).
  Do NOT use for code quality review (use simplify or deep-review).
  Do NOT use for general AI output evaluation outside finance (use evals-skills).
  Do NOT use for running the daily pipeline (use today).
metadata:
  author: thaki
  version: 1.0.0
  category: review
---

# AI Quality Evaluator

Validate AI-generated financial reports and analysis outputs against ground truth data, scoring across 5 quality dimensions. Acts as a quality gate between report generation and Slack distribution.

## Quality Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| **Accuracy** | 30% | Do numbers match DB data? Are signals correct? |
| **Consistency** | 20% | Do conclusions align with the underlying data? |
| **Coverage** | 20% | Are all tracked tickers and categories represented? |
| **Actionability** | 20% | Are buy/sell recommendations clear and justified? |
| **Tone** | 10% | Is the language professional, balanced, and disclaimer-compliant? |

Final score: weighted average on a 0-10 scale.

| Score Range | Gate Decision |
|-------------|---------------|
| 8.0 - 10.0 | PASS — publish directly |
| 6.0 - 7.9 | REVIEW — flag issues, suggest fixes, ask for confirmation |
| 0.0 - 5.9 | FAIL — do not publish, list all critical issues |

## Workflow

### Step 1: Identify Artifacts to Evaluate

Locate the AI-generated outputs:

1. **Analysis JSON**: `o
