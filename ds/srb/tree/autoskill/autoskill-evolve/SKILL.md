---
name: autoskill-evolve
description: "Use when End-to-end skill evolution pipeline, extract candidates from agent transcripts, judge each against existing skills, apply: covers autoskill, evolve, discard, manually, recalling"
metadata:
  holon-triggers: |
    evolve skills
    run autoskill evolution
---

---
name: autoskill-evolve
description: >-
  End-to-end skill evolution pipeline: extract candidates from agent transcripts,
  judge each against existing skills, apply add/merge/discard. Use when the user
  asks to "evolve skills", "run autoskill evolution", "mine sessions for skills",
  "autoskill evolve", "스킬 진화", "세션 기반 스킬 진화", "transcripts to skills",
  or when triggered by /autoskill-evolve. Do NOT use for creating skills
  manually (use create-skill), auditing skills (use skill-optimizer), or
  recalling session context (use recall).
metadata:
  author: thaki
  version: "0.2.0"
  category: self-improvement
---

# AutoSkill Evolve

End-to-end skill evolution pipeline that extracts reusable skill candidates from agent transcripts, judges each against the existing skill ecosystem, and applies add/merge/discard decisions. Optionally mines workflow patterns, composes workflow-type skills, validates security, and tracks intent alignment. Orchestrates autoskill-extractor, autoskill-judge, autoskill-merger, workflow-miner, skill-composer, semantic-guard, and intent-alignment-tracker.

## Instructions

### Pipeline Overview

```
Transcripts → [Mine Patterns] → Extract → Judge → [Compose/Merge] → Guard → Report (+IA)
```

### Step 1: Scope Selection

Determine which transcripts to process based on the `--scope` flag:

- `recent` (default): Process the 5 most recent transcripts not yet indexed
- `all`: Process all unindexed transcripts (use with caution)
- `session <uuid>`: Process a specific session transcript

Track processed transcripts in `.cursor/hooks/state/autoskill-evolution.json`:
```json
{
  "last_processed": "2026-03-14T10:00:00Z",
  "processed_transcripts": ["uuid1", "uuid2"],
  "evolution_count": 42,
  "skills_created": 12,
  "skills_merged": 28,
  "skills_discarded": 15
}
```

### Step 1.5: Pattern Discovery (workflow-miner, optional)

When `--with-mining` is set:
1. Read `.cursor/skills/workflow-miner/SKILL.md` and run mining on the same transcript scope

