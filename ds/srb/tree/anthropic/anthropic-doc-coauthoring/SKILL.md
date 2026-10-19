---
name: anthropic-doc-coauthoring
description: "Use when Structured co-authoring workflow for documents. Use when user wants to write documentation, proposals, technical specs, decision docs, or: covers anthropic, doc, coauthoring, 문서 공동 작성, 스펙 작성"
metadata:
  holon-triggers: |
    user wants to write documentation
    proposals
---

---
name: anthropic-doc-coauthoring
description: >-
  Structured co-authoring workflow for documents. Use when user wants to write
  documentation, proposals, technical specs, decision docs, or similar
  structured content. This workflow helps users efficiently transfer context,
  refine content through iteration, and verify the doc works for readers. Do NOT
  use for Word document generation (use anthropic-docx) or PR/release notes (use
  pr-review-captain). Korean triggers: "문서 공동 작성", "스펙 작성".
metadata:
  author: "anthropic"
  version: "1.0.0"
  category: "document"
---
# Doc Co-Authoring Workflow

This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Testing.

## When to Offer This Workflow

**Trigger conditions:**
- User mentions writing documentation: "write a doc", "draft a proposal", "create a spec", "write up"
- User mentions specific doc types: "PRD", "design doc", "decision doc", "RFC"
- User seems to be starting a substantial writing task

**Initial offer:**
Offer the user a structured workflow for co-authoring the document. Explain the three stages:

1. **Context Gathering**: User provides all relevant context while Claude asks clarifying questions
2. **Refinement & Structure**: Iteratively build each section through brainstorming and editing
3. **Reader Testing**: Test the doc with a fresh Claude (no context) to catch blind spots before others read it

Explain that this approach helps ensure the doc works well when others read it (including when they paste it into Claude). Ask if they want to try this workflow or prefer to work freeform.

If user declines, work freeform. If user accepts, proceed to Stage 1.

## Stage 1: Context Gathering

**Goal:** Close the gap between what the user knows and what Claude knows, enabling smart guidance later.

### Initial Questions

Start by asking the user for
