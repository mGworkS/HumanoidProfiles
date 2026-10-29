<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->

# HumanoidProfiles

Quellenbasierte Wissensbasis für humanoide Roboter. Für Menschen lesbar und für strukturierte Auswahl sowie RAG exportierbar. Branchen, Aufgaben und Umgebungen sind erweiterbare Tags.

**Erfasster Bestand:** 236 Profile. 2 entwicklungsprogramm, 8 familie, 209 modell, 17 variante. Der Großteil wurde aus vorhandenen Listen übernommen und ist noch fachlich zu prüfen. Keine Vollständigkeitsbehauptung und keine pauschale Kaufempfehlung. Herstellerangaben, Ankündigungen und unabhängige Nachweise bleiben unterscheidbar.

## Einstieg

* [Gegenwärtige Plattformen](katalog/gegenwaertig.md)
* [Entwicklungspipeline](katalog/entwicklungspipeline.md)
* [Erfasste Profile mit offener Prüfung](katalog/ungeprueft.md)

## Branchen, Aufgaben und Umgebungen

* [Industrie](katalog/branche_industrie.md) (branche)
* [Logistik](katalog/branche_logistik.md) (branche)
* [Gesundheit und Pflege](katalog/branche_gesundheit_pflege.md) (branche)
* [Einzelhandel](katalog/branche_einzelhandel.md) (branche)
* [Bildung](katalog/branche_bildung.md) (branche)
* [Forschung](katalog/branche_forschung.md) (branche)
* [Unterhaltung](katalog/branche_unterhaltung.md) (branche)
* [Service](katalog/branche_service.md) (branche)
* [Haushalt](katalog/branche_haushalt.md) (branche)
* [Sicherheit und Rettung](katalog/branche_sicherheit_rettung.md) (branche)
* [Raumfahrt](katalog/branche_raumfahrt.md) (branche)
* [Transport](katalog/aufgabe_transport.md) (aufgabe)
* [Interaktion](katalog/aufgabe_interaktion.md) (aufgabe)
* [Manipulation](katalog/aufgabe_manipulation.md) (aufgabe)
* [Policy Training](katalog/aufgabe_policy_training.md) (aufgabe)
* [Inspektion](katalog/aufgabe_inspektion.md) (aufgabe)
* [Innenraum](katalog/umgebung_innen.md) (umgebung)
* [Außenbereich](katalog/umgebung_aussen.md) (umgebung)
* [Publikumsverkehr](katalog/umgebung_publikum.md) (umgebung)

## Historie und vollständiger erfasster Bestand

* [Historie und frühere Generationen](katalog/historie.md)
* [Alle erfassten Modelle](katalog/gesamtbestand.md)

## Pflegen und erweitern

* [Architektur und Dateistruktur](docs/architektur.md)
* [Datenregeln](docs/datenregeln.md)
* [Pflege und neue Recherche](docs/pflegeprozess.md)
* [Vollständiges Merkmalsverzeichnis](schema/merkmale.yaml)
* [Vorlagen](vorlagen/README.md)
* [Vollständiger Importnachweis](recherche/importe/README.md)
* [Recherchekandidaten](recherche/kandidaten/README.md)
* [RAG und Auswahlregeln](docs/rag.md)
* [Änderungen](CHANGELOG.md)

## Lokal ausführen

```sh
python -m pip install -r requirements.txt
python scripts/kb.py validate
python scripts/kb.py build
python -m unittest discover -s tests -v
python scripts/kb.py export
python scripts/kb.py query --mode procurement --region EU --audience unternehmen
```

`export/` ist abgeleitet und wird nicht versioniert. `README.md`, die Kataloge und die Modellansichten sind automatisch erzeugt. Es läuft noch kein gehostetes RAG System und keine automatische Webrecherche.
