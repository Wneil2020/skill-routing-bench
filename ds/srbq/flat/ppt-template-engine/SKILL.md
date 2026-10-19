---
name: ppt-template-engine
description: "Use when Populate approved PPTX templates with LLM-generated content via JSON specs, enforcing slide master layouts, placeholder contracts, and: covers ppt, template, engine, master, branding"
metadata:
  holon-triggers: |
    fill a PPT template
    generate slides from template
---

---
name: ppt-template-engine
description: >-
  Populate approved PPTX templates with LLM-generated content via JSON specs,
  enforcing slide master layouts, placeholder contracts, and corporate styling.
  Use when the user asks to "fill a PPT template", "generate slides from
  template", "populate presentation template", "PPT 템플릿 채우기", "슬라이드
  템플릿 적용", "프레젠테이션 템플릿 생성", or needs template-compliant PPTX
  output that preserves corporate branding. Do NOT use for creating
  presentations from scratch without a template (use anthropic-pptx). Do NOT
  use for editing existing non-template presentations (use anthropic-pptx). Do
  NOT use for DOCX template work (use docx-template-engine). Do NOT use for
  orchestrating template selection across formats (use office-template-enforcer).
metadata:
  author: "thakicloud"
  version: "1.0.0"
  category: "document"
---

# PPT Template Engine

Generate corporate-compliant PPTX files by populating approved templates with structured content. The LLM produces content only; this engine enforces all layout, style, and branding rules.

## Core Principle

**Content from LLM. Format from template. No exceptions.**

The LLM never decides fonts, colors, positions, or layouts. It only fills named placeholders with text, bullet lists, or table data.

## Workflow

```
1. Inspect template    → extract layouts + placeholders
2. Generate JSON spec  → LLM fills placeholder values only
3. Populate template   → scripts/generate_pptx.py
4. Validate output     → scripts/validate_pptx.py
5. Return or fail      → hard fail blocks; soft fail warns
```

### Step 1: Inspect Template

Run `scripts/inspect_template_pptx.py <template.pptx>` to discover available layouts and placeholder names. Review the corresponding placeholder map at `assets/placeholder-maps/<template_id>.json`.

### Step 2: Generate JSON Spec

Instruct the LLM to produce a JSON object matching this schema:

```json
{
  "template_id": "thaki-proposal-v1",
  "presentation_title": "Title here"
