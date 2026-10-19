---
name: "admin-wsl"
description: "Use when the task involves configure infrastructure: covers admin, wsl, side., profile, admin-windows"
---

# admin-wsl

WSL2 Ubuntu administration from Linux side. Profile-aware - reads preferences from
Windows-side profile at /mnt/c/Users/{WIN_USER}/.admin/profiles/{hostname}.json

Use when: Inside WSL for apt packages, Docker, Python/uv, shell configs, systemd.
Coordinates with admin-windows via shared profile ON T
