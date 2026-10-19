---
name: office-template-enforcer
description: "Use when Create company-compliant DOCX and PPTX outputs from approved corporate templates without fine-tuning. Orchestrates template: covers office, template, enforcer, population, preserve"
metadata:
  holon-triggers: |
    create a document from template
    make a presentation from template
---

---
name: office-template-enforcer
description: >-
  Create company-compliant DOCX and PPTX outputs from approved corporate
  templates without fine-tuning. Orchestrates template selection, content
  generation as structured JSON, template population via sub-engines, and
  automated validation. Use when the user asks to "create a document from
  template", "make a presentation from template", "회사 템플릿으로 문서 만들기",
  "사내 양식으로 PPT 생성", "템플릿 기반 보고서", "corporate template document",
  "template-compliant output", or needs office documents that preserve corporate
  styles, slide masters, layouts, and formatting rules. Do NOT use for creating
  documents from scratch without templates (use anthropic-docx or anthropic-pptx).
  Do NOT use for PPTX template work alone (use ppt-template-engine directly).
  Do NOT use for DOCX template work alone (use docx-template-engine directly).
  Do NOT use for non-office document generation like PDFs or spreadsheets.
metadata:
  author: "thakicloud"
  version: "1.0.0"
  category: "document"
---

# Office Template Enforcer

Orchestrate the creation of corporate-compliant office documents by routing user requests to the correct template engine. This skill ensures that all DOCX and PPTX outputs adhere to approved templates with zero style drift.

## Core Principle

**LLM generates content. Template engines enforce format. Validators block violations.**

No fine-tuning required. No model-specific behavior. Any LLM produces the same compliant output because the template is the authority, not the model.

## Architecture

```
User Request
    ↓
office-template-enforcer (this skill)
    ├─ Detect document type (PPTX or DOCX)
    ├─ Select template from catalog
    ├─ Generate JSON content spec (LLM)
    └─ Delegate to engine
         ├─ ppt-template-engine  → .pptx output
         └─ docx-template-engine → .docx output
              ↓
         Validate → Return or Fail
```

## Workflow

### Step 1: Analyze Request

Determine from the user's request:
