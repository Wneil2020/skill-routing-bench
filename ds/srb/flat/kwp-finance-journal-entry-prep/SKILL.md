---
name: kwp-finance-journal-entry-prep
description: "Use when Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization: covers kwp, finance, journal, 수정, 문서"
metadata:
  holon-triggers: |
    booking accruals
    prepaid amortization
---

---
name: kwp-finance-journal-entry-prep
description: >-
  Prepare journal entries with proper debits, credits, and supporting
  documentation for month-end close. Use when booking accruals, prepaid
  amortization, fixed asset depreciation, payroll entries, revenue recognition,
  or any manual journal entry. Do NOT use for tasks outside the finance domain.
  Korean triggers: "수정", "문서".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Journal Entry Preparation

**Important**: This skill assists with journal entry workflows but does not provide financial advice. All entries should be reviewed by qualified financial professionals before posting.

Best practices, standard entry types, documentation requirements, and review workflows for journal entry preparation.

## Standard Accrual Types and Their Entries

### Accounts Payable Accruals

Accrue for goods or services received but not yet invoiced at period end.

**Typical entry:**
- Debit: Expense account (or capitalize if asset-qualifying)
- Credit: Accrued liabilities

**Sources for calculation:**
- Open purchase orders with confirmed receipts
- Contracts with services rendered but unbilled
- Recurring vendor arrangements (utilities, subscriptions, professional services)
- Employee expense reports submitted but not yet processed

**Key considerations:**
- Reverse in the following period (auto-reversal recommended)
- Use consistent estimation methodology period over period
- Document basis for estimates (PO amount, contract terms, historical run-rate)
- Track actual vs accrual to refine future estimates

### Fixed Asset Depreciation

Book periodic depreciation expense for tangible and intangible assets.

**Typical entry:**
- Debit: Depreciation/amortization expense (by department or cost center)
- Credit: Accumulated depreciation/amortization

**Depreciation methods:**
- **Straight-line:** (Cost - Salvage) / Useful life — most common for financial reporting
- **Declining balance:** A
