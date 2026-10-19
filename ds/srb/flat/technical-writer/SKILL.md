---
name: technical-writer
description: "Use when Author Architecture Decision Records (ADRs), API documentation, operational guides, and changelogs. Use when the user asks to document a design: covers technical, writer, 리뷰, 생성, adr"
metadata:
  holon-triggers: |
    document a design decision
    write an ADR
---

---
name: technical-writer
description: >-
  Author Architecture Decision Records (ADRs), API documentation, operational
  guides, and changelogs. Use when the user asks to document a design decision,
  write an ADR, generate a changelog, or create operational documentation. Do
  NOT use for PR summaries or release notes (use pr-review-captain) or prompt
  engineering (use prompt-transformer). Korean triggers: "리뷰", "생성", "설계",
  "릴리즈".
metadata:
  version: "1.0.0"
  category: "generation"
  author: "thaki"
---
# Technical Writer

Produce clear, structured documentation for the realtime-agent-copilot platform. Documentation lives at `docs/`.

## ADR (Architecture Decision Record)

### When to Write

- New technology adopted or replaced
- Architectural pattern chosen (e.g., event-driven vs request-response)
- Significant trade-off decision made
- Infrastructure change (new service, DB choice, deployment model)

### Process

1. **Create** ADR using the template at [templates/adr-template.md](templates/adr-template.md)
2. **Number** sequentially: `docs/09-decisions-guidelines/adr/NNNN-title-in-kebab-case.md`
3. **Status** lifecycle: `Proposed` → `Accepted` → (`Deprecated` | `Superseded by ADR-NNNN`)
4. **Review** with at least one team member before merging

### Writing Guidelines

- **Context**: State the problem and constraints objectively
- **Decision**: Be specific about what was chosen
- **Consequences**: List both positive and negative outcomes
- **Alternatives**: Document what was considered and why it was rejected
- Keep each section concise (3-5 bullet points)

## API Documentation

### Format

Follow OpenAPI 3.1 conventions. For each endpoint document:

```markdown
### POST /api/v1/resources

Create a new resource.

**Request Body** (application/json):
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Resource name (1-255 chars) |
| tenant_id | string | Yes | Tenant UUID |

**Response** (201 Created):

