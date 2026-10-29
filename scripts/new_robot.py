#!/usr/bin/env python3
"""Create an unknown-valued record; never overwrite an existing model."""
import argparse
from datetime import date
import re
import yaml
from kb import ROOT, front
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--id',required=True);p.add_argument('--name',required=True)
p.add_argument('--manufacturer',required=True);p.add_argument('--source',required=True)
a=p.parse_args()
if not re.fullmatch('[a-z][a-z0-9_]*',a.id):p.error('ID muss stabil und pfadsicher sein')
if not (ROOT/f'hersteller/{a.manufacturer}/profil.md').is_file():p.error('Hersteller zuerst anlegen')
if not (ROOT/f'quellen/{a.source}.md').is_file():p.error('Quelle zuerst anlegen')
target=ROOT/'roboter'/a.id
if target.exists():p.error('Modell ID existiert bereits')
m,b=front(ROOT/'vorlagen/roboter/profil.md');today=date.today().isoformat()
m.update(id=a.id,name=a.name,manufacturer_id=a.manufacturer)
m['classification']['source_ids']=[a.source];m['classification']['assessed_at']=today
m['maintenance'].update(last_search=today,reviewed_at=today,next_review=today,status='erfasst')
b=b.replace('# Modellname','# '+a.name)
d=yaml.safe_load((ROOT/'vorlagen/roboter/fakten.yaml').read_text());d['robot_id']=a.id
# Use current registry, so new core fields are not missed by an old template.
metrics=yaml.safe_load((ROOT/'schema/merkmale.yaml').read_text())['metrics']
base=d['claims'][0];d['claims']=[{**base,'id':k.replace('.','_'),'key':k,'unit':s['unit']} for k,s in metrics.items() if s['core']]
target.mkdir(parents=True)
(target/'profil.md').write_text('---\n'+yaml.safe_dump(m,allow_unicode=True,sort_keys=False)+'---\n\n'+b+'\n')
(target/'fakten.yaml').write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False))
for folder in ['assets','dokumente']:
 (target/folder).mkdir();(target/folder/'README.md').write_text('# Ablage\n\nNoch keine Originale gespeichert. Herkunft und Rechte vor Aufnahme prüfen.\n')
print(f'Angelegt: {a.id}. Jetzt Einordnung, Quellen, Fakten und offene Fragen prüfen; danach validate und build.')
