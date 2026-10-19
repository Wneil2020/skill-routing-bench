---
name: kwp-productivity-memory-management
description: "Use when Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal: covers kwp, productivity, memory, acronyms, collaborator"
---

---
name: kwp-productivity-memory-management
description: >-
  Two-tier memory system that makes Claude a true workplace collaborator.
  Decodes shorthand, acronyms, nicknames, and internal language so Claude
  understands requests like a colleague would. CLAUDE.md for working memory,
  memory/ directory for the full knowledge base. Do NOT use for tasks outside
  the productivity domain.
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Memory Management

Memory makes Claude your workplace collaborator - someone who speaks your internal language.

## The Goal

Transform shorthand into understanding:

```
User: "ask todd to do the PSR for oracle"
              ↓ Claude decodes
"Ask Todd Martinez (Finance lead) to prepare the Pipeline Status Report
 for the Oracle Systems deal ($2.3M, closing Q2)"
```

Without memory, that request is meaningless. With memory, Claude knows:
- **todd** → Todd Martinez, Finance lead, prefers Slack
- **PSR** → Pipeline Status Report (weekly sales doc)
- **oracle** → Oracle Systems deal, not the company

## Architecture

```
CLAUDE.md          ← Hot cache (~30 people, common terms)
memory/
  glossary.md      ← Full decoder ring (everything)
  people/          ← Complete profiles
  projects/        ← Project details
  context/         ← Company, teams, tools
```

**CLAUDE.md (Hot Cache):**
- Top ~30 people you interact with most
- ~30 most common acronyms/terms
- Active projects (5-15)
- Your preferences
- **Goal: Cover 90% of daily decoding needs**

**memory/glossary.md (Full Glossary):**
- Complete decoder ring - everyone, every term
- Searched when something isn't in CLAUDE.md
- Can grow indefinitely

**memory/people/, projects/, context/:**
- Rich detail when needed for execution
- Full profiles, history, context

## Lookup Flow

```
User: "ask todd about the PSR for phoenix"

1. Check CLAUDE.md (hot cache)
   → Todd? ✓ Todd Martinez, Finance
   → PSR? ✓ Pipeline Status Report
   → Phoenix? ✓ DB migrati
