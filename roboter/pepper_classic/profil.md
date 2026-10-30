---
schema_version: '1.0'
id: pepper_classic
name: Pepper · klassische Plattform
aliases: []
entity_type: modell
manufacturer_id: softbank_robotics
developer_ids:
- aldebaran
- softbank_robotics
form: raeder
classification:
  value: historisch_relevant
  reason: Historisch prägende soziale Plattform mit weiter verfügbaren Produkt und Entwicklerseiten. Heutige
    regionale Kaufverfügbarkeit und Produktionsende bleiben separat offen.
  source_ids:
  - src_pepper_cn_hardware_20261030
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: service
  basis: herstellerziel
  source_ids:
  - src_pepper_uses
- axis: branche
  id: bildung
  basis: herstellerziel
  source_ids:
  - src_pepper_uses
- axis: branche
  id: gesundheit_pflege
  basis: herstellerziel
  source_ids:
  - src_pepper_uses
- axis: branche
  id: einzelhandel
  basis: herstellerziel
  source_ids:
  - src_pepper_uses
- axis: aufgabe
  id: interaktion
  basis: herstellerziel
  source_ids:
  - src_pepper_uses
- axis: umgebung
  id: innen
  basis: herstellerziel
  source_ids:
  - src_pepper_manual
relations: []
scope: Klassische Pepper Plattform. Japan Startkonfiguration 2015 und undatiertes China Hardwaredokument
  getrennt beachten. Pepper+ ausgeschlossen. Software 2.5 und 2.9 getrennt.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.softbank.jp/en/robot/
  kind: produkt
  source_id: src_pepper_cn_hardware_20261030
  verification: geprueft
screening:
  section: historie
  access: unbekannt
  reason: Historisch prägende soziale Plattform mit weiter verfügbaren Produkt und Entwicklerseiten. Heutige
    regionale Kaufverfügbarkeit und Produktionsende bleiben separat offen.
  source_ids:
  - src_pepper_cn_hardware_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Pepper · klassische Plattform

## Einordnung

Soziale Plattform auf Rädern für Interaktion. Gesundheits und Pflegezuordnungen beschreiben Einsatzfelder, keine medizinische Wirksamkeit. Historische Relevanz ist unabhängig von aktuellem Support oder regionalen Restangeboten.

## Integration und eigene Entwicklung

Eigene Anwendungen sind möglich, aber NAOqi 2.5 und Android mit NAOqi 2.9 besitzen unterschiedliche Entwicklungswege. SDK Zugang bedeutet keine offene Gesamtsteuerung oder freie eigene Ganzkörper Policies. Für Integration sind Softwareversion, Konten, Appverteilung, Sprachdienste und Support entscheidend.

## Einsatzgrenzen und Beleglage

IPX0 und die Temperaturspanne stammen aus dem verlinkten Hardwaredokument. Es bestätigt keine Staubeignung. Die Rollenplattform ist für normale Treppen ungeeignet. Unterschiedliche offizielle Massenwerte bleiben mit Quellen und Konfigurationen sichtbar; ein Mittelwert wird nicht gebildet.

## Dokumentationsstand

Offizielles Hardware PDF, Herstellerbild und Entwicklerdokumentation verlinkt. Der zuvor gespeicherte Handbuchlink 2019 war nicht abrufbar; daraus werden keine neuen Werte übernommen. Historische Japan Preise werden nicht als aktuelle Angebote geführt.

## Offene Entscheidungsfragen

* Welche Hardware und NAOqi Version wird tatsächlich angeboten?
* Welche regionale Liefer und Supportzusage besteht heute?
* Welche Dienste, Apps und Konten funktionieren noch und welche Abos sind nötig?
* Welche Traglast und Manipulationsfunktionen sind für die eigene Anwendung ausdrücklich freigegeben?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
