---
name: workflow
description: "Use when the request concerns the workflow category of skills: covers workflow"
---

Grouping node for the 0 skills of the workflow category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **workflow-eval-opt** (`workflow-eval-opt/`): Use when Wrap any generation task in an evaluator-optimizer loop with defined quality criteria, iteration limits, and stopping conditions. Separates: covers eval, opt, checkers, deterministic, falls
- **workflow-miner** (`workflow-miner/`): Use when Mine agent transcript files (.jsonl) to discover frequent workflow patterns using Sequential Pattern Mining (SPM). Use when the user asks to "mine: covers miner, frequent, jsonl, mining, spm
- **workflow-parallel** (`workflow-parallel/`): Use when Fan out independent tasks to parallel subagents, aggregate results with a defined strategy (merge, vote, defer, union), and handle conflicts. Use: covers parallel, defer, fan, vote, union
- **workflow-sequential** (`workflow-sequential/`): Use when Execute a list of tasks in dependency order with checkpoints, error recovery, and conditional skipping. Use when the user: covers sequential, ordered, skipping, simultaneously, conditional

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
