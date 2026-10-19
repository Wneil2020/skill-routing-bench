---
name: sentence-polisher
description: "Use when Bilingual (Korean + English) sentence quality checker that detects grammar errors, logical inconsistencies, tone misalignment: covers sentence, polisher, awkward, bilingual, honorific"
metadata:
  holon-triggers: |
    polish this text
    check grammar
---

---
name: sentence-polisher
description: >-
  Bilingual (Korean + English) sentence quality checker that detects grammar
  errors, logical inconsistencies, tone misalignment, awkward phrasing, and
  honorific/politeness level issues in Korean. Applies fixes automatically and
  returns polished text with a change summary. Designed as a final-stage
  refinement step for any text output pipeline. Based on pm-toolkit
  grammar-check methodology. Use when the user asks to "polish this text",
  "check grammar", "proofread", "sentence polish", "교정", "문장 교정", "문장
  다듬기", "문법 체크", "글 다듬어줘", or when invoked as a pipeline stage by
  other skills (e.g., gws-email-reply). Do NOT use for full document rewriting
  (use prompt-transformer), brand voice generation from scratch (use
  kwp-brand-voice-guideline-generation), or translation (handle directly).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "generation"
---
# Sentence Polisher

Bilingual (Korean + English) active text fixer. Unlike pm-toolkit `grammar-check` (which only suggests), this skill APPLIES fixes and returns polished text ready for use.

## Workflow

### Step 1: Detect Language

Identify the primary language of the input text:

| Detection | Mode |
|-----------|------|
| >80% Korean characters | Korean mode |
| >80% Latin characters | English mode |
| Mixed | Bilingual mode — apply both rulesets; scan ALL Korean segments for Konglish and ALL English segments for grammar |

### Step 2: Context Analysis

Identify before scanning:
- **Text purpose**: email reply, report, Slack message, presentation, documentation
- **Target audience**: internal team, external client, executive, technical peer
- **Expected tone**: formal (-합니다체), semi-formal (-해요체), casual (-하다체), diplomatic

If invoked by another skill (e.g., `gws-email-reply`), inherit the context from the caller.

### Step 3: Error Scan

Check 4 categories. For the full error taxonomy and examples, see [references/error-taxonomy.md](references/error-ta
