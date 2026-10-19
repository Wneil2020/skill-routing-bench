---
name: anthropic-pptx
description: "Use when Create, read, edit PowerPoint presentations (.pptx). Includes creating slide decks, pitch decks, or presentations, reading, parsing, or: covers anthropic, pptx, 프레젠테이션, 슬라이드, above"
metadata:
  holon-triggers: |
    deck
    slides
---

---
name: anthropic-pptx
description: >-
  Create, read, edit PowerPoint presentations (.pptx). Includes creating slide
  decks, pitch decks, or presentations; reading, parsing, or extracting text
  from .pptx files; editing, modifying, or updating existing presentations;
  combining or splitting slide files; working with templates, layouts, speaker
  notes, or comments. Use when user mentions "deck", "slides", "presentation",
  or references a .pptx filename. Do NOT use for Word documents (use
  anthropic-docx), spreadsheets (use anthropic-xlsx), or PDFs (use
  anthropic-pdf). Korean triggers: "프레젠테이션", "슬라이드", "pptx".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Proprietary. LICENSE.txt has complete terms"
  category: "document"
---
# PPTX Skill

## HARD-GATE (New Presentation Creation Only)

When creating a NEW presentation from scratch (not reading or editing existing ones), do NOT start generating until these are confirmed:

1. **Audience** — Who will see this? (investors, board, engineers, customers, internal team)
2. **Key message** — What is the ONE thing the audience should remember?
3. **Slide count** — Approximate number of slides (default: 10-15 if unspecified)

If any of these are unclear from the user's request, ASK before proceeding. Do not assume audience or message.

This gate does NOT apply to: reading content, editing existing presentations, template-based modifications, or content extraction.

## Quick Reference

| Task | Guide |
|------|-------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit or create from template | Read [references/editing.md](references/editing.md) |
| Create from scratch | Confirm HARD-GATE requirements → Read [references/pptxgenjs.md](references/pptxgenjs.md) + [references/style-guide.md](references/style-guide.md) |

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw X
