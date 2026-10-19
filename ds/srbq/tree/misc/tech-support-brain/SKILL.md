---
name: tech-support-brain
description: "Use when --- description, Auto-classifies customer technical questions, searches knowledge graph for matches. High confidence (>0.8), auto-drafts: covers tech, support, brain, 기술 지원, 테크 지원 브레인"
metadata:
  holon-triggers: |
    tech support brain
    기술 지원
---

---
description: Auto-classifies customer technical questions, searches knowledge graph for matches. High confidence (>0.8): auto-drafts response. Low confidence: routes to specialist with context + customer history. Use when "tech support brain", "기술 지원", "customer question routing", "KB search". Do NOT use for known issue lookup (use cognee directly), ticket management (use Notion). Korean triggers: "기술 지원", "테크 지원 브레인", "고객 질문 라우팅".
---

# Tech Support Brain

## Overview
Intelligent routing and response system for customer technical questions. Classifies incoming questions, searches the knowledge graph for matches, auto-drafts responses for high-confidence matches (>0.8), and routes low-confidence cases to specialists with full context and customer history.

## Autonomy Level
**L3** — Semi-autonomous; high-confidence responses are drafted for human review; low-confidence routes to specialists.

## Pipeline Architecture
Sequential with branching: classify → KG search → if match (conf > 0.8): draft response → if not: route to specialist with context.

### Mermaid Diagram
```mermaid
flowchart LR
    A[Customer Question] --> B[Classify]
    B --> C[cognee KG Search]
    C --> D{Confidence > 0.8?}
    D -->|Yes| E[Draft Response]
    D -->|No| F[Route to Specialist]
    F --> G[Attach Context + History]
```

## Trigger Conditions
- Customer technical question (email, chat, ticket)
- "tech support brain", "기술 지원", "customer question routing", "KB search"
- `/tech-support-brain` with question text

## Skill Chain
| Step | Skill | Purpose |
|------|-------|---------|
| 1 | kwp-customer-support-ticket-triage | Classify question type, priority |
| 2 | kwp-customer-support-customer-research | Customer context, history |
| 3 | kwp-customer-support-response-drafting | Draft response for high-confidence match |
| 4 | kwp-customer-support-knowledge-management | KB article retrieval, update |
| 5 | cognee | Knowledge graph search for answer matching |

## Output Channels
- **Res
