#!/usr/bin/env python3
"""Fail if checked-in human views do not match canonical data."""
from kb import ROOT, generate, check_links
paths=lambda: {p.relative_to(ROOT):p.read_bytes() for p in ROOT.rglob('*.md') if p.read_text().startswith('<!-- AUTOMATISCH')}
before=paths();generate();check_links();after=paths()
if before!=after:
 changed=sorted(str(p) for p in set(before)|set(after) if before.get(p)!=after.get(p))
 raise SystemExit('Erzeugte Ansichten veraltet: '+', '.join(changed))
print('Erzeugte Ansichten sind aktuell.')
