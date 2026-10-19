---
name: kwp-bio-research-nextflow-development
description: "Use when Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local: covers kwp, bio, research, 리서치, 파이프라인"
metadata:
  holon-triggers: |
    analyzing RNA-seq
    ATAC-seq data—either local FASTQs
---

---
name: kwp-bio-research-nextflow-development
description: >-
  Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing
  data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local
  FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ
  analysis, variant calling, gene expression, differential expression, GEO
  reanalysis, GSE/GSM/SRR accessions, or samplesheet creation. Do NOT use for
  tasks outside the bio domain. Korean triggers: "리서치", "파이프라인", "데이터".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# nf-core Pipeline Deployment

Run nf-core bioinformatics pipelines on local or public sequencing data.

**Target users:** Bench scientists and researchers without specialized bioinformatics training who need to run large-scale omics analyses—differential expression, variant calling, or chromatin accessibility analysis.

## Workflow Checklist

```
- [ ] Step 0: Acquire data (if from GEO/SRA)
- [ ] Step 1: Environment check (MUST pass)
- [ ] Step 2: Select pipeline (confirm with user)
- [ ] Step 3: Run test profile (MUST pass)
- [ ] Step 4: Create samplesheet
- [ ] Step 5: Configure & run (confirm genome with user)
- [ ] Step 6: Verify outputs
```

---

## Step 0: Acquire Data (GEO/SRA Only)

**Skip this step if user has local FASTQ files.**

For public datasets, fetch from GEO/SRA first. See [references/geo-sra-acquisition.md](references/geo-sra-acquisition.md) for the full workflow.

**Quick start:**

```bash
# 1. Get study info
python scripts/sra_geo_fetch.py info GSE110004

# 2. Download (interactive mode)
python scripts/sra_geo_fetch.py download GSE110004 -o ./fastq -i

# 3. Generate samplesheet
python scripts/sra_geo_fetch.py samplesheet GSE110004 --fastq-dir ./fastq -o samplesheet.csv
```

**DECISION POINT:** After fetching study info, confirm with user:
- Which sample subset to download (if multiple data types)
- Suggested genome and pipeline

Then continue to Step 1.
