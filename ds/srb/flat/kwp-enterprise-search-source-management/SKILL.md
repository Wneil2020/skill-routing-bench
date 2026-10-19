---
name: kwp-enterprise-search-source-management
description: "Use when Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority: covers kwp, enterprise, search, 검색, awareness"
---

---
name: kwp-enterprise-search-source-management
description: >-
  Manages connected MCP sources for enterprise search. Detects available
  sources, guides users to connect new ones, handles source priority ordering,
  and manages rate limiting awareness. Do NOT use for tasks outside the
  enterprise-search domain. Korean triggers: "검색".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Source Management


Knows what sources are available, helps connect new ones, and manages how sources are queried.

## Checking Available Sources

Determine which MCP sources are connected by checking available tools. Each source corresponds to a set of MCP tools:

| Source | Key capabilities |
|--------|-----------------|
| **Slack** | Search messages, read channels and threads |
| **Gmail** | Search messages, read individual emails |
| **Google Drive** | Search files, fetch document contents |
| **Linear** | Search tasks, typeahead search |
| **HubSpot** | Query records (accounts, contacts, opportunities) |
| **Notion** | Semantic search, keyword search |

If a tool prefix is available, the source is connected and searchable.

## Guiding Users to Connect Sources

When a user searches but has few or no sources connected:

```
You currently have [N] source(s) connected: [list].

To expand your search, you can connect additional sources in your MCP settings:
- Slack — messages, threads, channels
- Gmail — emails, conversations, attachments
- Google Drive — docs, sheets, slides
- Linear — tasks, projects, milestones
- HubSpot — accounts, contacts, opportunities
- Notion — wiki pages, knowledge base articles

The more sources you connect, the more complete your search results.
```

When a user asks about a specific tool that is not connected:

```
[Tool name] isn't currently connected. To add it:
1. Open your MCP settings
2. Add the [tool] MCP server configuration
3. Authenticate when prompted

Once connected, it will be automatically included in futur
