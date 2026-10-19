---
name: sefo
description: "Use when the request concerns the sefo category of skills: covers sefo"
---

Grouping node for the 0 skills of the sefo category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **sefo-federation** (`sefo-federation/`): Use when Manage Federated Skill Evolution (FSE) operations, trigger gossip synchronization between instances, check federation sync status, resolve: covers sefo, federation, crdt, federated, forks
- **sefo-governance** (`sefo-governance/`): Use when Manage Trusted Skill Governance (TSG) operations, sign skills with Ed25519 cryptographic keys, verify provenance chains, check and: covers sefo, governance, cryptographic, ed25519, keypair
- **sefo-orchestrator** (`sefo-orchestrator/`): Use when Orchestrate complex tasks via SEFO's Skill-Aware Dynamic Orchestration (SADO) API. Decomposes tasks into optimal skill: covers sefo, orchestrator, compositions, constrained, decomposes

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
