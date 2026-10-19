---
name: "artifacts"
description: "Use when the task involves implement documentation: covers artifacts, chromadb, answer, chroma_db, confirm-before-execute"
---

# artifacts

Create and manage repo-local work artifacts for a user âtask requestâ by generating `.artifacts/artifacts/{request_id}/` with `plan.md`, `todo.md`, and `walkthrough.md`, then indexing completed work into ChromaDB stored at `.artifacts/chroma_db/` for 7-day recall. Use when the user wants (1) a t
