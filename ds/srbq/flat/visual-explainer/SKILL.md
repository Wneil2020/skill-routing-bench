---
name: visual-explainer
description: "Use when Generate beautiful, self-contained HTML pages that visually explain systems, code changes, plans, and data. Use when the user asks for a diagram: covers visual, explainer, 리뷰, 생성, recap"
metadata:
  holon-triggers: |
    a diagram
    architecture overview
---

---
name: visual-explainer
description: >-
  Generate beautiful, self-contained HTML pages that visually explain systems,
  code changes, plans, and data. Use when the user asks for a diagram,
  architecture overview, diff review, plan review, project recap, comparison
  table, or any visual explanation. Also use proactively when about to render a
  complex ASCII table (4+ rows or 3+ columns). Do NOT use for simple text-only
  responses, static markdown formatting, or non-visual documentation. Korean
  triggers: "리뷰", "생성", "계획", "문서".
metadata:
  author: "nicobailon (ported by thaki)"
  version: "0.4.3"
  category: "execution"
---
# Visual Explainer

Generate self-contained HTML files for technical diagrams, visualizations, and data tables. Always open the result in the browser. Never fall back to ASCII art when this skill is loaded.

**Proactive table rendering.** When you're about to present tabular data as an ASCII box-drawing table in the terminal (comparisons, audits, feature matrices, status reports, any structured rows/columns), generate an HTML page instead. The threshold: if the table has 4+ rows or 3+ columns, it belongs in the browser. Don't wait for the user to ask — render it as HTML automatically and tell them the file path. You can still include a brief text summary in the chat, but the table itself should be the HTML page.

## HARD-GATE (Diagram & Slide Generation)

When generating a new diagram, visual plan, or slide deck (not diff-review, project-recap, or fact-check), do NOT start generating until these are confirmed:

1. **Subject matter** — What system, concept, or data is being visualized?
2. **Target audience** — Developers? PMs? Executives? (determines information density)

If the user's request is vague (e.g., "make a diagram"), ASK what to visualize and for whom before proceeding. Do not guess the subject matter.

This gate does NOT apply to: diff-review, plan-review, project-recap, fact-check, or proactive table rendering (these have suff
