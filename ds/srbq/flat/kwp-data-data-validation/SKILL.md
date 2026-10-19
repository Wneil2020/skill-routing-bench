---
name: kwp-data-data-validation
description: "Use when QA an analysis before sharing with stakeholders — methodology checks, accuracy verification, and bias detection. Use when reviewing an analysis for: covers kwp, data, validation, 데이터, 리뷰"
metadata:
  holon-triggers: |
    reviewing an analysis for errors
    checking for survivorship bias
---

---
name: kwp-data-data-validation
description: >-
  QA an analysis before sharing with stakeholders — methodology checks,
  accuracy verification, and bias detection. Use when reviewing an analysis for
  errors, checking for survivorship bias, validating aggregation logic, or
  preparing documentation for reproducibility. Do NOT use for tasks outside the
  data domain. Korean triggers: "데이터", "리뷰", "체크", "출시".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Data Validation Skill

Pre-delivery QA checklist, common data analysis pitfalls, result sanity checking, and documentation standards for reproducibility.

## Pre-Delivery QA Checklist

Run through this checklist before sharing any analysis with stakeholders.

### Data Quality Checks

- [ ] **Source verification**: Confirmed which tables/data sources were used. Are they the right ones for this question?
- [ ] **Freshness**: Data is current enough for the analysis. Noted the "as of" date.
- [ ] **Completeness**: No unexpected gaps in time series or missing segments.
- [ ] **Null handling**: Checked null rates in key columns. Nulls are handled appropriately (excluded, imputed, or flagged).
- [ ] **Deduplication**: Confirmed no double-counting from bad joins or duplicate source records.
- [ ] **Filter verification**: All WHERE clauses and filters are correct. No unintended exclusions.

### Calculation Checks

- [ ] **Aggregation logic**: GROUP BY includes all non-aggregated columns. Aggregation level matches the analysis grain.
- [ ] **Denominator correctness**: Rate and percentage calculations use the right denominator. Denominators are non-zero.
- [ ] **Date alignment**: Comparisons use the same time period length. Partial periods are excluded or noted.
- [ ] **Join correctness**: JOIN types are appropriate (INNER vs LEFT). Many-to-many joins haven't inflated counts.
- [ ] **Metric definitions**: Metrics match how stakeholders define them. Any deviations are noted.
- [ ] **Subto
