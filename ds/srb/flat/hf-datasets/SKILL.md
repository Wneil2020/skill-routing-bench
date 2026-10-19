---
name: hf-datasets
description: "Use when Create and manage datasets on HuggingFace Hub — initialize repos, stream row updates, run SQL queries, and transform data. Use when: covers datasets, 데이터셋 생성, HF 데이터셋, initialize, curated"
metadata:
  holon-triggers: |
    creating financial training datasets (sentiment labels
    stock signals)
---

---
name: hf-datasets
description: >-
  Create and manage datasets on HuggingFace Hub — initialize repos, stream row
  updates, run SQL queries, and transform data. Use when creating financial
  training datasets (sentiment labels, stock signals), uploading curated data to
  Hub, or querying existing datasets with SQL. Do NOT use for exploring datasets
  read-only (use hf-dataset-viewer). Do NOT use for local CSV/DB operations (use
  weekly-stock-update). Do NOT use for model training (use hf-model-trainer).
  Korean triggers: "데이터셋 생성", "HF 데이터셋".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Overview
This skill provides tools to manage datasets on the Hugging Face Hub with a focus on creation, configuration, content management, and SQL-based data manipulation. It is designed to complement the existing Hugging Face MCP server by providing dataset editing and querying capabilities.

## Integration with HF MCP Server
- **Use HF MCP Server for**: Dataset discovery, search, and metadata retrieval
- **Use This Skill for**: Dataset creation, content editing, SQL queries, data transformation, and structured data formatting

# Version
2.1.0

# Dependencies
# This skill uses PEP 723 scripts with inline dependency management
# Scripts auto-install requirements when run with: uv run scripts/script_name.py

- uv (Python package manager)
- Getting Started: See "Usage Instructions" below for PEP 723 usage

# Core Capabilities

## 1. Dataset Lifecycle Management
- **Initialize**: Create new dataset repositories with proper structure
- **Configure**: Store detailed configuration including system prompts and metadata
- **Stream Updates**: Add rows efficiently without downloading entire datasets

## 2. SQL-Based Dataset Querying (NEW)
Query any Hugging Face dataset using DuckDB SQL via `scripts/sql_manager.py`:
- **Direct Queries**: Run SQL on datasets using the `hf://` protocol
- **Schema Discovery**: Describe dataset structure and column types
- **Data Samp
