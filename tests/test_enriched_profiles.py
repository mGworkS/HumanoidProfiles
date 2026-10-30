from datetime import date
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import kb

class EnrichedProfileTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sources,cls.orgs,cls.robots,cls.metrics,cls.axes=kb.load()
 def test_variants_do_not_gain_unlicensed_or_missing_capabilities(self):
  def known(rid,key):
   return [c for c in kb.active_claims(self.robots[rid][1]) if c['key']==key and c['value'] is not None]
  self.assertIn('nicht unterstützt',known('unitree_g1','openness.sdk')[0]['value'])
  self.assertTrue(known('unitree_g1_edu','openness.training_code'))
  self.assertFalse(known('unitree_g1_plus_edu','openness.policy_deployment'))
  self.assertFalse(known('neura_4ne1_mini_standard','hardware.payload_rated'))
  self.assertIn('nicht im Standard',known('neura_4ne1_mini_standard','manipulation.scope')[0]['value'])
  for key in ['hardware.height','hardware.mass','hardware.payload_arm']:
   self.assertFalse(known('neura_robotics_r_4ne1_gen_4',key))
 def test_media_and_ai_records_survive_export(self):
  index,chunks=kb.export(commit='media-test',as_of=date(2026,10,30))
  row=next(r for r in index if r['robot_id']=='unitree_g1_edu')
  simulated=[x for x in row['ai_systems'] if x['relationship']=='simulation']
  self.assertEqual(len(simulated),3)
  self.assertTrue(all(x['source_ids'] for x in simulated))
  self.assertTrue(any(x['relationship']=='referenzintegration' for x in row['ai_systems']))
  self.assertEqual(kb.ai_records(self.robots['unitree_g1'][1]),[])
  self.assertTrue(any(c['kind']=='media' and c['record']['type']=='datenblatt' for c in chunks))
  self.assertTrue(any(c['kind']=='extension' and c['source_ids'] for c in chunks))
  self.assertTrue(all('notice' in c for c in chunks if c['kind']=='media'))
 def test_navigation_and_profile_information_are_visible(self):
  catalog=(kb.ROOT/'katalog/README.md').read_text()
  self.assertEqual(catalog,(kb.ROOT/'katalog/gesamtbestand.md').read_text())
  self.assertLess(catalog.index('## Historie'),catalog.index('## Noch zu prüfende'))
  manufacturers=(kb.ROOT/'hersteller/README.md').read_text()
  self.assertIn('neura_robotics/README.md',manufacturers)
  profile=(kb.ROOT/'roboter/figure_figure_03/README.md').read_text()
  for text in ['| Offizielle Website |','| Vorstellung und weitere Videos |','## KI, Modelle und Software','## Modellspezifische Besonderheiten','## Integration und eigene Entwicklung']:
   self.assertIn(text,profile)
  self.assertIn('![',profile)
  self.assertIn('Helix 2.5',profile)
  self.assertIn('src_figure03_bmw_2026',profile)
 def test_selected_profiles_have_scoped_original_media(self):
  selected=json.loads((kb.ROOT/'recherche/importe/ergaenzungen_20261030_profile.json').read_text())['enriched_ids']
  for rid in selected:
   data=self.robots[rid][1]
   self.assertTrue(any(m['type'] in ['foto','rendering'] for m in data['media']),rid)
   self.assertTrue(any(m['type']=='datenblatt' for m in data['media']),rid)
   self.assertTrue(data['extensions'],rid)
   self.assertTrue(all(m['rights'] and m['scope'] and m['source_id'] in self.sources for m in data['media']))
 def test_delivery_scope_does_not_turn_demos_into_included_functions(self):
  figure=kb.capability_records(self.robots['figure_figure_03'][1])
  pick=next(c for c in figure if c['key']=='manipulation.pick_place')
  self.assertEqual(pick['delivery'],'demo')
  pepper=kb.capability_records(self.robots['pepper_classic'][1])
  navigation=next(c for c in pepper if c['key']=='navigation.scope')
  self.assertEqual(navigation['delivery'],'eigene_entwicklung')
  digit=kb.capability_records(self.robots['agility_robotics_digit_generation_4'][1])
  self.assertEqual(next(c for c in digit if c['key']=='fleet.management')['delivery'],'projektintegration')
  erp=next(c for c in digit if c['key']=='integration.erp')
  self.assertIsNone(erp['value'])
  self.assertEqual(erp['delivery'],'unbekannt')
  page=(kb.ROOT/'roboter/pepper_classic/README.md').read_text()
  self.assertIn('## Fähigkeiten und Lieferumfang',page)
  self.assertIn('## Navigation, Flotte und Unternehmens IT',page)

if __name__=='__main__':unittest.main()
