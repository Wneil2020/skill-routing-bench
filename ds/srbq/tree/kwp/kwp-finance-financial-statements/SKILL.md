---
name: kwp-finance-financial-statements
description: "Use when Generate income statements, balance sheets, and cash flow statements with GAAP presentation and period-over-period comparison. Use when preparing: covers kwp, finance, financial, 생성, 리포트"
metadata:
  holon-triggers: |
    preparing financial statements
    running flux analysis
---

---
name: kwp-finance-financial-statements
description: >-
  Generate income statements, balance sheets, and cash flow statements with
  GAAP presentation and period-over-period comparison. Use when preparing
  financial statements, running flux analysis, or creating P&L reports with
  variance commentary. Do NOT use for tasks outside the finance domain. Korean
  triggers: "생성", "리포트", "프레젠테이션".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Financial Statements

**Important**: This skill assists with financial statement workflows but does not provide financial advice. All statements should be reviewed by qualified financial professionals before use in reporting or filings.

Formats, GAAP presentation requirements, common adjustments, and flux analysis methodology for income statements, balance sheets, and cash flow statements.

## Income Statement

### Standard Format (Classification of Expenses by Function)

```
Revenue
  Product revenue
  Service revenue
  Other revenue
Total Revenue

Cost of Revenue
  Product costs
  Service costs
Total Cost of Revenue

Gross Profit

Operating Expenses
  Research and development
  Sales and marketing
  General and administrative
Total Operating Expenses

Operating Income (Loss)

Other Income (Expense)
  Interest income
  Interest expense
  Other income (expense), net
Total Other Income (Expense)

Income (Loss) Before Income Taxes
  Income tax expense (benefit)
Net Income (Loss)

Earnings Per Share (if applicable)
  Basic
  Diluted
```

### GAAP Presentation Requirements (ASC 220 / IAS 1)

- Present all items of income and expense recognized in a period
- Classify expenses either by nature (materials, labor, depreciation) or by function (COGS, R&D, S&M, G&A) — function is more common for US companies
- If classified by function, disclose depreciation, amortization, and employee benefit costs by nature in the notes
- Present operating and non-operating items separately
- Show income tax expense
