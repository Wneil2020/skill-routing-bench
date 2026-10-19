---
name: ux-expert
description: "Use when Conduct UX audits, heuristic evaluations (Nielsen's 10), accessibility checks (WCAG 2.1 AA), and design-system consistency reviews. Use when the user: covers expert, 감사, 리뷰, nielsen, conduct"
metadata:
  holon-triggers: |
    a UX review
    usability analysis
---

---
name: ux-expert
description: >-
  Conduct UX audits, heuristic evaluations (Nielsen's 10), accessibility checks
  (WCAG 2.1 AA), and design-system consistency reviews. Use when the user asks
  for a UX review, usability analysis, accessibility audit, or design-system
  alignment check. Do NOT use for building or implementing UI components (use
  frontend-design), checking Web Interface Guidelines compliance (use
  web-design-guidelines), or frontend code review (use frontend-expert). Korean
  triggers: "감사", "리뷰", "빌드", "설계".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# UX Expert

Perform user-experience reviews for a React 18 + Tailwind CSS + Zustand application. The frontend lives at `frontend/`.

## Review Workflow

1. **Scope** — Identify the pages/components under review.
2. **Heuristic Evaluation** — Apply Nielsen's 10 usability heuristics.
3. **Accessibility Audit** — Check WCAG 2.1 Level AA compliance.
4. **Design-System Consistency** — Verify Tailwind token usage, component naming, and spacing/color consistency.
5. **User-Flow Analysis** — Trace critical paths (happy path + error states).
6. **Report** — Produce the structured output below.

## Heuristic Checklist

| # | Heuristic | What to check |
|---|-----------|---------------|
| 1 | Visibility of system status | Loading states, progress indicators, toast feedback |
| 2 | Match between system and real world | Domain language, icons, metaphors |
| 3 | User control and freedom | Undo/redo, cancel, back navigation |
| 4 | Consistency and standards | Tailwind design tokens, component library reuse |
| 5 | Error prevention | Form validation, confirmation dialogs, disabled states |
| 6 | Recognition over recall | Labels, placeholders, breadcrumbs |
| 7 | Flexibility and efficiency | Keyboard shortcuts, power-user paths |
| 8 | Aesthetic and minimalist design | Visual noise, information density |
| 9 | Help users recover from errors | Error messages with guidance, retry actions
