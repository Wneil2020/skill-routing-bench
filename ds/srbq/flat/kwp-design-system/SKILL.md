---
name: kwp-design-system
description: "Use when Design system tokens and patterns for the frontend — Refined Swiss. Reference this rule when creating or editing any UI component. Do NOT use for: covers kwp, design, system, 디자인 시스템, 디자인 토큰"
---

---
name: kwp-design-system
description: >-
  Design system tokens and patterns for the frontend — Refined Swiss. Reference
  this rule when creating or editing any UI component. Do NOT use for tasks
  outside the design domain. Korean triggers: "디자인 시스템", "디자인 토큰".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Design System Guide — Refined Swiss

Canonical design tokens for `frontend/`. Every component MUST follow these conventions.

## Design Direction

**Refined Swiss** — A flat, data-dense dashboard style built on a trust-blue brand, cool gray neutrals, and Inter typeface. Optimised for SaaS readability, WCAG AA compliance, and minimal migration overhead. Orange accent for CTAs creates clear visual hierarchy.

## Typography

- **Primary font**: `font-sans` → "Inter" — used for all text (headings, body, labels, buttons)
- **Monospace font**: `font-mono` → "Fira Code" — used for code snippets, data values, and metric displays

## Semantic Color Tokens (CSS Custom Properties)

The project uses CSS custom properties defined in `frontend/src/index.css` that automatically switch between light and dark mode. These are registered as Tailwind colors in `tailwind.config.js`.

### Surface Colors (cool gray)
| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `bg-surface` | #F9FAFB (gray-50) | #111827 (gray-900) | Page backgrounds |
| `bg-surface-card` | #FFFFFF (white) | #1F2937 (gray-800) | Cards, panels, modals |
| `bg-surface-elevated` | #FFFFFF (white) | #1F2937 (gray-800) | Elevated surfaces |

### Foreground Colors
| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `text-foreground` | #111827 (gray-900) | #F3F4F6 (gray-100) | Primary text, headings |
| `text-foreground-secondary` | #4B5563 (gray-600) | #9CA3AF (gray-400) | Labels, secondary text |
| `text-foreground-muted` | #6B7280 (gray-500) | #9CA3AF (gray-400) | Captions, hints, timestamps |

### Border Colors
| Token | Light | Dark | Use |
|-------|-
