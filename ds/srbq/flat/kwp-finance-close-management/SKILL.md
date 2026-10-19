---
name: kwp-finance-close-management
description: "Use when Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close: covers kwp, finance, close, 계획, 캘린더"
metadata:
  holon-triggers: |
    planning the close calendar
    tracking close progress
---

---
name: kwp-finance-close-management
description: >-
  Manage the month-end close process with task sequencing, dependencies, and
  status tracking. Use when planning the close calendar, tracking close
  progress, identifying blockers, or sequencing close activities by day. Do NOT
  use for tasks outside the finance domain. Korean triggers: "계획", "캘린더".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Close Management

**Important**: This skill assists with close management workflows but does not provide financial advice. All close activities should be reviewed by qualified financial professionals.

Month-end close checklist, task sequencing and dependencies, status tracking, and common close activities organized by day.

## Month-End Close Checklist

### Pre-Close (Last 2-3 Business Days of the Month)

- [ ] Send close calendar and deadline reminders to all contributors
- [ ] Confirm cut-off procedures with AP, AR, payroll, and treasury
- [ ] Verify all sub-systems are processing normally (ERP, payroll, banking)
- [ ] Complete preliminary bank reconciliation (all but last-day activity)
- [ ] Review open purchase orders for potential accrual needs
- [ ] Confirm payroll processing schedule aligns with close timeline
- [ ] Collect information for any known unusual transactions

### Close Day 1 (T+1: First Business Day After Month-End)

- [ ] Confirm all sub-ledger modules have completed period-end processing
- [ ] Run AP accruals for goods/services received but not invoiced
- [ ] Post payroll entries and payroll accrual (if pay period straddles month-end)
- [ ] Record cash receipts and disbursements through month-end
- [ ] Post intercompany transactions and confirm with counterparties
- [ ] Complete bank reconciliation with final bank statement
- [ ] Run fixed asset depreciation
- [ ] Post prepaid expense amortization

### Close Day 2 (T+2)

- [ ] Complete revenue recognition entries and deferred revenue adjustments
- [ ] Post all 
