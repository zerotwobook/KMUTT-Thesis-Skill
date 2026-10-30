# Copy-and-paste instructions for Codex / an AI document agent

## Example 1 — full Thai postgraduate thesis formatting

```text
Read ./KMUTT-Thesis-Skill/SKILL.md and all 5 reference Markdown files.
Treat references/KMUTT_Thesis_Manual_2556.pdf as the source of truth.
Convert my provided thesis content into a Thai postgraduate thesis DOCX and PDF
following the supplied 2556 manual. Set A4, margins left 40/right 20/top 30/
bottom 20 mm; AngsanaUPC Thai body 16 pt and chapter/section/subsection
22/20/18 pt bold; apply front matter and proper Thai/Arabic page numbering.
Use a single consistent citation system chosen from the manual. Generate
real headings, TOC and lists of figures/tables. Do not fabricate academic data.
Run included audits, render final document, inspect all sections for typography
and pagination, and output a deviation report with manual page citations.
If a current-rule check is necessary, explicitly tell me that 2556 is old.
```

## Example 2 — normal KMUTT course report (layout only)

```text
Use ./KMUTT-Thesis-Skill/SKILL.md as a formatting profile for a course report,
NOT as a mandatory thesis package. Apply exact A4 margin/font/heading conventions
from the 2556 manual. Do not add thesis approval, research biography, hardcover,
old intellectual property forms or CD-ROM requirements. Preserve all original
report sections, quotes and references. Make DOCX+PDF, run checks and report
what is inferred vs explicitly in the source.
```

## Example 3 — review an existing file and fix it

```text
Open my existing DOCX, compare to ./KMUTT-Thesis-Skill/SKILL.md and source PDF.
List every mismatch with its original manual printed page, then fix directly
without changing the meaning of any academic content. Maintain citations.
Inspect the exported PDF pages. Return both corrected files and a QA log.
```

## Example 4 — audit only

```bash
python KMUTT-Thesis-Skill/scripts/audit_docx.py thesis.docx --language th --json-out audit_docx.json
python KMUTT-Thesis-Skill/scripts/audit_pdf.py thesis.pdf --json-out audit_pdf.json
```

The scripts are **advisory** and never eliminate the need for rendered-page inspection.
