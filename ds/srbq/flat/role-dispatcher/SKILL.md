---
name: role-dispatcher
description: "Use when Cross-role mission control that dispatches a given topic to all 12 role-perspective analyzer skills in parallel batches, collects results: covers role, dispatcher, 직무별 분석, 종합 분석, batches"
metadata:
  holon-triggers: |
    cross-role analysis
    직무별 분석
---

---
name: role-dispatcher
description: >
  Cross-role mission control that dispatches a given topic to all 12 role-perspective analyzer
  skills in parallel batches, collects results, invokes executive-briefing for CEO synthesis,
  and posts the final report to Slack #효정-할일. Orchestrates role-ceo, role-cto, role-pm,
  role-developer, role-ux-designer, role-security-engineer, role-cso, role-sales, role-hr,
  role-finance, role-data-scientist, role-trading-expert, and executive-briefing.
  Use when the user runs /role-dispatch, asks for "cross-role analysis", "직무별 분석",
  "종합 분석", "multi-perspective analysis", "all roles analyze", "12개 직무 관점",
  or wants comprehensive multi-role analysis of any business topic.
  Do NOT use for single-role analysis (use the specific role-{name} skill),
  general code review (use deep-review), or financial report generation (use today).
  Korean triggers: "직무별 분석", "종합 분석", "크로스롤 분석", "전 직무 관점".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "orchestration"
---

# Cross-Role Topic Analysis Dispatcher

Orchestrates a comprehensive multi-perspective analysis of any business topic by dispatching
to 12 role-specific analyzer skills, filtering by relevance, synthesizing into a CEO executive
briefing, and delivering results to Slack.

## Input Parsing

Extract from user input:
- **Topic** (required): The business topic to analyze
- **Scope constraints** (optional): Additional context or boundaries
- **Role whitelist** (optional): Analyze only specific roles (e.g., "CTO, PM, Security only")
- **Role blacklist** (optional): Skip specific roles (e.g., "skip HR, Finance")

## Orchestration Flow

### Step 1: Preparation

Create output directory:
```bash
mkdir -p outputs/role-analysis/{topic-slug}
```

Generate a topic slug from the topic (lowercase, hyphens, max 50 chars).

### Step 2: Fan-Out — Role Analysis (Parallel Batches)

Dispatch to role skills using Task tool subagents. Max 4 concurrent subagents.

**Batch 1** (parallel):
| # |
