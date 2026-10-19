---
name: skill
description: "Use when the request concerns the skill category of skills: covers skill"
---

Grouping node for the 0 skills of the skill category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **skill-autoimprove** (`skill-autoimprove/`): Use when Autonomously optimize any existing skill's prompt by running it repeatedly, scoring outputs against binary evals, mutating one: covers autoimprove, autoresearch, binary, improved, karpathy
- **skill-composer** (`skill-composer/`): Use when Converts natural language workflow descriptions into persistent, reusable skill chains. Use when the user wants to define workflows: covers composer, agentos, modular, descriptions, reusable
- **skill-guide-generator** (`skill-guide-generator/`): Use when Scan all installed skills, identify undocumented ones, generate guide documentation following the standard template, and update the README: covers guide, generator, ensure, following, readme
- **skill-optimizer** (`skill-optimizer/`): Use when Audit, evaluate, benchmark, and compare existing agent skills (SKILL.md files) for quality assurance. Use when the user asks to "optimize: covers optimizer, 스킬, 감사, effectiveness, assurance
- **skill-seekers** (`skill-seekers/`): Use when Convert documentation sites, GitHub repos, PDFs, and videos into structured Cursor skill files with conflict detection. Use when converting external: covers seekers, 스킬, 빌드, registry, built

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
