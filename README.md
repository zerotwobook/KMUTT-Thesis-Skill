# KMUTT Thesis Formatting AI Skill (manual พ.ศ. 2556)

An agent-readable skill package built from the uploaded **56-page scanned KMUTT postgraduate thesis manual**. Includes evidence-linked rules, structure, citation/reference formats, quality gates, source PDF, and advisory DOCX/PDF auditors.

## Install for Codex

Place the folder in your project's `.agents/skills/kmutt-thesis-2556-format/` (or in a Codex skills directory supported by your installation) **with all contents intact**, then prompt Codex to read `SKILL.md`. Alternatively keep the folder alongside your thesis files and explicitly mention its `SKILL.md` path.

Use `examples/use_with_codex.md` for ready-to-copy prompts.

## Package

- `SKILL.md` — skill definition, primary workflow, core rules.
- `AGENTS.md` — simple instructions for other coding agents.
- `references/*.md` — detailed evidence-linked requirements.
- `references/KMUTT_Thesis_Manual_2556.pdf` — original source.
- `examples/KMUTT_styles_starter.docx` — basic page geometry/styles **not submission-ready**.
- `scripts/audit_docx.py` — DOCX geometry and layout sanity checks.
- `scripts/audit_pdf.py` — PDF page-size and text sanity checks.

## Important limits

The manual is dated **2556 (2013)** and relates to **postgraduate theses**. The tool does not certify current KMUTT academic policy, real 80-gsm paper, originality, exact page-number schemes or full compliance solely by running scripts. `AngsanaUPC` must exist in the output computer for identical rendering; **no font binaries are included**. Word styles starter is technical scaffolding, not a completed thesis. The manual is originally a scan; visually consult source pages where details conflict.

## Requirements for scripts

```bash
pip install python-docx pymupdf
python scripts/audit_docx.py YOUR_DOCUMENT.docx --language th
python scripts/audit_pdf.py YOUR_DOCUMENT.pdf
```
