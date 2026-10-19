---
name: docx-template-engine
description: "Use when Populate approved DOCX templates with LLM-generated content via JSON specs, enforcing style whitelists, slot contracts, heading hierarchy, and: covers docx, template, engine, heading, slot"
metadata:
  holon-triggers: |
    fill a Word template
    generate report from template
---

---
name: docx-template-engine
description: >-
  Populate approved DOCX templates with LLM-generated content via JSON specs,
  enforcing style whitelists, slot contracts, heading hierarchy, and corporate
  formatting. Use when the user asks to "fill a Word template", "generate
  report from template", "populate document template", "DOCX 템플릿 채우기",
  "워드 템플릿 적용", "보고서 템플릿 생성", or needs template-compliant DOCX
  output that preserves corporate branding and structure. Do NOT use for
  creating Word documents from scratch without a template (use anthropic-docx).
  Do NOT use for editing existing non-template documents (use anthropic-docx).
  Do NOT use for PPTX template work (use ppt-template-engine). Do NOT use for
  orchestrating template selection across formats (use office-template-enforcer).
metadata:
  author: "thakicloud"
  version: "1.0.0"
  category: "document"
---

# DOCX Template Engine

Generate corporate-compliant DOCX files by populating approved templates with structured content. The LLM produces content only; this engine enforces all styles, structure, and formatting rules.

## Core Principle

**Content from LLM. Format from template. No exceptions.**

The LLM never decides fonts, colors, heading styles, or page layout. It only fills named slots with text, tables, or lists.

## Workflow

```
1. Inspect template    → extract styles + slots + bookmarks
2. Generate JSON spec  → LLM fills slot values only
3. Populate template   → scripts/generate_docx.py
4. Validate output     → scripts/validate_docx.py
5. Return or fail      → hard fail blocks; soft fail warns
```

### Step 1: Inspect Template

Run `scripts/inspect_template_docx.py <template.docx>` to discover available styles, bookmarks, and placeholder markers. Review the corresponding placeholder map at `assets/placeholder-maps/<template_id>.json`.

### Step 2: Generate JSON Spec

Instruct the LLM to produce a JSON object matching this schema:

```json
{
  "template_id": "thaki-report-v1",
  "document_tit
