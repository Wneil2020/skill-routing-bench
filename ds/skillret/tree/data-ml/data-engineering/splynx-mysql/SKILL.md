---
name: "splynx-mysql"
description: "Use when the task involves analyze database: covers splynx, mysql, splynx_mysql, tariffs, customers"
---

# splynx-mysql

Direct MySQL access to Splynx ISP management database.
Use when querying or modifying Splynx tables: customers, leads (category='lead'), services, tariffs, invoices, payments, tickets, network.
Faster than REST API for bulk operations. Reference: src/migration/loaders/splynx_mysql/
