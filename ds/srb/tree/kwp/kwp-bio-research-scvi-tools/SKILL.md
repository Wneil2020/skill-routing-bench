---
name: kwp-bio-research-scvi-tools
description: "Use when Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with: covers kwp, bio, research, 리서치, 스캔"
---

---
name: kwp-bio-research-scvi-tools
description: >-
  Deep learning for single-cell analysis using scvi-tools. This skill should be
  used when users need (1) data integration and batch correction with
  scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal
  analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5)
  spatial transcriptomics deconvolution with DestVI, (6) label transfer and
  reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8)
  any deep learning-based single-cell method. Triggers include mentions of scVI,
  scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational
  autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq,
  multiome, reference mapping, latent space. Do NOT use for tasks outside the
  bio domain. Korean triggers: "리서치", "스캔", "스킬", "데이터".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# scvi-tools Deep Learning Skill

This skill provides guidance for deep learning-based single-cell analysis using scvi-tools, the leading framework for probabilistic models in single-cell genomics.

## How to Use This Skill

1. Identify the appropriate workflow from the model/workflow tables below
2. Read the corresponding reference file for detailed steps and code
3. Use scripts in `scripts/` to avoid rewriting common code
4. For installation or GPU issues, consult `references/environment_setup.md`
5. For debugging, consult `references/troubleshooting.md`

## When to Use This Skill

- When scvi-tools, scVI, scANVI, or related models are mentioned
- When deep learning-based batch correction or integration is needed
- When working with multi-modal data (CITE-seq, multiome)
- When reference mapping or label transfer is required
- When analyzing ATAC-seq or spatial transcriptomics data
- When learning latent representations of single-cell data

## Model Selection Guide

| Data Type | Model | Primary Use Case |
|----------
