---
name: kwp-finance-variance-analysis
description: "Use when Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period: covers kwp, finance, variance, 계획, 출시"
metadata:
  holon-triggers: |
    analyzing budget vs. actual
    period-over-period changes
---

---
name: kwp-finance-variance-analysis
description: >-
  Decompose financial variances into drivers with narrative explanations and
  waterfall analysis. Use when analyzing budget vs. actual, period-over-period
  changes, revenue or expense variances, or preparing variance commentary for
  leadership. Do NOT use for tasks outside the finance domain. Korean triggers:
  "계획", "출시".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Variance Analysis

**Important**: This skill assists with variance analysis workflows but does not provide financial advice. All analyses should be reviewed by qualified financial professionals before use in reporting.

Techniques for decomposing variances, materiality thresholds, narrative generation, waterfall chart methodology, and budget vs actual vs forecast comparisons.

## Before You Start

Before beginning analysis, ask the user to clarify (use AskQuestion):

1. **Comparison type** — Budget vs. actual, actual vs. prior period, actual vs. forecast, or sequential (MoM)?
2. **Data source** — Where is the financial data? (file path, spreadsheet, or paste it directly)
3. **Materiality thresholds** — What dollar and percentage thresholds matter for your organization?
4. **Output audience** — Who will read this? (board, CFO, department heads, internal team)

DO NOT start the analysis until aligned on these inputs. The decomposition technique and narrative style differ by comparison type and audience.

## Variance Decomposition Techniques

### Price / Volume Decomposition

The most fundamental variance decomposition. Used for revenue, cost of goods, and any metric that can be expressed as Price x Volume.

**Formula:**
```
Total Variance = Actual - Budget (or Prior)

Volume Effect  = (Actual Volume - Budget Volume) x Budget Price
Price Effect   = (Actual Price - Budget Price) x Actual Volume
Mix Effect     = Residual (interaction term), or allocated proportionally

Verification:  Volume Effect + Price Effect
