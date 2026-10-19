---
name: role-ux-designer
description: "Use when Analyze a given topic from the UX Designer perspective — user experience impact, accessibility concerns, design system consistency, user: covers role, designer, UX 관점, 디자이너 분석, critique"
metadata:
  holon-triggers: |
    UX perspective
    UX 관점
---

---
name: role-ux-designer
description: >
  Analyze a given topic from the UX Designer perspective — user experience impact, accessibility
  concerns, design system consistency, user research needs, and design handoff requirements.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes ux-expert, kwp-design-user-research, kwp-design-design-critique,
  kwp-design-accessibility-review, kwp-design-design-system-management,
  workflow-miner, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "UX perspective", "UX 관점", "디자이너 분석", "user experience impact".
  Do NOT use for conducting a full UX audit (use ux-expert), design system token management
  (use kwp-design-design-system-management), or writing UX copy (use kwp-design-ux-writing).
  Korean triggers: "UX 관점", "디자이너 분석", "사용자 경험 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# UX Designer Perspective Analyzer

Analyzes any business topic from the UX Designer's viewpoint, covering user experience impact,
interface changes, accessibility compliance, design system consistency, and user research needs.

## Relevance Criteria

Score the topic 1-10 based on overlap with UX concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| User interface | High | UI, dashboard, page, screen, component, layout, navigation |
| User experience | High | flow, journey, onboarding, usability, friction, delight |
| Accessibility | High | WCAG, screen reader, keyboard, contrast, a11y |
| Design system | High | token, component library, consistency, pattern, Figma |
| User research | Medium | persona, interview, usability test, feedback, survey |
| Internationalization | Medium | i18n, locale, RTL, translation, multilingual |
| Content & copy | Medium | microcopy, error message, empty state, label |
| Performance (perceived) | Medium | loading, skeleton, ani
