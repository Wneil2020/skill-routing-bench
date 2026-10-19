---
name: nlm-deep-learn
description: "Use when Accelerated learning pipeline, upload sources to NotebookLM, extract core mental models, map expert disagreements and consensus, run: covers nlm, deep, learn, accelerated, deeply"
metadata:
  holon-triggers: |
    deep learn
    accelerated learning
---

---
name: nlm-deep-learn
description: >-
  Accelerated learning pipeline: upload sources to NotebookLM, extract core
  mental models, map expert disagreements and consensus, run deep-understanding
  quizzes with gap analysis, generate study artifacts (debate podcast,
  flashcards, quiz, mind map, study guide).
  Use when the user asks to "deep learn", "accelerated learning",
  "compress learning", "mental models for", "48-hour learning",
  "NLM deep learn", "가속 학습", "멘탈 모델 추출", "심층 이해 퀴즈",
  or any request to deeply learn a subject using NotebookLM.
  Do NOT use for ad-hoc studio_create -- use notebooklm-studio.
  Do NOT use for product discovery -- use nlm-discovery-lab.
  Do NOT use for local StudyVault quizzing -- use docs-tutor.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# NLM Deep Learn: Accelerated Learning Pipeline

Compress a semester of learning into hours. Mass-upload source materials to NotebookLM, extract the mental models experts share, map the intellectual landscape of debates and consensus, then test deep understanding through interactive quizzes powered by the full corpus. The difference between a semester and 48 hours isn't the amount of content — it's knowing which questions to ask.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- At least one source material (PDF, URL, or text) — more sources produce richer results

## System Prompt

The intellectual landscape document rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before Phase 4. It defines:

- Socratic, depth-first tone for each language
- Structure: Mental Models -> Debates -> Consensus -> Open Questions -> Study Path
- EN + KO bilingual rules
- Quality gates for depth vs. surface-level summarization

## Question Rules

Deep understanding question design rules are stored at `references/question-rules.md` (relative to this skill). Read it before Phase 5. It d
