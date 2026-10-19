---
name: sefo-federation
description: "Use when Manage Federated Skill Evolution (FSE) operations, trigger gossip synchronization between instances, check federation sync status, resolve: covers sefo, federation, crdt, federated, forks"
metadata:
  holon-triggers: |
    sync skills across instances
    federation status
---

---
name: sefo-federation
description: >-
  Manage Federated Skill Evolution (FSE) operations: trigger gossip synchronization
  between instances, check federation sync status, resolve skill forks from CRDT
  conflicts, register peers, and promote skills across air-gapped environments.
  Use when the user asks to "sync skills across instances", "federation status",
  "resolve fork", "register peer", "gossip sync", "SEFO 페더레이션", "스킬 동기화",
  "포크 해결", "피어 등록", or any cross-instance skill management. Do NOT use for
  task routing (use sefo-orchestrator), trust/governance (use sefo-governance),
  or single-instance skill CRUD (use sefo skills API directly).
metadata:
  author: thaki
  version: "0.1.0"
  category: sefo
---

# SEFO Federation

Manage Federated Skill Evolution (FSE) across distributed orchestrator instances using CRDT merge semantics, gossip protocols, and fork-based conflict resolution.

## Instructions

### Operations

#### 1. Check Federation Status
Query `GET /api/v1/sefo/fse/status` to see:
- `peer_count`: Number of registered federation peers
- `pending_messages`: Gossip messages awaiting delivery
- `active_forks`: Unresolved skill forks from CRDT conflicts
- `convergence_estimate`: Progress toward full convergence (0.0 - 1.0)

#### 2. Register a New Peer
Register a federation peer: `POST /api/v1/sefo/fse/peers?peer_id=<uuid>&endpoint=<url>`

Peers are identified by UUID and communicate via HTTP gossip endpoints. For air-gapped environments, use offline gossip message export/import.

#### 3. Send Gossip Message
Share a skill with a peer: `POST /api/v1/sefo/fse/gossip` with:
```json
{
  "peer_id": "<sender-uuid>",
  "skill_name": "paper-review",
  "skill_data": {
    "grammar_rule": {...},
    "composition_dag": {...},
    "version": "1.2.0",
    "perf_stats": {...},
    "provenance_chain": [...]
  },
  "version_vector": {"peer-a": 3, "peer-b": 1}
}
```

The FSE module applies CRDT merge (Appendix B algorithm):
- **Remote dominates**: Accept remote ver
