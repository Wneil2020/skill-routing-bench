---
name: kwp-brand-voice-guideline-generation
description: "Use when This skill generates, creates, or builds brand voice guidelines from source materials. It should be used when the user asks to \"generate brand guidelines\": covers kwp, brand, voice, 빌드, 분석"
---

---
name: kwp-brand-voice-guideline-generation
description: >-
  This skill generates, creates, or builds brand voice guidelines from source
  materials. It should be used when the user asks to "generate brand
  guidelines", "create a style guide", "extract brand voice", "create guidelines
  from calls", "consolidate brand materials", "analyze my sales calls for brand
  voice", "build a brand playbook from documents", "synthesize a voice and tone
  guide", or uploads brand documents, transcripts, or meeting recordings for
  brand analysis. Also triggers when the user has a discovery report and wants
  to convert it into actionable guidelines. Do NOT use for tasks outside the
  brand-voice domain. Korean triggers: "빌드", "분석", "생성", "리포트".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Guideline Generation

Generate comprehensive, LLM-ready brand voice guidelines from any combination of sources — brand documents, sales call transcripts, discovery reports, or direct user input. Transform raw materials into structured, enforceable guidelines with confidence scoring and open questions.

## Inputs

Accept any combination of:
- **Discovery report** from the discover-brand skill (structured, pre-triaged)
- **Brand documents** uploaded or from connected platforms (PDF, PPTX, DOCX, MD, TXT)
- **Conversation transcripts** from Gong, Granola, manual uploads, or Notion meeting notes
- **Direct user input** about their brand voice and values

When a discovery report is provided, use it as the primary input — sources are already triaged and ranked. Supplement with additional analysis as needed.

## Generation Workflow

### 1. Identify and Classify Sources

Determine what the user has provided. If no sources are available:
- Check if a discovery report exists from a previous `/brand-voice:discover-brand` run
- Check `.claude/brand-voice.local.md` for known brand material locations
- Suggest running discovery first: `/brand-voice:discover-brand`

