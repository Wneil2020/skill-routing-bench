---
name: "vps-checkup"
description: "Use when the task involves analyze infrastructure: covers vps, checkup, read-only, health, fail2ban"
---

# vps-checkup

SSH into an Ubuntu VPS (Docker) for a read-only health/security/update report (UFW + fail2ban) and propose fixes; apply updates/restarts only with explicit confirmation. Use when the user wants a read-only VPS health/security check.
