# Architektur 1.0

Die Wissensbasis ist branchenoffen und erfasst humanoide Modelle, relevante Varianten, Forschungsplattformen, Programme und historische Systeme. Die fünf Startprofile sind ein geprüfter Strukturpilot, keine vollständige Inventarmigration.

## Kanonische Dateien

```text
README.md                         erzeugter Einstieg
AGENTS.md                         Arbeitsregeln für Agenten
hersteller/<id>/profil.md          Unternehmenszuordnung und Text
hersteller/<id>/README.md          erzeugtes Portfolio
roboter/<id>/profil.md             Identität, Einordnung und Beschreibung
roboter/<id>/fakten.yaml           belegte Aussagen, Angebote, Ereignisse, Medien
roboter/<id>/README.md             erzeugter lesbarer Steckbrief
roboter/<id>/assets/               rechtlich geprüfte Medien
roboter/<id>/dokumente/            versionierte Originaldokumente
quellen/<id>.md                    zentrale Quellenbeschreibung
schema/                           Schemata, Merkmale und Taxonomie
vorlagen/                         bearbeitbare Muster und Anleitungen
katalog/                          erzeugte Mehrfachansichten
recherche/kandidaten/              ungeklärte Funde
recherche/laeufe/                  dokumentierte Suchläufe
recherche/quellenmonitoring.yaml   Quellen und Suchintervalle
scripts/kb.py                     Prüfung, Ansichten, Export, Auswahl
scripts/new_robot.py              neues Profil ohne erfundene Werte
scripts/check_generated.py        Prüfung reproduzierbarer Ansichten
export/                           erzeugt und nicht versioniert
```

## Bewusste Vereinfachung

Für jedes Modell gibt es genau zwei Originaldateien. profil.md enthält kurze Metadaten und redaktionellen Text. fakten.yaml enthält gleichartig strukturierte Fakten sowie klar getrennte Listen für Angebote und Ereignisse. Die zuvor diskutierten vielen Teildateien werden zum Start nicht benötigt. Eine spätere Aufteilung ist eine Migration, keine Änderung der fachlichen Bedeutung.

Ein kleiner Satz von Entscheidungsfeldern ist verpflichtend, ein unbekannter Wert ist zulässig. Zusätzliche Merkmale werden registriert und nur bei Bedarf erfasst. Es gibt keinen gemeinsamen Fähigkeitskatalog, dessen Werte pauschal für alle Humanoiden gelten.

Jede Information wird einmal gepflegt. Mehrere Branchenansichten verlinken dasselbe Modell. Ein generierter Steckbrief und ein RAG Abschnitt dürfen dieselbe Quelle wiedergeben, sind aber keine zusätzlichen Originaldatensätze.

## Grenzen und Ausbau

Kein gehostetes RAG System, keine automatische Webrecherche und keine Rechtsprüfung sind eingerichtet. Der Export stellt die geprüfte Grundlage bereit. Ein späteres Frontend kann dieselben Dateien über Formulare bearbeiten.

Schemas haben eine eigene Version. Neue optionale Merkmale und Tags benötigen keine neue Profilstruktur. Umbenennungen oder Bedeutungsänderungen bestehender Felder benötigen Migration, Tests und eine neue Schemafassung. Alte IDs werden nicht neu vergeben.

Erstellte Texte und Software erhalten hier noch keine pauschale Veröffentlichungslizenz. Rechte an fremden Quellen und Medien bleiben beim jeweiligen Rechteinhaber. Lizenzentscheidung durch den Repository Eigentümer offen.
