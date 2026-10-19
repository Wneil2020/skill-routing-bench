---
name: pm-toolkit
description: "Use when PM utility skills, resume review against PM best practices, NDA drafting, privacy policy generation, and grammar/flow checking. Based on: covers toolkit, 이력서 검토, PM 이력서, grammar, utility"
metadata:
  holon-triggers: |
    review resume
    draft NDA
---

---
name: pm-toolkit
description: >-
  PM utility skills: resume review against PM best practices, NDA drafting,
  privacy policy generation, and grammar/flow checking. Based on
  phuryn/pm-skills. Use when the user asks for "review resume", "draft NDA",
  "privacy policy", "grammar check", "proofread", or "PM resume review". Do NOT
  use for legal contract review (use kwp-legal-contract-review), general
  documentation (use technical-writer), or marketing content (use
  kwp-marketing-content-creation). Korean triggers: "이력서 검토", "PM 이력서",
  "NDA 초안", "개인정보처리방침", "문법 교정", "교정", "이력서 맞춤화", "컴플라이언스".
metadata:
  author: "thaki"
  version: "1.0.0"
  upstream: "https://github.com/phuryn/pm-skills"
  category: "product"
---
# PM Toolkit

PM utility skills for resume review, NDA drafting, privacy policy generation, and grammar/flow checking. Each sub-skill has a reference file with full instructions.

## Sub-Skill Index

| Sub-Skill        | Reference              | Triggers                                                                 |
|------------------|------------------------|--------------------------------------------------------------------------|
| draft-nda        | [references/draft-nda.md](references/draft-nda.md) | draft NDA, confidentiality agreement, NDA template                       |
| grammar-check    | [references/grammar-check.md](references/grammar-check.md) | grammar check, proofread, fix typos, writing review                      |
| privacy-policy   | [references/privacy-policy.md](references/privacy-policy.md) | privacy policy, data protection policy, GDPR policy, CCPA                 |
| review-resume    | [references/review-resume.md](references/review-resume.md) | review PM resume, resume feedback, PM job application, tailor resume     |

## Workflow

1. **Identify sub-skill**: Match user intent to one of the four sub-skills above.
2. **Read reference**: Load the corresponding `references/<name>.md` for full instructions, input arguments, a
