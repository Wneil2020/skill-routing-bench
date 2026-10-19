---
name: anthropic-xlsx
description: "Use when Work with spreadsheets (.xlsx, .csv, .tsv). Create, read, edit, fix, format, chart, clean data, convert between tabular formats. Do NOT use for: covers anthropic, xlsx, 엑셀, 스프레드시트, tabular"
---

---
name: anthropic-xlsx
description: >-
  Work with spreadsheets (.xlsx, .csv, .tsv). Create, read, edit, fix, format,
  chart, clean data; convert between tabular formats. Do NOT use for Word
  documents (use anthropic-docx), presentations (use anthropic-pptx), or PDFs
  (use anthropic-pdf). Korean triggers: "엑셀", "스프레드시트", "xlsx".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Proprietary. LICENSE.txt has complete terms"
  category: "document"
---
# Requirements for Outputs

## All Excel files

### Professional Font
- Use a consistent, professional font (e.g., Arial, Times New Roman) for all deliverables unless otherwise instructed by the user

### Zero Formula Errors
- Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preserve Existing Templates (when updating templates)
- Study and EXACTLY match existing format, style, and conventions when modifying files
- Never impose standardized formatting on files with established patterns
- Existing template conventions ALWAYS override these guidelines

## Financial models

### Color Coding Standards
Unless otherwise stated by the user or existing template

#### Industry-Standard Color Conventions
- **Blue text (RGB: 0,0,255)**: Hardcoded inputs, and numbers users will change for scenarios
- **Black text (RGB: 0,0,0)**: ALL formulas and calculations
- **Green text (RGB: 0,128,0)**: Links pulling from other worksheets within same workbook
- **Red text (RGB: 255,0,0)**: External links to other files
- **Yellow background (RGB: 255,255,0)**: Key assumptions needing attention or cells that need to be updated

### Number Formatting Standards

#### Required Format Rules
- **Years**: Format as text strings (e.g., "2024" not "2,024")
- **Currency**: Use $#,##0 format; ALWAYS specify units in headers ("Revenue ($mm)")
- **Zeros**: Use number formatting to make all zeros "-", including percentages (e.g., "$#,##0;($#,##0);-")
- **Percentages**: Default to 0.0% f
