# Physical layout and typography (source-derived)

## Legend
- **RULE**: explicit prose instruction from the 2556 manual.
- **EXAMPLE**: specimen page, which can guide appearance but may not mandate every incidental detail.
- **IMPLEMENTATION**: reasonable workflow recommendation **not claimed as a university requirement**.
- All references are to the **printed page**; PDF page is printed page + 2 except unnumbered cover material.

## 1. Paper and printing
- **RULE**: White paper, no ruled lines; A4, 210 × 297 mm; paper weight 80 g/m²; one-sided printing. Printed p. 11 (PDF 13).
- **RULE**: Clean final manuscript without correction marks, erasures, smudges, creases, tears; A4 paper at least 80 grams. Printed p. 5 (PDF 7).
- **RULE**: Body printed with laser printer; font selected must be consistent throughout. Printed p. 11 (PDF 13).
- **RULE**: SI units used; if another unit is indispensable, show in parentheses. Printed p. 5 (PDF 7).
- **IMPLEMENTATION**: Keep editable original plus PDF, inspect print preview for one-sided layout. Paper *weight* cannot be verified from a digital DOCX/PDF.

## 2. Margins and text area
- **EXAMPLE with exact dimensions**: Top 30 mm, left 40 mm, right 20 mm, bottom 20 mm. Printed pp. 40–41 (PDF 42–43).
- **IMPLEMENTATION**: Configure page size A4, `left=4.0 cm; right=2.0 cm; top=3.0 cm; bottom=2.0 cm` in *every* section. Content rectangle width = 210−40−20=150 mm; height = 297−30−20=247 mm. Do not move text outside margins. If document is landscape for a large drawing/table, note as exception because manual doesn't give a general landscape rule.
- **Unspecified**: Required header offset, footer offset, precise first-line indentation, absolute paragraph spacing before/after, exact table cell padding. Don't call guesses official KMUTT rules.

## 3. Fonts and headings
### Thai thesis and any thesis containing Thai and English
- **RULE**: If the thesis is in Thai **or contains both Thai and English**, use **AngsanaUPC 16 pt** for its body and **18–22 pt** for bold headings (printed p. 11, PDF 13). This includes English words inside a bilingual thesis, unless a newer governing instruction specifies otherwise.
- **EXAMPLE**: chapter title **22 pt bold**, primary section heading **20 pt bold**, numbered subheading **18 pt bold**, body **16 pt** (printed p. 40, PDF 42).
- **IMPLEMENTATION**: Styles `KMUTT TH Body 16`, `KMUTT TH Chapter 22`, `KMUTT TH Section 20`, `KMUTT TH Subsection 18`.
### English thesis
- **RULE**: Times New Roman, **12 pt** body, **13–15 pt** heading (printed p. 11, PDF 13).
- **EXAMPLE**: chapter title **15 pt bold**, primary section **14 pt bold**, numbered subheading **13 pt bold**, body **12 pt** (printed p. 41, PDF 43).
- **IMPLEMENTATION**: Styles `KMUTT EN Body 12`, `KMUTT EN Chapter 15`, `KMUTT EN Section 14`, `KMUTT EN Subsection 13`.
### Mixed-language text
- **RULE**: The manual groups Thai-only and Thai+English theses together under **AngsanaUPC**. Do not replace Latin-letter runs with Times New Roman inside an otherwise Thai/bilingual thesis solely because the words are English.
- **IMPLEMENTATION**: Set `ascii`, `hAnsi`, `cs`, and `eastAsia` font properties to AngsanaUPC for Thai/bilingual styles; monitor font substitution. No font files are shipped.
- **RULE**: The manual says to leave **one printing line** between normal lines and to use **Double space or suitable spacing** for major headings; avoid leaving a final word alone on the next line. Printed pp. 11–12 (PDF 13–14).
- **IMPLEMENTATION**: Begin with **single-line (1.0)** body spacing as a practical interpretation of “เว้นหนึ่งบรรทัดพิมพ์”; handle heading gaps as double space or to suit the content. The manual does not provide a fixed value in points or millimetres for all paragraph spacing. Do not claim a precise fixed `before/after` value is required.

## 4. Figures, tables, and abbreviations
- **RULE**: Figures/graphs should generally not exceed **130 mm × 180 mm** (manual says 5 × 7 inches) (printed p. 12, PDF 14).
- **RULE**: Figures with other sources must cite original; photos of experimental products should be authentic photos/scans. Use “รูปที่...” plus sequential figure number and a description (printed p. 12, PDF 14).
- **RULE**: Use “ตารางที่...” plus sequential table number and description (printed p. 12, PDF 14).
- **EXAMPLE**: printed p. 42 / PDF 44 displays `ตารางที่ 2.2` **above** table and `รูปที่ 2.4` **below** the figure.
- **RULE**: List of tables and list of figures include items in the body and in appendices; printed pp. 7–8, PDF 9–10. See examples pp. 35–37.
- **RULE**: Symbols list ordered Latin letters, Greek letters, superscripts/subscripts with specific ordering, explained on printed p. 8 (PDF 10); examples printed p. 38 (PDF 40). Technical terms/abbreviations glossary examples printed p. 39 (PDF 41).
- **IMPLEMENTATION**: Use sequential SEQ fields / cross-references where supported, then refresh and verify after PDF export. Never duplicate a caption or lose an appendix entry.

## 5. Capitalization, numbers, and examples
- **RULE**: For English prose thesis, selected style of capitalisation should be consistent; PDF printed p. 12 illustrates spelling of university name and acceptable word division but explicitly forbids a few odd hyphenations.
- **EXAMPLE**: Thai numbered headings `3`, `3.1`, `3.1.1`; English specimen has `CHAPTER 2` followed by `3.1`, showing **specimen placeholder inconsistency**. Number actual sections logically based on their true chapter, not by copying the sample's `3.1` under Chapter 2.
- **IMPLEMENTATION**: use outline numbering linked to heading styles, not typed static numbers.

## Source verification
See `source_page_map.md` and the original PDF. For the first two pages of the PDF there is photography rather than technical rules. If a style requirement isn't explicitly in the source, label it clearly as an implementation decision.
