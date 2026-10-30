---
schema_version: '1.0'
id: unitree_g1_edu
name: G1 EDU
aliases: []
entity_type: variante
manufacturer_id: unitree
developer_ids: []
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. EDU über Vertrieb abzustimmen.
  source_ids:
  - src_g1_specs_20261030
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: forschung
  basis: herstellerziel
  source_ids:
  - src_g1_specs_20261030
- axis: branche
  id: bildung
  basis: herstellerziel
  source_ids:
  - src_g1_specs_20261030
- axis: aufgabe
  id: interaktion
  basis: herstellerziel
  source_ids:
  - src_g1_specs_20261030
- axis: aufgabe
  id: policy_training
  basis: herstellerziel
  source_ids:
  - src_unitree_rl_20261030
relations:
- type: variante_von
  target_id: unitree_g1
scope: G1 EDU. Andere Editionen sind eigene Profile. Technische Tabelle am 30. Oktober 2026.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.unitree.com/g1/
  kind: produkt
  source_id: src_g1_specs_20261030
  verification: geprueft
screening:
  section: aktuell
  access: anfrage
  reason: Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. EDU über Vertrieb abzustimmen.
  source_ids:
  - src_g1_specs_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# G1 EDU

## Einordnung

Kompakte zweibeinige Plattform. Die EDU Edition ist für eigene Entwicklung vorgesehen.

## Integration und eigene Entwicklung

Eigene Entwicklung benötigt passende Hardware, SDK Version und ein eigenes Testkonzept. G1 RL Gym dokumentiert Bewegungslernen und Sim2Real. Ausgereifte autonome Arbeitsaufgaben und eine komplette Integration sind kein automatischer Bestandteil des Hardwarepreises.

## Einsatzgrenzen und Beleglage

Armnutzlast ist haltungsabhängig. Aus Sensorik und Herstelleraufnahmen folgt keine garantierte Sturzvermeidung. Für Treppen, Geröll, Staub und dynamische Hindernisse fehlen hier konfigurationsbezogene Betriebsgrenzen.

## Dokumentationsstand

Technische HTML Tabelle und offizieller Handbucheinstieg verlinkt. Allgemeine PDF nicht gefunden. Bilder sind externe Herstellerverweise mit Konfigurationshinweis.

## Offene Entscheidungsfragen

* Welche genaue Achsen, Hände und Rechenmodule enthält das Angebot?
* Welche SDK und Policy Funktionen sind auf dieser Seriennummer freigeschaltet?
* Welche Nutzlast, Betriebsdauer und Bodenbedingungen werden im Abnahmetest erreicht?
* Welche regionalen Lieferbedingungen, Lizenzen, Abos und Sicherheitsunterlagen gelten?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
