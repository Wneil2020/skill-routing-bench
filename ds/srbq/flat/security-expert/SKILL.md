---
name: security-expert
description: "Use when Perform threat modeling (STRIDE), vulnerability assessments (OWASP Top 10), secret detection, LLM/AI-specific security checks, and PII handling: covers security, expert, 보안, 감사, assessments"
metadata:
  holon-triggers: |
    a security review
    threat model
---

---
name: security-expert
description: >-
  Perform threat modeling (STRIDE), vulnerability assessments (OWASP Top 10),
  secret detection, LLM/AI-specific security checks, and PII handling reviews.
  Use when the user asks for a security review, threat model, vulnerability
  scan, or secret audit. Do NOT use for data governance or regulatory compliance
  documentation (use compliance-governance) or dependency CVE scanning only (use
  dependency-auditor). Korean triggers: "보안", "감사", "리뷰", "체크".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Security Expert

Procedural security skill for a FastAPI microservices platform with LLM inference, RAG, PII redaction, and multi-tenant architecture.

## Threat Modeling (STRIDE)

For each component or feature under review, evaluate:

| Threat | Question | Example in this system |
|--------|----------|----------------------|
| **S**poofing | Can an attacker impersonate a user/service? | JWT forgery, service-to-service auth bypass |
| **T**ampering | Can data be modified in transit/at rest? | WebSocket message injection, DB record tampering |
| **R**epudiation | Can actions be denied without evidence? | Missing audit logs in admin service |
| **I**nformation Disclosure | Can sensitive data leak? | PII in logs, model config in error responses |
| **D**enial of Service | Can the service be overwhelmed? | Unbounded file upload, missing rate limits |
| **E**levation of Privilege | Can a user gain unauthorized access? | Tenant isolation bypass, role escalation |

## OWASP Top 10 Checklist

- [ ] **A01 Broken Access Control**: Verify RBAC enforcement, tenant isolation, CORS policy
- [ ] **A02 Cryptographic Failures**: TLS everywhere, passwords hashed (bcrypt/argon2), secrets not in code
- [ ] **A03 Injection**: SQL (parameterized queries), command injection, template injection
- [ ] **A04 Insecure Design**: Threat model exists, abuse cases considered, rate limiting
- [ ] **A05 Security Misconfiguration**: De
