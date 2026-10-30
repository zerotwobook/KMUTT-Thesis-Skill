#!/usr/bin/env python3
"""Advisory PDF review: A4 size, text fonts, visible bounding boxes.

Does not assess manual line breaks/citations/content. For scan PDFs, text may be empty.
Inspect all pages visually; especially page numbers and opening-page suppression.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
import fitz

PT_PER_MM=72/25.4

def check(path):
    doc=fitz.open(path)
    errors,warnings,facts=[],[],[]
    font_freq=Counter()
    for i,p in enumerate(doc,1):
        w,h=p.rect.width/PT_PER_MM,p.rect.height/PT_PER_MM
        if abs(w-210)>0.6 or abs(h-297)>0.6:
            errors.append(f'PDF page {i}: {w:.2f}x{h:.2f} mm != A4 210x297 mm')
        data=p.get_text('dict')
        runs=[]
        for block in data['blocks']:
            if 'lines' in block:
                for line in block['lines']:
                    for span in line['spans']:
                        if span['text'].strip():
                            runs.append(span)
                            font_freq[span['font']] += len(span['text'])
        if i in (1,2,3,len(doc)) or (i%20==0):
            facts.append(f'Page {i}: extracted text spans {len(runs)}; size {w:.1f}×{h:.1f} mm')
        if not runs and len(doc)>1:
            # Scanned, figure-only, cover or truly blank page: review manually rather than fail.
            if i <= 3 or i > len(doc)-2:
                continue
            warnings.append(f'PDF page {i}: no extractable text; scanned or image-only page, manual check required')
        elif i > 3:  # Covers/approval may legitimately use full-page layout
            # Only warn on text extending past physical page, not the body margins:
            # header/page number and special diagrams could be outside the body box.
            for span in runs:
                x0,y0,x1,y1=span['bbox']
                if x0 < -1 or y0 < -1 or x1>p.rect.width+1 or y1>p.rect.height+1:
                    warnings.append(f'PDF page {i}: text touches/outside physical page; manual review')
                    break
    facts.append(f'Total pages: {len(doc)}')
    facts.append(f'Extracted font frequencies by characters: {dict(font_freq.most_common(10))}')
    warnings.append('Automatic PDF check cannot prove exact margin of every paragraph, correct upper-right page numbering, blank chapter-first header, 80 gsm paper, actual embedded fonts, or bibliography accuracy')
    return {'path':str(path),'status':'FAIL' if errors else 'REVIEW','errors':errors,'warnings':warnings,'facts':facts}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pdf')
    ap.add_argument('--json-out')
    a=ap.parse_args()
    res=check(a.pdf)
    print('KMUTT 2556 PDF audit:',res['status'])
    for category in ('errors','warnings','facts'):
        for item in res[category]: print(category.upper()+': '+item)
    if a.json_out: Path(a.json_out).write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf8')
    raise SystemExit(1 if res['errors'] else 0)

if __name__=='__main__': main()
