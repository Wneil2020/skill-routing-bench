---
name: role-security-engineer
description: "Use when Analyze a given topic from the Security Engineer perspective — threat modeling (STRIDE), vulnerability assessment (OWASP Top 10): covers role, security, engineer, 보안 관점, 보안 엔지니어 분석"
metadata:
  holon-triggers: |
    security perspective
    보안 관점
---

---
name: role-security-engineer
description: >
  Analyze a given topic from the Security Engineer perspective — threat modeling (STRIDE),
  vulnerability assessment (OWASP Top 10), compliance impact, incident readiness, and
  access control implications. Scores topic relevance (1-10) and produces a structured
  Korean analysis document when relevant (>= 5).   Composes security-expert, compliance-governance, dependency-auditor,
  kwp-operations-risk-assessment, workflow-miner, semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "security perspective", "보안 관점", "보안 엔지니어 분석", "threat analysis".
  Do NOT use for running a full security audit (use security-expert), dependency CVE scanning
  (use dependency-auditor), or incident response (use incident-to-improvement).
  Korean triggers: "보안 관점", "보안 엔지니어 분석", "위협 분석".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# Security Engineer Perspective Analyzer

Analyzes any business topic from the Security Engineer's viewpoint, covering threat modeling,
vulnerability exposure, compliance requirements, data protection, and incident preparedness.

## Relevance Criteria

Score the topic 1-10 based on overlap with security concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Authentication & authorization | High | auth, login, JWT, RBAC, ABAC, session, token |
| Data protection | High | PII, encryption, data classification, GDPR, privacy |
| Vulnerability & threats | High | CVE, OWASP, injection, XSS, CSRF, SSRF |
| API security | High | rate limit, input validation, API key, endpoint exposure |
| Compliance & audit | High | SOC 2, ISO 27001, audit log, regulatory |
| Infrastructure security | Medium | network, firewall, container, K8s, secrets management |
| Dependency security | Medium | supply chain, package, CVE scan, SCA |
| Incident response | Medium | breach, incident, forensics, recov
