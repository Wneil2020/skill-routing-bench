---
name: kwp-data-data-exploration
description: "Use when Profile and explore datasets to understand their shape, quality, and patterns before analysis. Use when encountering a new dataset, assessing data: covers kwp, data, exploration, 데이터, 분석"
metadata:
  holon-triggers: |
    encountering a new dataset
    assessing data quality
---

---
name: kwp-data-data-exploration
description: >-
  Profile and explore datasets to understand their shape, quality, and patterns
  before analysis. Use when encountering a new dataset, assessing data quality,
  discovering column distributions, identifying nulls and outliers, or deciding
  which dimensions to analyze. Do NOT use for tasks outside the data domain.
  Korean triggers: "데이터", "분석".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Data Exploration Skill

Systematic methodology for profiling datasets, assessing data quality, discovering patterns, and understanding schemas.

## Before You Start

Before exploring a dataset, ask the user to clarify (use AskQuestion):

1. **Data location** — Where is the dataset? (file path, database table, or paste a sample)
2. **Analysis goal** — What question are you trying to answer? Or is this an open-ended quality check?
3. **Data context** — What does one row represent? Any known issues or gotchas?

If the user provides a file or table directly, proceed to profiling and ask about context as you discover the schema.

## Data Profiling Methodology

### Phase 1: Structural Understanding

Before analyzing any data, understand its structure:

**Table-level questions:**
- How many rows and columns?
- What is the grain (one row per what)?
- What is the primary key? Is it unique?
- When was the data last updated?
- How far back does the data go?

**Column classification:**
Categorize each column as one of:
- **Identifier**: Unique keys, foreign keys, entity IDs
- **Dimension**: Categorical attributes for grouping/filtering (status, type, region, category)
- **Metric**: Quantitative values for measurement (revenue, count, duration, score)
- **Temporal**: Dates and timestamps (created_at, updated_at, event_date)
- **Text**: Free-form text fields (description, notes, name)
- **Boolean**: True/false flags
- **Structural**: JSON, arrays, nested structures

### Phase 2: Column-Level Profiling

F
