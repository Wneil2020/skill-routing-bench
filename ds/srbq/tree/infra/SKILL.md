---
name: infra
description: "Use when the request concerns the infra category of skills: covers infra"
---

Grouping node for the 0 skills of the infra category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **infra-drift-detector** (`infra-drift-detector/`): Use when Detect infrastructure drift by comparing live cluster state against declared IaC (Helm releases, K8s manifests, Terraform state). Reports: covers infra, drift, detector, cluster, declared
- **infra-runbook-generator** (`infra-runbook-generator/`): Use when Generate infrastructure runbooks from Helm charts, K8s manifests, monitoring configs, and alert rules. Produces structured runbooks with: covers infra, runbook, generator, configs, paths

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
