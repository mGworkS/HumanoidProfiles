import copy
from datetime import date
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import kb
from screening import section
from views import render_table

class ScreeningTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sources,cls.orgs,cls.robots,cls.metrics,cls.axes=kb.load()
  cls.policy=kb.read_yaml(kb.ROOT/'schema/screening_policy.yaml')
  cls.day=date(2026,10,30)
 def test_history_and_unavailable_research_excluded_from_main(self):
  for rid in ['pepper_classic','honda_asimo_2011','figure_figure_02','aist_und_kawada_hrp_5p']:
   m,d,b=self.robots[rid]
   self.assertNotEqual(section(m,d,self.day,self.policy),'aktuell')
 def test_older_available_research_platform_is_eligible(self):
  m,d,b=self.robots['pal_robotics_talos']
  self.assertEqual(section(m,d,self.day,self.policy),'aktuell')
  first=next(c for c in d['claims'] if c['key']=='lifecycle.first_presented')
  self.assertLess(first['value'],'2020')
 def test_expired_or_unproven_inclusion_falls_back_to_review(self):
  m,d,b=self.robots['unitree_h1'];m=copy.deepcopy(m)
  m['screening']['checked_at']='2025-01-01'
  self.assertEqual(section(m,d,self.day,self.policy),'ungeklaert')
  m['screening']['checked_at']='2026-10-30';m['screening']['basis']='bestandsimport'
  self.assertEqual(section(m,d,self.day,self.policy),'ungeklaert')
 def test_history_overrides_manual_current_flag(self):
  m,d,b=self.robots['pepper_classic'];m=copy.deepcopy(m)
  m['screening']=copy.deepcopy(self.robots['unitree_h1'][0]['screening'])
  self.assertEqual(section(m,d,self.day,self.policy),'historie')
 def test_construction_keeps_research_in_its_own_table(self):
  page=(kb.ROOT/'katalog/branche_bau.md').read_text()
  self.assertIn('aist_und_kawada_hrp_5p',page)
  self.assertNotIn('aist_und_kawada_hrp_5p',page.split('<details>')[0])
  self.assertIn('aist_und_kawada_hrp_5p',(kb.ROOT/'katalog/aufgabe_manipulation.md').read_text())
  self.assertNotIn('aist_und_kawada_hrp_5p',(kb.ROOT/'katalog/aktuelle_auswahl.md').read_text())
 def test_overviews_show_required_fields_and_qualified_payload(self):
  table=render_table(['unitree_g1','agility_digit5'],self.robots,self.orgs,self.policy,self.day)
  for heading in ['Hersteller','Ursprungsland','Vorstellung','Verkaufsstart','Höhe','Payload']:
   self.assertIn(heading,table)
  self.assertIn('je Arm',table);self.assertIn('22.7 kg; Lastbezug beachten (angekündigt)',table)
  self.assertNotIn('22.7 kg beidhändig',table)
 def test_official_link_and_environment_label_in_profile(self):
  page=(kb.ROOT/'roboter/deep_dr02/README.md').read_text()
  self.assertIn('https://en.deeprobotics.cn/en/index/dr02.html',page)
  self.assertIn('../../docs/legende.md',page)
  self.assertIn('../docs/legende.md',(kb.ROOT/'katalog/aktuelle_auswahl.md').read_text())
  self.assertIn('Umgebung mit Besuchern oder Kunden',(kb.ROOT/'README.md').read_text())
  self.assertNotIn('* [Publikumsverkehr]',(kb.ROOT/'README.md').read_text())

if __name__=='__main__':unittest.main()
