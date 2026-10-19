---
name: kwp-apollo-prospect
description: "Use when Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and: covers kwp, apollo, prospect, 파이프라인, 이메일"
---

---
name: kwp-apollo-prospect
description: >-
  Full ICP-to-leads pipeline. Describe your ideal customer in plain English and
  get a ranked table of enriched decision-maker leads with emails and phone
  numbers. Do NOT use for tasks outside the apollo domain. Korean triggers:
  "파이프라인", "이메일".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Prospect

Go from an ICP description to a ranked, enriched lead list in one shot. The user describes their ideal customer via "$ARGUMENTS".

## Examples

- `/apollo:prospect VP of Engineering at Series B+ SaaS companies in the US, 200-1000 employees`
- `/apollo:prospect heads of marketing at e-commerce companies in Europe`
- `/apollo:prospect CTOs at fintech startups, 50-500 employees, New York`
- `/apollo:prospect procurement managers at manufacturing companies with 1000+ employees`
- `/apollo:prospect SDR leaders at companies using Salesforce and Outreach`

## Step 1 — Parse the ICP

Extract structured filters from the natural language description in "$ARGUMENTS":

**Company filters:**
- Industry/vertical keywords → `q_organization_keyword_tags`
- Employee count ranges → `organization_num_employees_ranges`
- Company locations → `organization_locations`
- Specific domains → `q_organization_domains_list`

**Person filters:**
- Job titles → `person_titles`
- Seniority levels → `person_seniorities`
- Person locations → `person_locations`

If the ICP is vague, ask 1-2 clarifying questions before proceeding. At minimum, you need a title/role and an industry or company size.

## Step 2 — Search for Companies

Use `mcp__claude_ai_Apollo_MCP__apollo_mixed_companies_search` with the company filters:
- `q_organization_keyword_tags` for industry/vertical
- `organization_num_employees_ranges` for size
- `organization_locations` for geography
- Set `per_page` to 25

## Step 3 — Enrich Top Companies

Use `mcp__claude_ai_Apollo_MCP__apollo_organizations_bulk_enrich` with the domains from the top 10 results.
