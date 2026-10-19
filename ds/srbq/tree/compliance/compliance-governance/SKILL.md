---
name: compliance-governance
description: "Use when Review data classification, access control policies, audit logging, and regulatory compliance documentation. Use when the user asks about data: covers compliance, governance, 감사, 리뷰, logging"
metadata:
  holon-triggers: |
    compliance audits
    access control reviews
---

---
name: compliance-governance
description: >-
  Review data classification, access control policies, audit logging, and
  regulatory compliance documentation. Use when the user asks about data
  governance, compliance audits, access control reviews, GDPR, SOC2, or policy
  documentation. Do NOT use for vulnerability scanning or threat modeling (use
  security-expert) or general code review (use backend-expert). Korean triggers:
  "감사", "리뷰", "스캔", "보안".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Compliance & Governance

Review governance posture for a multi-tenant SaaS platform with LLM/AI capabilities. Key services: `admin` (8018), `pii-redaction` (8021), `analytics` (8022).

## Data Classification

### Classification Levels

| Level | Definition | Examples in this system | Handling |
|-------|-----------|----------------------|---------|
| **Restricted** | Regulatory/legal protection required | PII, call recordings, auth tokens | Encrypted at rest + transit, access logged, retention enforced |
| **Confidential** | Business-sensitive | Tenant configs, model parameters, analytics | Encrypted at rest, role-restricted access |
| **Internal** | Internal use only | Service logs, deployment configs | Access restricted to team, no public exposure |
| **Public** | No restrictions | API docs, public-facing UI content | No special handling |

### Review Checklist

- [ ] Each data store has a classification label
- [ ] Restricted data encrypted at rest (PostgreSQL TDE or column-level)
- [ ] Restricted data encrypted in transit (TLS 1.2+)
- [ ] Data classification documented per service

## Access Control Review

### RBAC Audit

- [ ] Roles defined and documented (admin, manager, agent, viewer)
- [ ] Role assignments follow least-privilege principle
- [ ] Service-to-service auth uses mTLS or signed tokens (not shared secrets)
- [ ] API endpoints enforce authorization (not just authentication)
- [ ] Admin endpoints restricted to admin role only

