---
name: paper
description: "Use when the request concerns the paper category of skills: covers paper"
---

Grouping node for the 0 skills of the paper category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **paper-archive** (`paper-archive/`): Use when Central catalog and knowledge hub for all paper-related activities. Manages a searchable JSON index of reviewed, discovered, and scouted: covers paper, archive, central, previously, reviewed
- **paper-auto-classifier** (`paper-auto-classifier/`): Use when Automatically discover, classify, and route academic papers from arXiv RSS feeds and HuggingFace daily papers. Scores relevance to tracked: covers paper, auto, classifier, queues, feeds
- **paper-review** (`paper-review/`): Use when End-to-end academic paper review pipeline that ingests a paper (arXiv URL, PDF, or markdown), produces a structured Korean review: covers paper, review, ingests, threaded, distributes

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
