---
name: kwp-bio-research-single-cell-rna-qc
description: "Use when Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive: covers kwp, bio, research, 리서치, 스캔"
metadata:
  holon-triggers: |
    users request QC analysis
    filtering low-quality cells
---

---
name: kwp-bio-research-single-cell-rna-qc
description: >-
  Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files)
  using scverse best practices with MAD-based filtering and comprehensive
  visualizations. Use when users request QC analysis, filtering low-quality
  cells, assessing data quality, or following scverse/scanpy best practices for
  single-cell analysis. Do NOT use for tasks outside the bio domain. Korean
  triggers: "리서치", "스캔", "데이터".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Single-Cell RNA-seq Quality Control

Automated QC workflow for single-cell RNA-seq data following scverse best practices.

## When to Use This Skill

Use when users:
- Request quality control or QC on single-cell RNA-seq data
- Want to filter low-quality cells or assess data quality
- Need QC visualizations or metrics
- Ask to follow scverse/scanpy best practices
- Request MAD-based filtering or outlier detection

**Supported input formats:**
- `.h5ad` files (AnnData format from scanpy/Python workflows)
- `.h5` files (10X Genomics Cell Ranger output)

**Default recommendation**: Use Approach 1 (complete pipeline) unless the user has specific custom requirements or explicitly requests non-standard filtering logic.

## Approach 1: Complete QC Pipeline (Recommended for Standard Workflows)

For standard QC following scverse best practices, use the convenience script `scripts/qc_analysis.py`:

```bash
python3 scripts/qc_analysis.py input.h5ad
# or for 10X Genomics .h5 files:
python3 scripts/qc_analysis.py raw_feature_bc_matrix.h5
```

The script automatically detects the file format and loads it appropriately.

**When to use this approach:**
- Standard QC workflow with adjustable thresholds (all cells filtered the same way)
- Batch processing multiple datasets
- Quick exploratory analysis
- User wants the "just works" solution

**Requirements:** anndata, scanpy, scipy, matplotlib, seaborn, numpy

**Parameters:**

Customiz
