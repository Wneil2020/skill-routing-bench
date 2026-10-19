---
name: public-apis
description: "Use when Search and discover 1,400+ free public APIs across 50+ categories (weather, finance, AI/ML, games, government data, cryptocurrency: covers public, apis, cryptocurrency, games, government"
metadata:
  holon-triggers: |
    find an API
    search for free APIs
---

---
name: public-apis
description: >-
  Search and discover 1,400+ free public APIs across 50+ categories (weather,
  finance, AI/ML, games, government data, cryptocurrency, etc.) via the
  public-apis MCP server. Use when the user asks to "find an API", "search for
  free APIs", "list weather APIs", "public API for X", "free API", "API 추천", "무료
  API", "API 검색", or any API discovery/lookup task. Do NOT use for calling the
  discovered APIs directly, building MCP servers, or non-API-related searches.
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Public APIs: Free API Discovery & Recommendation

Search, filter, and discover 1,400+ free public APIs across 50+ categories. Get project-based recommendations, generate integration code, and find alternatives -- all via a single MCP server.

## Prerequisites

The `public-apis` MCP server must be registered. Add to your MCP config (`~/.cursor/mcp.json` or Cursor Settings > MCP):

```json
{
  "mcpServers": {
    "public-apis": {
      "command": "npx",
      "args": ["-y", "@weilei_kyle/public-apis-mcp"],
      "env": {}
    }
  }
}
```

No API keys required. The server syncs data from the [public-apis/public-apis](https://github.com/public-apis/public-apis) GitHub repository on first use.

## Available Tools

### Search & Discovery -- 5 tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `search_apis_by_category` | Search APIs within a specific category | `category` (required), `limit` (default: 10) |
| `search_apis_by_keyword` | Full-text keyword search across all APIs | `keyword` (required), `limit` (default: 10) |
| `get_api_details` | Get detailed info for a specific API by name | `apiName` (required) |
| `get_category_list` | List all available API categories | -- |
| `get_random_api` | Get a random API, optionally within a category | `category` (optional) |

### Filtering -- 3 tools

| Tool | Description | Key Parameters |
|------|-------------|-------
