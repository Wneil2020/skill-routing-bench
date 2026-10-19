---
name: anthropic-docx
description: "Use when Create, read, edit, and manipulate Word documents (.docx). Use when the user mentions Word doc, .docx, or requests professional documents with: covers anthropic, docx, 워드 문서, 문서 생성, headings"
metadata:
  holon-triggers: |
    requests professional documents with tables of contents
    page numbers
---

---
name: anthropic-docx
description: >-
  Create, read, edit, and manipulate Word documents (.docx). Use when the user
  mentions Word doc, .docx, or requests professional documents with tables of
  contents, headings, page numbers, letterheads; extracting or reorganizing
  content from .docx; inserting or replacing images; find-and-replace; tracked
  changes or comments; reports, memos, letters, templates as Word files. Do NOT
  use for PDFs (use anthropic-pdf), spreadsheets (use anthropic-xlsx), or
  presentations (use anthropic-pptx). Korean triggers: "워드 문서", "docx",
  "문서 생성", "리포트".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license_note: "See LICENSE.txt in skill directory"
  category: "document"
---
# DOCX creation, editing, and analysis

## Overview

A .docx file is a ZIP archive containing XML files.

## HARD-GATE (New Document Creation Only)

When creating a NEW document (not reading or editing existing ones), do NOT start generating until these are confirmed:

1. **Document purpose** — What type of document? (report, memo, letter, proposal, manual)
2. **Target audience** — Who will read this? (executives, engineers, clients, regulators)
3. **Key sections or structure** — What must the document contain?

If any of these are unclear from the user's request, ASK before proceeding. Do not assume defaults for audience or purpose.

This gate does NOT apply to: reading content, editing existing documents, format conversion, or find-and-replace operations.

## Quick Reference

| Task | Approach |
|------|----------|
| Read/analyze content | `pandoc` or unpack for raw XML |
| Create new document | Confirm HARD-GATE requirements → Read [references/style-guide.md](references/style-guide.md) + [assets/templates/document-structure.md](assets/templates/document-structure.md) → Use `docx-js` - see Creating New Documents below |
| Edit existing document | Unpack → edit XML → repack - see Editing Existing Documents below |

### Converting .doc to .docx

Legacy
