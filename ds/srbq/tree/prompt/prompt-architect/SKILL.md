---
name: prompt-architect
description: "Use when Analyze prompts and restructure them using 8 research-backed frameworks (CO-STAR, RISEN, RISE-IE, RISE-IX, TIDD-EC, RTF, Chain of: covers prompt, architect, density, restructure, rise"
metadata:
  holon-triggers: |
    architect a prompt
    structure my prompt
---

---
name: prompt-architect
description: >-
  Analyze prompts and restructure them using 8 research-backed frameworks
  (CO-STAR, RISEN, RISE-IE, RISE-IX, TIDD-EC, RTF, Chain of Thought, Chain of
  Density). Provides framework recommendations, quality scoring, targeted
  clarifying questions, and iterative refinement. Use when the user asks to
  "architect a prompt", "structure my prompt", "which framework for this
  prompt", "improve prompt with CO-STAR", "RISEN framework", "프롬프트 설계", "프레임워크
  추천", or any framework-specific prompt design request. Do NOT use for general
  prompt polishing without framework selection (use prompt-transformer),
  creating new skills (use skill-creator), or writing documentation (use
  technical-writer).
metadata:
  author: "thaki"
  version: "1.0.0"
  source: "https://github.com/ckelsoe/claude-skill-prompt-architect"
  category: "execution"
---
# Prompt Architect — Framework-Based Prompt Design

Transform vague or incomplete prompts into well-structured, effective prompts by selecting and applying the right prompting framework.

## Workflow

Execute these 6 steps for every prompt architecture request.

### Step 1: Analyze the Original Prompt

Score the prompt across 5 dimensions (1-10 each):

| Dimension | Score 1-3 | Score 4-6 | Score 7-10 |
|-----------|-----------|-----------|------------|
| **Clarity** | Vague goal, ambiguous pronouns | Basic goal stated, some ambiguity | Clear, unambiguous, single interpretation |
| **Specificity** | Under 5 words, no details | Some details, missing specs | Quantified, named entities, format specs |
| **Context** | No background at all | Some situational info | Rich background, constraints, history |
| **Completeness** | Missing what/why/how/format | Has 1-2 of the four elements | All four elements present |
| **Structure** | Single sentence, no organization | Multi-sentence, basic flow | Sections, bullets, logical hierarchy |

Calculate overall = average of all 5. Present the scorecard to the user
