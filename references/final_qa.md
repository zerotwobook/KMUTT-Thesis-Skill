# Final quality gate for 2556 KMUTT thesis formatting

## Pass / needs review / fail
Report each item as **PASS**, **REVIEW**, **FAIL**, or **N/A**. Automated scripts give diagnostic warnings, NOT full compliance.

### Document scope and authenticity
- [ ] Manual identified correctly as **postgraduate thesis 2556**, not alleged current all-program policy.
- [ ] Any class-specific instruction or newer rule handled explicitly with citation/override record.
- [ ] Thesis-specific cover, signatures, degrees and forms used only when appropriate and genuine (no example-name copying).
- [ ] No fabricated findings, citations, institutional logos or committee member details.

### Physical and typographic format
- [ ] A4 210×297 mm on all applicable pages; printable content portrait unless exception documented.
- [ ] Margins: **left 40, right 20, top 30, bottom 20 mm**.
- [ ] Body language fonts correct (AngsanaUPC 16 pt Thai or bilingual thesis; Times New Roman 12 pt English-only thesis).
- [ ] Heading hierarchy as specimen (TH 22/20/18, EN 15/14/13) and consistent bold.
- [ ] Within same language, no font drift from headings, pasted tables, footnotes (unless justified).
- [ ] Printed output instructions white clean paper 80 gsm, one-sided (digital artifact can't verify real paper).
- [ ] Paragraphs and headings visually aligned; no clipped Thai vowel/tone marks or doubled spaces/stranded words.

### Structure and pages
- [ ] Appropriate cover, title, approval where thesis required.
- [ ] Abstract(s) (each at most one page), correct sequence, keywords (3–8) separated with `/`.
- [ ] Acknowledgments one page or less; TOC and lists accurate; symbol/glossary list if applicable.
- [ ] Main content, complete cited references, appendices if needed, researcher biography ≤1 page.
- [ ] No page numbers on cover/approval; prelim Thai consonant or English Roman correctly rendered.
- [ ] Main page numbers Arabic upper-right, continuous; first page of every chapter number invisible but counted.
- [ ] Chapter numbering and subsection hierarchies consistent (no mismatch copying specimen).
- [ ] TOC and lists use **actual** final PDF pages; no stale fields or wrong leader dots.

### Figures, tables, and sources
- [ ] Every figure/table labelled and referenced with correct numbering and caption.
- [ ] Figures generally ≤130 × 180 mm, checked on the final page (not merely original image dimensions).
- [ ] Every reused visual has complete source attribution.
- [ ] Appendices' tables and figures included in the lists.
- [ ] SI units used; other units explained.
- [ ] One consistent reference system, source fields accurate and no orphan references.
- [ ] Direct quotations have correct formatting, attribution and page when applicable.

### Quality checks and evidence
- [ ] Ran `scripts/audit_docx.py` on DOCX (if delivered).
- [ ] Ran `scripts/audit_pdf.py` on PDF (if delivered).
- [ ] Rendered final DOCX to images / PDF, inspected cover, prelims, chapter openings, representative bodies, tables and references.
- [ ] Checked the exported PDF for font embedding/substitution if applicable, text clipping and unexpected page breaks.
- [ ] Output described clearly: deliverables, manual/version used, unresolved warnings/assumptions, link to files.

## Example QA report template
```
Manual: KMUTT Postgraduate Thesis Formatting 2556 (not verified current)
Document type: [thesis/course report]
Language: [TH/EN/mixed]
Citations: [numbered/author-year]
DOCX check: [N pass / N warnings / N errors]
PDF check: [A4 and geometry, font/visual limitations]
Visual sampling: [pages inspected]
Deviations: [item, reason, manual page]
Unverified: [e.g., installed AngsanaUPC, current approval forms, physical paper weight]
Final status: [PASS / REVIEW / FAIL]
```

Do NOT declare a final PDF "submission-ready" if important checks are `REVIEW` or `FAIL`.
