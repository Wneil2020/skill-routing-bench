---
name: compliance
description: "Use when the request concerns the compliance category of skills: covers compliance"
---

Grouping node for the 0 skills of the compliance category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **compliance-gate** (`compliance-gate/`): Use when Unified compliance quality gate that aggregates secret scanning, SAST (Bandit/Semgrep), dependency CVEs, IaC policy violations, and SBOM: covers compliance, gate, aggregates, bandit, cis
- **compliance-governance** (`compliance-governance/`): Use when Review data classification, access control policies, audit logging, and regulatory compliance documentation. Use when the user asks about data: covers compliance, governance, 감사, 리뷰, logging

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
