---
name: executive-briefing
description: "Use when Synthesize multiple role-perspective analysis documents into a unified CEO executive briefing report in Korean. Identifies: covers executive, briefing, CEO 종합 보고서, 경영진 브리핑, collecting"
metadata:
  holon-triggers: |
    create executive briefing
    CEO 종합 보고서
---

---
name: executive-briefing
description: >
  Synthesize multiple role-perspective analysis documents into a unified CEO executive briefing
  report in Korean. Identifies cross-role consensus, conflicting perspectives, prioritized action
  items, and a risk matrix. Outputs structured markdown and a .docx executive summary.
  Composes agency-executive-summary-generator, anthropic-docx, and visual-explainer.
  Use when the role-dispatcher invokes this skill after collecting role analyses, or when the
  user asks to "create executive briefing", "CEO 종합 보고서", "경영진 브리핑 생성",
  "synthesize role analyses", "cross-role summary".
  Do NOT use for single-role analysis (use the specific role-{name} skill), daily morning
  briefing (use morning-ship), or investor presentation (use presentation-strategist).
  Korean triggers: "CEO 종합 보고서", "경영진 브리핑", "직무별 종합".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "synthesis"
---

# Executive Briefing Generator

Synthesizes analysis documents from multiple role-perspective skills into a comprehensive
CEO executive briefing with cross-functional insights, consensus mapping, and prioritized actions.

## Input Requirements

This skill expects a collection of role-perspective analysis documents, each following this structure:
- Role name and relevance score
- Executive summary bullets
- Detailed domain-specific analysis
- Risks & concerns
- Recommendations

Documents are typically located in `outputs/role-analysis/{topic-slug}/` or passed as context.

## Synthesis Pipeline

Execute sequentially:

### Phase 1: Content Aggregation
- Collect all role-perspective documents
- Record participation: which roles analyzed (relevance >= 5) vs skipped
- Extract key findings, risks, and recommendations from each

### Phase 2: Cross-Role Analysis (via `agency-executive-summary-generator`)
Apply McKinsey SCQA framework:
- **Situation**: Topic context and scope
- **Complication**: Key tensions revealed by cross-role analysis
- **Question**: Wha
