from pathlib import Path
import json
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import kb
from presentation import rebase_markdown_links


class NavigationLabelTests(unittest.TestCase):
 def test_document_entry_links_keep_targets_and_anchors(self):
  text='[Profil](../roboter/unitree_g1/README.md#steckbrief) [Ansicht](aktuelle_auswahl.md) [Quelle](https://example.org/a#x) [Hier](#einordnung)'
  moved=rebase_markdown_links(text,'katalog')
  self.assertIn('(roboter/unitree_g1/README.md#steckbrief)',moved)
  self.assertIn('(katalog/aktuelle_auswahl.md)',moved)
  self.assertIn('(https://example.org/a#x)',moved)
  self.assertIn('(#einordnung)',moved)
 def test_all_statuses_and_tags_are_explained(self):
  specs=kb.read_yaml(kb.ROOT/'schema/einordnungen.yaml')['values']
  schema=json.loads((kb.ROOT/'schema/roboter.schema.json').read_text())
  self.assertEqual(set(specs),set(schema['properties']['classification']['properties']['value']['enum']))
  page=(kb.ROOT/'docs/einordnung_und_tags.md').read_text()
  for spec in specs.values():self.assertIn(spec['label'],page)
  axes=kb.read_yaml(kb.ROOT/'schema/taxonomie.yaml')['axes']
  for axis,tags in axes.items():
   for tid,tag in tags.items():self.assertIn(f'[{tag["label"]}](../katalog/{axis}_{tid}.md)',page)
 def test_g1_has_model_image_and_clear_status(self):
  robots=kb.load()[2]
  for rid in ['unitree_g1','unitree_g1_edu']:
   photo=next(x for x in robots[rid][1]['media'] if x['id']=='herstellerbild')
   self.assertEqual(photo['source_id'],'src_g1_product_image_20261030')
   self.assertIn('1_968fd08b-9aaf-4f32-b895-5c786285ee52.jpg',photo['url'])
   page=(kb.ROOT/'roboter'/rid/'README.md').read_text()
   self.assertIn('| Einordnung | [Aktuelles Modell]',page)
   self.assertNotIn('| Einordnung | gegenwaertig',page)
   for label in ['Branchen','Aufgaben','Umgebungen']:self.assertIn('| '+label+' |',page)
 def test_start_page_opens_documents_instead_of_directories(self):
  page=(kb.ROOT/'README.md').read_text()
  self.assertIn('](KATALOG.md)',page)
  self.assertIn('](HERSTELLER.md)',page)
  self.assertTrue((kb.ROOT/'KATALOG.md').is_file())
  self.assertIn('](hersteller/neura_robotics/README.md)',(kb.ROOT/'HERSTELLER.md').read_text())
  self.assertIn('](roboter/unitree_g1/README.md)',(kb.ROOT/'KATALOG.md').read_text())


if __name__=='__main__':unittest.main()
