---
name: mirofish-graph-explorer
description: "Use when Explore and query MiroFish GraphRAG knowledge graphs — browse entities, relationships, entity types, and graph topology built from seed: covers mirofish, graph, explorer, topology, built"
metadata:
  holon-triggers: |
    explore graph
    browse knowledge graph
---

---
name: mirofish-graph-explorer
description: Explore and query MiroFish GraphRAG knowledge graphs — browse entities, relationships, entity types, and graph topology built from seed documents. Use when the user asks to "explore graph", "browse knowledge graph", "show entities", "graph data", "entity relationships", "그래프 탐색", "지식 그래프", "엔티티 관계", "mirofish graph", or any request to inspect the knowledge graph structure before or after simulation. Do NOT use for building graphs (use mirofish). Do NOT use for running simulations (use mirofish or mirofish-financial-sim). Do NOT use for general knowledge graph operations outside MiroFish (use cognee).
---

# MiroFish Graph Explorer

## Overview

Inspect and query the GraphRAG knowledge graphs that MiroFish builds from seed documents. Understand entity relationships, verify graph quality before simulation, and explore post-simulation graph updates.

## Prerequisites

MiroFish backend running at `http://localhost:5001`. At least one knowledge graph must be built.

## API Reference

### Project Management

```bash
# List all projects
curl -s http://localhost:5001/api/graph/project/list | python3 -m json.tool

# Get project details
curl -s http://localhost:5001/api/graph/project/<project_id> | python3 -m json.tool

# Reset project (clears all graphs and simulations)
curl -X POST http://localhost:5001/api/graph/project/<project_id>/reset
```

### Graph Data Exploration

```bash
# Get full graph data (nodes + edges)
curl -s http://localhost:5001/api/graph/data/<graph_id> | python3 -m json.tool

# List entities from graph
curl -s http://localhost:5001/api/simulation/entities/<graph_id> | python3 -m json.tool

# Get specific entity details
curl -s http://localhost:5001/api/simulation/entities/<graph_id>/<entity_uuid> | python3 -m json.tool

# Filter entities by type (person, organization, event, location, concept)
curl -s http://localhost:5001/api/simulation/entities/<graph_id>/by-type/person | python3 -m json.tool
```

### Task
