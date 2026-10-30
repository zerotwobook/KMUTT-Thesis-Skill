---
name: kmutt-thesis-2556-format
metadata:
  version: "1.0.0"
  language: "th-TH"
  source_year_buddhist: 2556
  scope: "KMUTT postgraduate thesis formatting based on supplied 2556 manual"
description: >
  Create, revise, and verify KMUTT postgraduate thesis documents using the
  user-supplied 'คู่มือการเขียนและพิมพ์วิทยานิพนธ์ ระดับบัณฑิตศึกษา มจธ. พ.ศ. 2556'.
  Use for Thai/English thesis layouts, front matter, headings, pagination,
  figures, tables, citations, bibliography, and DOCX/PDF layout audits.
  Do not claim this manual governs all KMUTT reports or is the latest policy.
---

# KMUTT postgraduate thesis / document formatting — 2556 source-specific skill

> **Source of truth:** `references/KMUTT_Thesis_Manual_2556.pdf` (56 PDF pages, scanned). All *printed page* citations in this skill refer to the number printed in the upper-right corner; for most manual content **PDF page = printed page + 2**. For the cover and unnumbered pages, use the PDF page number. Consult `references/source_page_map.md` whenever a point is ambiguous.
>
> **Scope and freshness:** The supplied text is a **postgraduate thesis manual dated พ.ศ. 2556**, not automatically a general-purpose university report template or the latest 2569 rules. When the task is a course report, apply its *formatting conventions* only if instructed and do **not** require thesis approval sheets, graduate copyright forms, or degree text. Prioritize a more recent faculty/program/course instruction when the user supplies one, and explicitly report conflicts.

## When to activate
- User requests a KMUTT/Mจธ. thesis in Thai/English **with this manual as the standard**.
- User asks to convert an existing report/thesis to this specified formatting.
- User asks for a KMUTT document template, a format audit, front matter, tables/figures, page numbering, or references **based on the provided manual**.
- For a generic KMUTT report, determine whether the user wants **thesis-exact structure** or **page/font/heading style only**; if not specified, use the latter without inventing thesis-specific front matter.

## Files you MUST read before authoring
1. `references/format_rules.md` — exact physical and typography parameters.
2. `references/structure_pagination.md` — front matter, chapters, and numbering.
3. `references/citations_references.md` — choose ONE of the manual's two citation systems.
4. `references/source_page_map.md` — check source/example and confidence status.
5. `references/final_qa.md` — submission gate.

## Priority and truthfulness
1. User's explicit deliverable constraints, **except** that you must disclose conflicts with the manual.
2. More recent and applicable official/faculty/course instructions **actually provided and verified**.
3. Explicit written requirements of this 2556 manual (label **RULE** in references).
4. Manual's layout figures and specimens (label **EXAMPLE**, and do not infer unwritten rules).
5. Implementation choices needed for software support (label **IMPLEMENTATION**; never present them as KMUTT mandates).

If a property is missing (e.g. mandatory line spacing for *every* paragraph, caption numeric style, table font, equations, current policy, binding specifications), do NOT fabricate it. Use a defensible default, document it under "Assumptions / needs faculty confirmation", and ask only if task cannot proceed. Do not transcribe fictional people, signatures, dates, title, degree, faculty, or logo from manual examples as the user's real details.

## Hard requirements: core profile
| Item | Value | Original evidence |
|---|---|---|
| Paper | A4, 210 × 297 mm, plain white unlined; printing on one side | Printed p. 11; PDF p. 13 |
| Paper weight for print | 80 g/m²; final clean copy must be at least 80 g/m² | Printed pp. 5, 11; PDF pp. 7, 13 |
| Margins | **Left 40 mm; right 20 mm; top 30 mm; bottom 20 mm** | Printed pp. 40–41; PDF pp. 42–43 |
| Thai or Thai+English thesis body | **AngsanaUPC, 16 pt throughout the text** | Printed p. 11; sample p. 40 |
| Thai chapter / major heading / subsection | **22 / 20 / 18 pt, bold**, respectively, as shown in specimen | Printed p. 40; PDF p. 42 |
| English body | **Times New Roman, 12 pt** | Printed p. 11; sample p. 41 |
| English chapter / major heading / subsection | **15 / 14 / 13 pt, bold**, respectively, as shown in specimen | Printed p. 41; PDF p. 43 |
| Typeface consistency | Use one font family consistently within the thesis text for the selected language treatment | Printed p. 11 |
| Figures | Generally **not larger than 130 × 180 mm**; cite source if applicable | Printed p. 12; PDF p. 14 |
| Units | SI units; if another unit is necessary, explain in parentheses | Printed p. 5; PDF p. 7 |
| In-text citation systems | Either **numbered** or **author–year**, with one consistent system | Printed p. 14; PDF p. 16 |
| Prelim / main pagination | Thai front matter: ก, ข, ค…; English: i, ii, iii…; main: Arabic 1, 2, 3… upper-right | Printed p. 12; PDF p. 14 |
| Chapter opening page | **Do not print the page number on the first page of each chapter**; numbering in subsequent pages continues | Printed p. 12; PDF p. 14 |

**Important:** Printed p. 11 states broader heading ranges: Thai 18–22 pt and English 13–15 pt; printed pp. 40–41 show the precise 22/20/18 and 15/14/13 hierarchy. Use the precise **sample hierarchy** for implementation, noting that the hierarchy is evidenced by an example rather than a universal sub-level scheme for all possible depths.

## Required workflow (execute in order)

### 1. Classify the target
Record `document_type: thesis|course_report|research_report`, `language: th|en|mixed`, `deliverables: docx|pdf|both`, `citation_system: numeric|author_year`, and whether there are newer overrides. A thesis gets the thesis-specific front matter; a class report normally does not unless asked.

### 2. Build an evidence-backed outline
Use `references/structure_pagination.md`. Derive actual chapter titles from supplied user content; do not invent thesis results or references. Use Heading styles, real TOC/caption fields when available, not manually typed dots or page numbers. Use Word section breaks to manage prelims, main text and chapter first-page page-number suppression.

### 3. Set page geometry and styles first
- Explicitly set A4 (not Letter), portrait unless landscape is necessary for a specific wide display.
- Set **40/20/30/20 mm** margins in the order left/right/top/bottom, **on every applicable section**. The usable body box is **150 × 247 mm**.
- For a **Thai-language thesis or a thesis containing both Thai and English**, use **AngsanaUPC 16 pt for the text** as the manual explicitly states. For an **English-language thesis**, use **Times New Roman 12 pt**. Do **not** automatically switch English runs to Times New Roman inside a Thai/bilingual thesis; that would contradict printed p. 11.
- Set Heading 1/2/3 language-specific sizes according to the specimen; don't assume English sample's "CHAPTER 2" and "3.1" refer to the *same* chapter — examples can have placeholders.
- Keep fonts standard at install level; **never bundle font files**. If missing locally, tell the user that visual fidelity cannot be guaranteed until rendered where the fonts exist.
- Main text should not be split by manual hard line breaks to simulate wrapping. Use single-line (1.0) as a software interpretation of normal “one printing line” spacing; for large headings use double spacing or appropriate visual clearance. The manual does not define an exact universal paragraph-before/after value in points. Avoid splitting a word at line end; use heading keep-with-next and widow/orphan checks.

### 4. Insert the correct pagination
- Unnumbered title/approval pages; prelim pages use language-specific letters/Roman; main content uses Arabic starting at 1, upper right.
- The first page of **each chapter** has no visibly printed number, while its page still counts.
- Use different-first-page headers or section-specific header logic as needed; do not suppress all page numbers by accident.
- Keep TOC page references consistent with actually rendered pagination. Never claim automatic TOC refresh without verifying it.

### 5. Render figures, tables, and source attributions
- Use numbered **รูปที่ ...** (figure) and **ตารางที่ ...** (table) labels, with explanatory captions. Table captions above table and figure captions below figure follow the demonstrated page (printed p. 42), but treat exact caption location as an **EXAMPLE** unless a stricter rule was supplied.
- Keep figure dimensions within 130 × 180 mm where practical; if exceeded for readability, flag the exception explicitly.
- Attribute reused figures/tables; for photographed experimental results, use real photograph/scan as described in manual rather than a fake recreated measurement image.
- Include all figures/tables in the corresponding lists, including appendix figures/tables.

### 6. Cite, build references, and cross-check
- Choose exactly one source-based system from `references/citations_references.md`.
- Never invent bibliographic metadata, author names, volume, page, DOI, URL, or access dates.
- Make every in-text citation match a complete reference; ensure every listed source is referenced if the work is an actual thesis/research document.
- Do not assume APA or IEEE rules override this manual unless user/faculty explicitly directs it.

### 7. Validate programmatically AND visually
- DOCX: `python scripts/audit_docx.py path/to/file.docx --language th` (or `en`).
- PDF: `python scripts/audit_pdf.py path/to/file.pdf`.
- **Mandatory manual visual pass** on cover, approval, first prelim, contents, first page of every chapter, representative body, table/figure page, references, appendix, last page.
- Check in exported PDF: glyph substitution, clipped Thai diacritics, margin violations, blank pages, header and page-number logic, TOC accuracy, citation links and screenshots/figures.
- Fix errors, re-export, and repeat. Automated audits are advisory checks, not a declaration of compliance.

### 8. Deliver with a transparent validation report
Supply actual document files and a brief QA result mentioning file format, applied manual/year, passes, warnings, and any unsatisfied or unverified constraints. **Never say "100% ตามระเบียบ" without full checks.**

## Template / starter notes
`examples/KMUTT_styles_starter.docx` defines page geometry and Thai/English paragraph styles, **not** a submission-ready thesis. It intentionally does not invent cover information, approval text, section breaks, TOC, citations, or chapter page numbers. Use it as a technical base only.

## Quick Codex invocation
```
Use the skill at KMUTT-Thesis-Skill/SKILL.md and its references.
Apply the supplied KMUTT postgraduate-thesis manual (2556) to my attached content.
Output a .docx and export a PDF. Use the correct Thai/English style,
section and chapter pagination, list of tables and figures, and one consistent
citation system. Render all pages, audit with both included scripts, and report
any deviations with source manual pages. Do not fabricate missing data.
```

## Minimal audit checklist
- [ ] Correct scope (thesis vs normal report) and source manual year disclosed.
- [ ] A4, single side, white 80 g/m² print instruction.
- [ ] Margins 40/20/30/20 mm every relevant section.
- [ ] Thai or bilingual AngsanaUPC 16 (headings 22/20/18) OR English-language thesis TNR 12 (15/14/13).
- [ ] Correct genuine sections, real front matter (where applicable), page numbering and chapter-opening suppression.
- [ ] Accurate TOC, list of tables/figures, figure sizes/captions, SI units.
- [ ] One citation system, no fabricated bibliographic details.
- [ ] DOCX/PDF audited, PDF visually checked, discrepancies disclosed.

See `references/final_qa.md` for the full acceptance test.
