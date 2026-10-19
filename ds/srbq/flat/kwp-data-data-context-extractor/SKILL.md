---
name: kwp-data-data-context-extractor
description: "Use when Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. Do NOT use for tasks outside the data domain: covers kwp, data, context, 데이터, 생성"
metadata:
  holon-triggers: |
    What data warehouse are you using?
    Which 3-5 tables do analysts query most often?
---

---
name: kwp-data-data-context-extractor
description: >-
  Generate or improve a company-specific data analysis skill by extracting
  tribal knowledge from analysts. Do NOT use for tasks outside the data domain.
  Korean triggers: "데이터", "생성", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Data Context Extractor

A meta-skill that extracts company-specific data knowledge from analysts and generates tailored data analysis skills.

## How It Works

This skill has two modes:

1. **Bootstrap Mode**: Create a new data analysis skill from scratch
2. **Iteration Mode**: Improve an existing skill by adding domain-specific reference files

---

## Bootstrap Mode

Use when: User wants to create a new data context skill for their warehouse.

### Phase 1: Database Connection & Discovery

**Step 1: Identify the database type**

Ask: "What data warehouse are you using?"

Common options:
- **BigQuery**
- **Snowflake**
- **PostgreSQL/Redshift**
- **Databricks**

Use `~~data warehouse` tools (query and schema) to connect. If unclear, check available MCP tools in the current session.

**Step 2: Explore the schema**

Use `~~data warehouse` schema tools to:
1. List available datasets/schemas
2. Identify the most important tables (ask user: "Which 3-5 tables do analysts query most often?")
3. Pull schema details for those key tables

Sample exploration queries by dialect:
```sql
-- BigQuery: List datasets
SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA

-- BigQuery: List tables in a dataset
SELECT table_name FROM `project.dataset.INFORMATION_SCHEMA.TABLES`

-- Snowflake: List schemas
SHOW SCHEMAS IN DATABASE my_database

-- Snowflake: List tables
SHOW TABLES IN SCHEMA my_schema
```

### Phase 2: Core Questions (Ask These)

After schema discovery, ask these questions conversationally (not all at once):

**Entity Disambiguation (Critical)**
> "When people here say 'user' or 'customer', what exactly do they mean? Are there different types?"


