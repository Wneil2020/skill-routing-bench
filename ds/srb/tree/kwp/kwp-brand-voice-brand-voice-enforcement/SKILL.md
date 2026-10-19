---
name: kwp-brand-voice-brand-voice-enforcement
description: "Use when This skill applies brand guidelines to content creation. It should be used when the user asks to \"write an email\", \"draft a proposal\", \"create a pitch: covers kwp, brand, voice, 생성, 이메일"
---

---
name: kwp-brand-voice-brand-voice-enforcement
description: >-
  This skill applies brand guidelines to content creation. It should be used
  when the user asks to "write an email", "draft a proposal", "create a pitch
  deck", "write a LinkedIn post", "draft a presentation", "write a Slack
  message", "draft sales content", or any content creation request where brand
  voice should be applied. Also triggers on "on-brand", "brand voice", "enforce
  voice", "apply brand guidelines", "brand-aligned content", "write in our
  voice", "use our brand tone", "make this sound like us", "rewrite this in our
  tone", or "this doesn't sound on-brand". Not for generating guidelines from
  scratch (use guideline-generation) or discovering brand materials (use
  discover-brand). Do NOT use for tasks outside the brand-voice domain. Korean
  triggers: "생성", "이메일", "프레젠테이션", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Brand Voice Enforcement

Apply existing brand guidelines to all sales and marketing content generation. Load the user's brand guidelines, apply voice constants and tone flexes to the content request, validate output, and explain brand choices.

## Loading Brand Guidelines

Find the user's brand guidelines using this sequence. Stop as soon as you find them:

1. **Session context** — Check if brand guidelines were generated earlier in this session (via `/brand-voice:generate-guidelines`). If so, they are already in the conversation. Use them directly. Session-generated guidelines are the freshest and reflect the user's most recent intent.

2. **Local guidelines file** — Check for `.claude/brand-voice-guidelines.md` inside the user's working folder. Do NOT use a relative path from the agent's current working directory — in Cowork, the agent runs from a plugin cache directory, not the user's project. Resolve the path relative to the user's working folder. If no working folder is set, skip this step.

3. **Ask the user** — If 
