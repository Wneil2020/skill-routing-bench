---
name: kwp-bio-research-instrument-data-to-allotrope
description: "Use when Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when: covers kwp, bio, research, 리서치, 데이터"
---

---
name: kwp-bio-research-instrument-data-to-allotrope
description: >-
  Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to
  Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill
  when scientists need to standardize instrument data for LIMS systems, data
  lakes, or downstream analysis. Supports auto-detection of instrument types.
  Outputs include full ASM JSON, flattened CSV for easy import, and exportable
  Python code for data engineers. Common triggers include converting instrument
  files, standardizing lab data, preparing data for upload to LIMS/ELN systems,
  or generating parser code for production pipelines. Do NOT use for tasks
  outside the bio domain. Korean triggers: "리서치", "데이터", "파이프라인", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Instrument Data to Allotrope Converter

Convert instrument files into standardized Allotrope Simple Model (ASM) format for LIMS upload, data lakes, or handoff to data engineering teams.

> **Note: This is an Example Skill**
>
> This skill demonstrates how skills can support your data engineering tasks—automating schema transformations, parsing instrument outputs, and generating production-ready code.
>
> **To customize for your organization:**
> - Modify the `references/` files to include your company's specific schemas or ontology mappings
> - Use an MCP server to connect to systems that define your schemas (e.g., your LIMS, data catalog, or schema registry)
> - Extend the `scripts/` to handle proprietary instrument formats or internal data standards
>
> This pattern can be adapted for any data transformation workflow where you need to convert between formats or validate against organizational standards.

## Workflow Overview

1. **Detect instrument type** from file contents (auto-detect or user-specified)
2. **Parse file** using allotropy library (native) or flexible fallback parser
3. **Generate outputs**:
   - ASM JSON (full semant
