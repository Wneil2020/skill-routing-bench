---
name: "prisma-connection-pool-exhaustion"
description: "Use when the task involves debug database: covers prisma, connection, pool, exhaustion, many"
---

# prisma-connection-pool-exhaustion

Fix Prisma "Too many connections" and connection pool exhaustion errors in 
serverless environments (Vercel, AWS Lambda, Netlify). Use when: (1) Error 
"P2024: Timed out fetching a new connection from the pool", (2) PostgreSQL 
"too many connections for role", (3) Database works locally but fails in
