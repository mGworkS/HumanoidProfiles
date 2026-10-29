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
  self.assertEqual(kb.validate(),5)
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
  claims=[c for c in data['claims'] if c['key'].startswith('hardware.payload')]
  self.assertTrue(claims)
  self.assertTrue(all(c['value'] is None and c['status']=='unbekannt' for c in claims))
 def test_historical_model_in_reference_export(self):
  with tempfile.TemporaryDirectory(dir=kb.ROOT.parent) as tmp:
   root=Path(tmp)/'repo';shutil.copytree(kb.ROOT,root,ignore=shutil.ignore_patterns('.git','export','__pycache__'))
   index,chunks=kb.export(root,commit='test')
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

if __name__=='__main__':unittest.main()
