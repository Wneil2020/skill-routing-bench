---
name: kwp-brand-voice-discover-brand
description: "Use when This skill orchestrates autonomous discovery of brand materials across enterprise platforms (Notion, Confluence, Google Drive, Box, SharePoint, Figma, Gong: covers kwp, brand, voice, 감사, 검색"
---

---
name: kwp-brand-voice-discover-brand
description: >-
  This skill orchestrates autonomous discovery of brand materials across
  enterprise platforms (Notion, Confluence, Google Drive, Box, SharePoint,
  Figma, Gong, Granola, Slack). It should be used when the user asks to
  "discover brand materials", "find brand documents", "search for brand
  guidelines", "audit brand content", "what brand materials do we have", "find
  our style guide", "where are our brand docs", "do we have a style guide",
  "discover brand voice", "brand content audit", or "find brand assets". Do NOT
  use for tasks outside the brand-voice domain. Korean triggers: "감사", "검색",
  "문서", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Brand Discovery

Orchestrate autonomous discovery of brand materials across enterprise platforms. This skill coordinates the discover-brand agent to search connected platforms (Notion, Confluence, Google Drive, Box, Microsoft 365, Figma, Gong, Granola, Slack), triage sources, and produce a structured discovery report with open questions.

## Discovery Workflow

### 0. Orient the User

Before starting, briefly explain what's about to happen so the user knows what to expect:

"Here's how brand discovery works:

1. **Search** — I'll search your connected platforms (Notion, Google Drive, Slack, etc.) for brand-related materials: style guides, pitch decks, templates, transcripts, and more.
2. **Analyze** — I'll categorize and rank what I find, pull the best sources, and produce a discovery report with what I found, any conflicts, and open questions.
3. **Generate guidelines** — Once you've reviewed the report, I can generate a structured brand voice guideline document from the results.
4. **Save** — Guidelines are saved to `.claude/brand-voice-guidelines.md` in your working folder once you approve them. Nothing is written until that step.

The search usually takes a few minutes depending on how many platforms are connected. Re
