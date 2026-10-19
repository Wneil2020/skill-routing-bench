---
name: "scaffold-experiment"
description: "Use when the task involves orchestrate pipeline: covers scaffold, experiment, configs, scaffold-inspect, scaffold-torchtune"
---

# scaffold-experiment

Set up complete experimental infrastructure for all runs in a designed experiment. Orchestrates parallel generation of fine-tuning configs (via scaffold-torchtune) and evaluation configs (via scaffold-inspect). Use after design-experiment to prepare configs before running experiments.
