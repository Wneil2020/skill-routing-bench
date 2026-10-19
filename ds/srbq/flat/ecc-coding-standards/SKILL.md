---
name: ecc-coding-standards
description: "Use when Universal coding standards and best practices for TypeScript, JavaScript, React, and Node.js — naming conventions, error handling patterns: covers ecc, coding, standards, 코딩 표준, 코드 스타일"
metadata:
  holon-triggers: |
    enforcing consistent style
    reviewing code quality
---

---
name: ecc-coding-standards
description: >-
  Universal coding standards and best practices for TypeScript, JavaScript,
  React, and Node.js — naming conventions, error handling patterns, testing
  strategies, and code organization. Use when enforcing consistent style,
  reviewing code quality, or onboarding new contributors. Do NOT use for
  Python-specific patterns (use backend-expert). Do NOT use for domain-specific
  review (use frontend-expert or backend-expert). Korean triggers: "코딩 표준", "코드 스타일".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# Coding Standards & Best Practices

Universal coding standards applicable across all projects.

## When to Activate

- Starting a new project or module
- Reviewing code for quality and maintainability
- Refactoring existing code to follow conventions
- Enforcing naming, formatting, or structural consistency
- Setting up linting, formatting, or type-checking rules
- Onboarding new contributors to coding conventions

## Code Quality Principles

### 1. Readability First
- Code is read more than written
- Clear variable and function names
- Self-documenting code preferred over comments
- Consistent formatting

### 2. KISS (Keep It Simple, Stupid)
- Simplest solution that works
- Avoid over-engineering
- No premature optimization
- Easy to understand > clever code

### 3. DRY (Don't Repeat Yourself)
- Extract common logic into functions
- Create reusable components
- Share utilities across modules
- Avoid copy-paste programming

### 4. YAGNI (You Aren't Gonna Need It)
- Don't build features before they're needed
- Avoid speculative generality
- Add complexity only when required
- Start simple, refactor when needed

## TypeScript/JavaScript Standards

### Variable and Function Naming

- **Variables**: Descriptive (`marketSearchQuery`, `isUserAuthenticated`) not unclear (`q`, `flag`, `x`)
- **Functions**: Verb-noun (`fetchMarketData`, `calculateSimilarity`) not noun-only (`market`, `s
