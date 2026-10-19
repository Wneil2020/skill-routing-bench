---
name: "padz-datastore-persistence"
description: "Use when the task involves design database: covers padz, datastore, persistence, store, membackend"
---

# padz-datastore-persistence

Explains the padz hybrid store architectureâfiles are truth, JSON metadata is a rebuildable cache. Covers self-healing reconciliation (orphans, zombies, staleness), the Backend+Store split for testability, and how to use MemBackend for unit tests. Use when working on storage, persistence, sync, do
