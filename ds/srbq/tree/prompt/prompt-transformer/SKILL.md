---
name: prompt-transformer
description: "Use when Transform rough or casual prompts into professional-grade prompts with proper structure, clarity, and enforcement. Use when the user asks to: covers prompt, transformer, 프롬프트, 문서, casual"
metadata:
  holon-triggers: |
    transform a prompt
    improve a prompt
---

---
name: prompt-transformer
description: >-
  Transform rough or casual prompts into professional-grade prompts with proper
  structure, clarity, and enforcement. Use when the user asks to transform a
  prompt, improve a prompt, rewrite a prompt, upgrade a prompt, refine a prompt,
  make a prompt professional, or convert a prompt to expert quality. Supports
  system prompts, Cursor rules (.mdc), SKILL.md files, task instructions, and
  generic prompts. Do NOT use for creating new skills from scratch (use
  skill-creator) or writing documentation (use technical-writer). Korean
  triggers: "프롬프트", "문서", "스킬".
metadata:
  version: "1.0.0"
  category: "generation"
  author: "thaki"
---
# Prompt Transformer

Transform any rough prompt into a professional, unambiguous, and well-structured prompt.

## Transformation Workflow

Execute these 5 steps in order for every transformation.

### Step 1: Classify the Prompt Type

Determine exactly one type:

| Type | Indicators |
|------|-----------|
| **System Prompt** | Role assignment for LLM, behavioral instructions, output constraints |
| **Cursor Rule** | `.mdc` file, workspace or project conventions, AI assistant guidance |
| **SKILL.md** | Skill frontmatter (`name:`, `description:`), agent workflow instructions |
| **Task Instruction** | Specific one-time task, step-by-step procedure, code generation request |
| **Generic** | None of the above; general-purpose prompt |

If the user specifies a type via `--type`, use that instead.

### Step 2: Apply Structural Template

Apply the matching template from [references/templates.md](references/templates.md) for the classified prompt type. Each template provides the required sections and structure for that type. Preserve the user's original intent while restructuring.

### Step 3: Eliminate Ambiguity

Scan the prompt and apply these replacements:

| Vague Expression | Replacement |
|-----------------|-------------|
| "if possible" | "always" or remove the instruction entirely |
| 
