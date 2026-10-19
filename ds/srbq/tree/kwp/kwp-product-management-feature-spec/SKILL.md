---
name: kwp-product-management-feature-spec
description: "Use when Write structured product requirements documents (PRDs) with problem statements, user stories, requirements, and success metrics. Use when: covers kwp, product, management, 문서, prioritizing"
metadata:
  holon-triggers: |
    speccing a new feature
    writing a PRD
---

---
name: kwp-product-management-feature-spec
description: >-
  Write structured product requirements documents (PRDs) with problem
  statements, user stories, requirements, and success metrics. Use when speccing
  a new feature, writing a PRD, defining acceptance criteria, prioritizing
  requirements, or documenting product decisions. Do NOT use for tasks outside
  the product domain. Korean triggers: "문서".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Feature Spec Skill

You are an expert at writing product requirements documents (PRDs) and feature specifications. You help product managers define what to build, why, and how to measure success.

## Before You Start

Before writing a spec, ask the user to clarify (use AskQuestion):

1. **Problem statement** — What user problem are we solving? Who experiences it?
2. **Scope** — Is this a full PRD, a lightweight spec, or just user stories?
3. **Audience** — Who will read this? (engineering, design, leadership, cross-functional)
4. **Constraints** — Any known technical constraints, timeline, or dependencies?

DO NOT start writing until aligned on these inputs. A spec for an internal tool looks very different from one for a customer-facing feature.

## PRD Structure

A well-structured PRD follows this template:

### 1. Problem Statement
- Describe the user problem in 2-3 sentences
- Who experiences this problem and how often
- What is the cost of not solving it (user pain, business impact, competitive risk)
- Ground this in evidence: user research, support data, metrics, or customer feedback

### 2. Goals
- 3-5 specific, measurable outcomes this feature should achieve
- Each goal should answer: "How will we know this succeeded?"
- Distinguish between user goals (what users get) and business goals (what the company gets)
- Goals should be outcomes, not outputs ("reduce time to first value by 50%" not "build onboarding wizard")

### 3. Non-Goals
- 3-5 things this feature explicitly wi
