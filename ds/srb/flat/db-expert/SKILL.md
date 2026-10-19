---
name: db-expert
description: "Use when Review PostgreSQL schemas, Alembic migrations, query plans, indexing strategies, and Redis caching patterns. Use when the user asks about database: covers expert, 리뷰, 설계, alembic, caching"
metadata:
  holon-triggers: |
    migration safety
    query optimization
---

---
name: db-expert
description: >-
  Review PostgreSQL schemas, Alembic migrations, query plans, indexing
  strategies, and Redis caching patterns. Use when the user asks about database
  design, migration safety, query optimization, schema review, or connection
  pooling. Do NOT use for backend API design or service architecture (use
  backend-expert) or full-stack performance profiling (use
  performance-profiler). Korean triggers: "리뷰", "설계", "계획", "성능".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# DB Expert

Specialist for PostgreSQL 16, PgBouncer, Redis 7, and Qdrant. Migrations managed by Alembic at `db/migrations/`. Init scripts at `db/init.sql`.

## Schema Review

### Checklist

- [ ] Tables have explicit primary keys (prefer `BIGINT GENERATED ALWAYS AS IDENTITY` or UUID)
- [ ] Foreign keys have `ON DELETE` behavior defined (CASCADE / SET NULL / RESTRICT)
- [ ] `NOT NULL` constraints on columns that should never be empty
- [ ] `CHECK` constraints for domain rules (e.g., `status IN ('active','inactive')`)
- [ ] `created_at` / `updated_at` timestamps with `DEFAULT now()` and trigger for update
- [ ] Multi-tenant isolation via `tenant_id` column where applicable
- [ ] Naming convention: `snake_case` tables, singular nouns, `fk_<table>_<ref>` for foreign keys
- [ ] No reserved-word column names (`user`, `order`, `group`)

### Index Strategy

- [ ] Primary key auto-indexed (no duplicate index)
- [ ] Foreign keys have indexes (PostgreSQL does NOT auto-index FK columns)
- [ ] Composite indexes match query patterns (leftmost-prefix rule)
- [ ] Partial indexes for filtered queries (`WHERE deleted_at IS NULL`)
- [ ] GIN/GiST indexes for JSONB or full-text search columns
- [ ] No unused indexes (check `pg_stat_user_indexes.idx_scan = 0`)

## Alembic Migration Safety

### Pre-merge Checklist

- [ ] Migration is reversible (`downgrade()` implemented and tested)
- [ ] No `ALTER TABLE ... ADD COLUMN ... NOT NULL` without `DEFAULT` (locks table
