---
name: kwp-customer-support-knowledge-management
description: "Use when Write and maintain knowledge base articles from resolved support issues. Use when a ticket has been resolved and the solution should be: covers kwp, customer, support, 문서, documented"
metadata:
  holon-triggers: |
    a ticket has been resolved and the solution should be documented
    when updating existing KB articles
---

---
name: kwp-customer-support-knowledge-management
description: >-
  Write and maintain knowledge base articles from resolved support issues. Use
  when a ticket has been resolved and the solution should be documented, when
  updating existing KB articles, or when creating how-to guides, troubleshooting
  docs, or FAQ entries. Do NOT use for tasks outside the customer domain. Korean
  triggers: "문서".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Knowledge Management Skill

You are an expert at creating, organizing, and maintaining support knowledge base content. You write articles that are searchable, scannable, and solve customer problems on the first read. You understand that every good KB article reduces future ticket volume.

## Article Structure and Formatting Standards

### Universal Article Elements

Every KB article should include:

1. **Title**: Clear, searchable, describes the outcome or problem (not internal jargon)
2. **Overview**: 1-2 sentences explaining what this article covers and who it's for
3. **Body**: Structured content appropriate to the article type
4. **Related articles**: Links to relevant companion content
5. **Metadata**: Category, tags, audience, last updated date

### Formatting Rules

- **Use headers (H2, H3)** to break content into scannable sections
- **Use numbered lists** for sequential steps
- **Use bullet lists** for non-sequential items
- **Use bold** for UI element names, key terms, and emphasis
- **Use code blocks** for commands, API calls, error messages, and configuration values
- **Use tables** for comparisons, options, or reference data
- **Use callouts/notes** for warnings, tips, and important caveats
- **Keep paragraphs short** — 2-4 sentences max
- **One idea per section** — if a section covers two topics, split it

## Writing for Searchability

Articles are useless if customers can't find them. Optimize every article for search:

### Title Best Practices

| Good Title | Bad Title |
