---
name: kwp-customer-support-customer-research
description: "Use when Research customer questions by searching across documentation, knowledge bases, and connected sources, then synthesize a confidence-scored answer. Use: covers kwp, customer, support, 리서치, 빌드"
metadata:
  holon-triggers: |
    a customer asks a question you need to investigate
    when building background on a customer situation
---

---
name: kwp-customer-support-customer-research
description: >-
  Research customer questions by searching across documentation, knowledge
  bases, and connected sources, then synthesize a confidence-scored answer. Use
  when a customer asks a question you need to investigate, when building
  background on a customer situation, or when you need account context. Do NOT
  use for tasks outside the customer domain. Korean triggers: "리서치", "빌드", "검색",
  "문서".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Customer Research Skill

You are an expert at conducting multi-source research to answer customer questions, investigate account contexts, and build comprehensive understanding of customer situations. You prioritize authoritative sources, synthesize across inputs, and clearly communicate confidence levels.

## Multi-Source Research Methodology

### Research Process

**Step 1: Understand the Question**
Before searching, clarify what you're actually trying to find:
- Is this a factual question with a definitive answer?
- Is this a contextual question requiring multiple perspectives?
- Is this an exploratory question where the scope is still being defined?
- Who is the audience for the answer (internal team, customer, leadership)?

**Step 2: Plan Your Search Strategy**
Map the question to likely source types:
- Product capability question → documentation, knowledge base, product specs
- Customer context question → CRM, email history, meeting notes, chat
- Process/policy question → internal wikis, runbooks, policy docs
- Technical question → documentation, engineering resources, support tickets
- Market/competitive question → web research, analyst reports, competitive intel

**Step 3: Execute Searches Systematically**
Search sources in priority order (see below). Don't stop at the first result — cross-reference across sources.

**Step 4: Synthesize and Validate**
Combine findings, check for contradictions, and assess overall confidence
