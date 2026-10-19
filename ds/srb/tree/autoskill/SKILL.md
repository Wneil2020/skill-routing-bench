---
name: autoskill
description: "Use when the request concerns the autoskill category of skills: covers autoskill"
---

Grouping node for the 0 skills of the autoskill category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **autoskill-evolve** (`autoskill-evolve/`): Use when End-to-end skill evolution pipeline, extract candidates from agent transcripts, judge each against existing skills, apply: covers autoskill, evolve, discard, manually, recalling
- **autoskill-extractor** (`autoskill-extractor/`): Use when Extract reusable skill candidates from Cursor agent transcripts by analyzing user interaction patterns, corrections, and: covers autoskill, extractor, durable, preferences, corrections
- **autoskill-judge** (`autoskill-judge/`): Use when Evaluate skill candidates produced by autoskill-extractor and decide whether each should be added, merged into an existing skill, or: covers autoskill, judge, discarded, produced, added
- **autoskill-merger** (`autoskill-merger/`): Use when Merge a skill candidate into an existing skill with semantic union of constraints, triggers, and tags. Use when autoskill-judge returns a: covers autoskill, merger, tags, union, candidate
- **autoskill-pipeline** (`autoskill-pipeline/`): Use when Orchestrates the full AutoSkill adaptation, research analysis, multi-role strategy, skill creation, infrastructure, QA. Use when the: covers autoskill, pipeline, adaptation, adapt, evolution

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
