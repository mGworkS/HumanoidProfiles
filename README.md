<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->

# HumanoidProfiles

Wissensbasis zur Auswahl humanoider Roboter und zur branchenübergreifenden Recherche.

**[Aktuelle Roboter vergleichen](katalog/aktuelle_auswahl.md): 71 Einträge** mit Hersteller, Ursprungsland, Vorstellung, Verkaufsstart, Zugang, Höhe und Payload. Vorbestellungen und kommerziell vorgestellte Entwicklungen sind eingeschlossen und erkennbar. Die Auswahl wird durch dokumentierte Quellen und Aktualität begrenzt.

**Wissensbestand:** 236 Profile (2 Entwicklungsprogramme, 8 Familien, 209 Modelle, 17 Varianten). Unterschiedliche Varianten und Quellenstände beachten.

**[Legende zu Spalten, Kürzeln und Nachweisen](docs/legende.md)**

## Aktuelle Auswahl nach Branchen

Ein Roboter darf unter mehreren Branchen oder Aufgaben erscheinen. Alle Links zeigen auf dasselbe Profil. Die Zuordnung ist keine Eignungszusage. Kategorien bleiben auch ohne aktuellen Treffer sichtbar.

* [Industrie](katalog/branche_industrie.md)
* [Logistik](katalog/branche_logistik.md)
* [Gesundheit und Pflege](katalog/branche_gesundheit_pflege.md)
* [Einzelhandel](katalog/branche_einzelhandel.md)
* [Bildung](katalog/branche_bildung.md)
* [Forschung](katalog/branche_forschung.md)
* [Unterhaltung](katalog/branche_unterhaltung.md)
* [Service](katalog/branche_service.md)
* [Landwirtschaft](katalog/branche_landwirtschaft.md)
* [Bau und Bauwirtschaft](katalog/branche_bau.md)
* [Haushalt](katalog/branche_haushalt.md)
* [Sicherheit und Rettung](katalog/branche_sicherheit_rettung.md)
* [Raumfahrt](katalog/branche_raumfahrt.md)

## Aufgaben

* [Transport](katalog/aufgabe_transport.md)
* [Interaktion](katalog/aufgabe_interaktion.md)
* [Manipulation](katalog/aufgabe_manipulation.md)
* [Policy Training](katalog/aufgabe_policy_training.md)
* [Inspektion](katalog/aufgabe_inspektion.md)

## Einsatzumgebungen

* [Innenraum](katalog/umgebung_innen.md)
* [Außenbereich](katalog/umgebung_aussen.md)
* [Umgebung mit Besuchern oder Kunden](katalog/umgebung_publikum.md)

## Weitere Ansichten

* [Vorbestellungen und vorgestellte Entwicklungen](katalog/entwicklungspipeline.md)
* [Forschungsplattformen ohne bestätigten externen Zugang](katalog/forschungsplattformen.md)
* [Noch zu prüfende Einträge](katalog/ungeprueft.md)
* [Historie und frühere Generationen](katalog/historie.md)
* [Gesamtbestand in getrennten Tabellen](katalog/gesamtbestand.md)

## Pflegen und erweitern

* [Architektur](docs/architektur.md)
* [Legende zu Merkmalen und Kürzeln](docs/legende.md)
* [Screeningregeln](docs/screening.md)
* [Datenregeln](docs/datenregeln.md)
* [Pflegeprozess](docs/pflegeprozess.md)
* [Steckbrief](docs/steckbrief.md)
* [Vorlagen](vorlagen/README.md)
* [Importnachweis](recherche/importe/README.md)
* [Offene Recherchekandidaten](recherche/kandidaten/README.md)
* [RAG und strukturierte Auswahl](docs/rag.md)
* [Änderungen](CHANGELOG.md)

## Lokal ausführen

```sh
python -m pip install -r requirements.txt
python scripts/kb.py validate
python scripts/kb.py build
python -m unittest discover -s tests -v
python scripts/kb.py export
python scripts/kb.py query --mode screening
```

Die lesbaren Ansichten werden automatisch aus den Originaldaten erzeugt. Exportdateien werden nicht versioniert. Noch kein gehostetes RAG System und keine automatische Webrecherche eingerichtet.
