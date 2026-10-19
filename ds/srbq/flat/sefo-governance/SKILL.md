---
name: sefo-governance
description: "Use when Manage Trusted Skill Governance (TSG) operations, sign skills with Ed25519 cryptographic keys, verify provenance chains, check and: covers sefo, governance, cryptographic, ed25519, keypair"
metadata:
  holon-triggers: |
    sign a skill
    verify provenance
---

---
name: sefo-governance
description: >-
  Manage Trusted Skill Governance (TSG) operations: sign skills with Ed25519
  cryptographic keys, verify provenance chains, check and update trust scores,
  scan for threats, apply differential privacy to statistics, and manage
  quarantine. Use when the user asks to "sign a skill", "verify provenance",
  "check trust scores", "generate keypair", "threat scan", "SEFO 거버넌스",
  "스킬 서명", "신뢰 점수", "위협 탐지", "프로비넌스 검증", or any trust and
  security operation on skills. Do NOT use for task routing (use sefo-orchestrator),
  federation sync (use sefo-federation), or general security review (use
  security-expert).
metadata:
  author: thaki
  version: "0.1.0"
  category: sefo
---

# SEFO Governance

Manage Trusted Skill Governance (TSG) for cryptographic integrity, Bayesian trust scoring, differential privacy, and threat detection across the skill ecosystem.

## Instructions

### Operations

#### 1. Generate Keypair
Create a new Ed25519 keypair for signing skills:
`POST /api/v1/sefo/tsg/keypair`

Returns `private_key_hex` and `public_key_hex`. Store the private key securely — it signs all skills from this orchestrator instance.

#### 2. Sign a Skill
After creating or modifying a skill, sign it to establish provenance:
`POST /api/v1/sefo/tsg/sign` with:
```json
{
  "skill_id": "<uuid>",
  "private_key_hex": "<hex>",
  "orchestrator_id": "local-instance"
}
```

This computes `Sign(sk, H(grammar_rule || composition_dag || version))` and extends the Merkle-linked provenance chain.

#### 3. Verify Skill Integrity
Before trusting a skill (especially from federation):
`POST /api/v1/sefo/tsg/verify` with:
```json
{
  "skill_id": "<uuid>",
  "public_key_hex": "<hex>"
}
```

Returns:
- `signature_valid`: Whether the Ed25519 signature matches
- `provenance_valid`: Whether the Merkle chain is intact
- `provenance_issues`: Specific chain integrity failures
- `threat_alerts`: Detected threats (poisoning, manipulation, etc.)

#### 4. Check Trust Sc
