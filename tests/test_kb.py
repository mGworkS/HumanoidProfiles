import copy
from datetime import date
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import kb

class KnowledgeTests(unittest.TestCase):
 def test_valid_seed(self):
  self.assertEqual(kb.validate(),len(kb.load()[2]))
  self.assertGreater(kb.validate(),5)
 def test_announced_offer_is_not_procurement(self):
  data=kb.load()[2]['agility_digit5'][1]
  self.assertEqual(kb.procurement_offers(data,date(2026,10,29),'EU','unternehmen'),[])
 def test_verified_offer_region_audience_and_expiry(self):
  offer=copy.deepcopy(kb.load()[2]['agility_digit5'][1]['offers'][0])
  offer.update(mode='raas',status='bestaetigt')
  data={'offers':[offer]}
  self.assertEqual(len(kb.procurement_offers(data,date(2026,10,29),'EU','unternehmen')),1)
  self.assertEqual(kb.procurement_offers(data,date(2026,10,29),'US','privat'),[])
  self.assertEqual(kb.procurement_offers(data,date(2026,10,29),'JP','unternehmen'),[])
  self.assertEqual(kb.procurement_offers(data,date(2027,10,29),'EU','unternehmen'),[])
  self.assertEqual(kb.procurement_offers(data,date(2025,10,29),'EU','unternehmen'),[])
 def test_h1_payload_does_not_inherit_h1_2(self):
  data=kb.load()[2]['unitree_h1'][1]
  claims=[c for c in data['claims'] if c['key'] in ['hardware.payload_arm','hardware.payload_two_arms','hardware.payload_walking']]
  self.assertTrue(claims)
  self.assertTrue(all(c['value'] is None and c['status']=='unbekannt' for c in claims))
 def test_historical_model_in_reference_export(self):
  with tempfile.TemporaryDirectory(dir=kb.ROOT.parent) as tmp:
   root=Path(tmp)/'repo';shutil.copytree(kb.ROOT,root,ignore=shutil.ignore_patterns('.git','export','__pycache__'))
   index,chunks=kb.export(root,commit='test',as_of=date(2026,10,30))
   self.assertTrue(all('screening_section' in row and 'official_link' in row for row in index))
   self.assertEqual(next(row for row in index if row['robot_id']=='aist_und_kawada_hrp_5p')['screening_section'],'forschung')
   self.assertEqual(next(row for row in index if row['robot_id']=='unitree_h1')['screening_section'],'aktuell')
   self.assertIn('honda_asimo_2011',[r['robot_id'] for r in index])
   unknown=[c for c in chunks if c['kind']=='claim' and c['claim']['status']=='unbekannt']
   self.assertTrue(all(c['claim']['value'] is None for c in unknown))
 def test_missing_source_and_wrong_unit_rejected(self):
  with tempfile.TemporaryDirectory(dir=kb.ROOT.parent) as tmp:
   root=Path(tmp)/'repo';shutil.copytree(kb.ROOT,root,ignore=shutil.ignore_patterns('.git','export','__pycache__'))
   p=root/'roboter/unitree_h1/fakten.yaml';d=kb.read_yaml(p)
   d['claims'][0]['sources'][0]['source_id']='src_missing'
   d['claims'][1]['unit']='kg'
   p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False))
   with self.assertRaisesRegex(ValueError,'unbekannte Quelle'): kb.validate(root)
 def test_unknown_cannot_contain_value(self):
  with tempfile.TemporaryDirectory(dir=kb.ROOT.parent) as tmp:
   root=Path(tmp)/'repo';shutil.copytree(kb.ROOT,root,ignore=shutil.ignore_patterns('.git','export','__pycache__'))
   p=root/'roboter/unitree_h1/fakten.yaml';d=kb.read_yaml(p)
   next(c for c in d['claims'] if c['status']=='unbekannt')['value']=False
   p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False))
   with self.assertRaises(ValueError): kb.validate(root)
 def test_deleted_model_removed_from_manifest(self):
  with tempfile.TemporaryDirectory(dir=kb.ROOT.parent) as tmp:
   root=Path(tmp)/'repo';shutil.copytree(kb.ROOT,root,ignore=shutil.ignore_patterns('.git','export','__pycache__'))
   kb.export(root,commit='before')
   shutil.rmtree(root/'roboter/unitree_h1')
   kb.export(root,commit='after')
   manifest=json.loads((root/'export/manifest.json').read_text())
   self.assertFalse(any(x.startswith('unitree_h1:') for x in manifest['chunk_ids']))
 def test_superseded_claim_excluded(self):
  old={'id':'old','supersedes':None,'valid_until':None}
  new={'id':'new','supersedes':'old','valid_until':None}
  self.assertEqual(kb.active_claims({'claims':[old,new]}),[new])
 def test_no_duplicate_yaml_keys(self):
  with self.assertRaises(ValueError): yaml.load('id: a\nid: b\n',Loader=kb.StrictLoader)
 def test_generated_views_reproducible_and_links_valid(self):
  kb.generate();kb.check_links()
  before=(kb.ROOT/'README.md').read_bytes();kb.generate()
  self.assertEqual(before,(kb.ROOT/'README.md').read_bytes())

 def test_import_coverage_and_existing_ids(self):
  manifest=json.loads((kb.ROOT/'recherche/importe/zuordnung_20261029.json').read_text())
  known=json.loads((kb.ROOT/'recherche/importe/bestand_20261029.json').read_text())
  added=json.loads((kb.ROOT/'recherche/importe/ergaenzungen_20261029.json').read_text())
  expected={'B'+r['id'] for r in known}|{f'N{i:02}.{j:02}' for i,r in enumerate(added,1) for j,_ in enumerate(r['models'],1)}
  rows=manifest['positions'];self.assertEqual(len(rows),len(expected))
  self.assertEqual({p['origin'] for p in rows},expected)
  targets=[rid for p in rows for rid in p['target_ids']]
  self.assertEqual(len(targets),len(set(targets)))
  self.assertEqual(set(targets),set(kb.load()[2]))
  self.assertTrue(set(manifest['preserved_seed_ids']).issubset(targets))
 def test_imports_do_not_invent_facts_or_offers(self):
  manifest=json.loads((kb.ROOT/'recherche/importe/zuordnung_20261029.json').read_text())
  robots=kb.load()[2]
  for rid in manifest['created_ids']:
   meta,data,body=robots[rid]
   self.assertEqual(meta['maintenance']['status'],'erfasst')
   self.assertIsNone(meta['maintenance']['reviewed_at'])
   self.assertFalse(data['offers'])
   self.assertTrue(all(c['value'] is None or (c['sources'] and c['checked_at'] and c['evidence'] in ['projektkatalog','herstellerangabe','herstellerdemo']) for c in data['claims']))
 def test_same_name_different_manufacturers_remain_distinct(self):
  robots=kb.load()[2]
  g1=[m for m,d,b in robots.values() if m['name']=='G1']
  self.assertEqual(len(g1),3)
  self.assertEqual(len({m['manufacturer_id'] for m in g1}),3)

if __name__=='__main__':unittest.main()
