---
name: daiso-mcp
description: "Use when Search stores, check product inventory, and look up movie seats across Daiso, Olive Young, and Megabox via the daiso-mcp MCP server. Use when: covers daiso, mcp, commerce, inventory, megabox"
metadata:
  holon-triggers: |
    find a Daiso store
    check Olive Young inventory
---

---
name: daiso-mcp
description: >-
  Search stores, check product inventory, and look up movie seats across Daiso,
  Olive Young, and Megabox via the daiso-mcp MCP server. Use when the user asks
  to "find a Daiso store", "check Olive Young inventory", "search Daiso
  products", "Megabox movie seats", "근처 다이소", "올리브영 재고", "메가박스 영화", or any
  Korean retail store/inventory/movie lookup. Do NOT use for non-Korean retail
  services, general web scraping, or e-commerce purchasing.
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Daiso MCP: Korean Retail & Movie Lookup

Search products, find nearby stores, check real-time inventory (Daiso, Olive Young), and browse movie showtimes with seat availability (Megabox) -- all via a single remote MCP server.

## Prerequisites

The `daiso-mcp` MCP server must be registered. Add to your MCP config (`.cursor/mcp.json` or Cursor Settings > MCP):

```json
{
  "mcpServers": {
    "daiso-mcp": {
      "url": "https://mcp.aka.page",
      "transport": "sse"
    }
  }
}
```

No API keys are required for the public server. All tools are available immediately after connection.

## Available Tools

### Daiso (다이소) -- 4 tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `daiso_search_products` | Search Daiso products by keyword | `query` (required), `page`, `pageSize` |
| `daiso_find_stores` | Find Daiso stores by location or keyword | `keyword` or `sido` (one required), `gugun`, `dong`, `limit` |
| `daiso_check_inventory` | Check store-level stock for a product | `productId` (required), `storeQuery`, `latitude`, `longitude` |
| `daiso_get_price_info` | Get product price details | `productId` or `productName` (one required) |

### Olive Young (올리브영) -- 2 tools

| Tool | Description | Key Parameters |
|------|-------------|----------------|
| `oliveyoung_find_nearby_stores` | Find nearby Olive Young stores | `latitude`, `longitude`, `keyword`, `limit` |
| `oliveyoung_check_inve
