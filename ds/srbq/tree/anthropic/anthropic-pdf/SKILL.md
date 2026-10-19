---
name: anthropic-pdf
description: "Use when Read, create, edit, manipulate PDF files. Includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs, splitting: covers anthropic, pdf, PDF, PDF 편집, PDF 생성"
metadata:
  holon-triggers: |
    asks to produce one
---

---
name: anthropic-pdf
description: >-
  Read, create, edit, manipulate PDF files. Includes reading or extracting
  text/tables from PDFs, combining or merging multiple PDFs, splitting PDFs,
  rotating pages, adding watermarks, creating new PDFs, filling PDF forms,
  encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make
  them searchable. Use when the user mentions a .pdf file or asks to produce
  one. Do NOT use for Word documents (use anthropic-docx), spreadsheets (use
  anthropic-xlsx), or presentations (use anthropic-pptx). Korean triggers: "PDF", "PDF 편집", "PDF 생성".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Proprietary. LICENSE.txt has complete terms"
  category: "document"
---
# PDF Processing Guide

## Overview

This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see REFERENCE.md. If you need to fill out a PDF form, read FORMS.md and follow its instructions.

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

# Read a PDF
reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Extract text
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Python Libraries

### pypdf - Basic Operations

#### Merge PDFs
```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Split PDF
```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

#### Extract Metadata
```python
reader = PdfReader("document.pdf")
meta = reader.metadata
print(f"Title: {meta.title}")
print(f"
