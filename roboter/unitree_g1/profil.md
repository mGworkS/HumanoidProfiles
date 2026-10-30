---
schema_version: '1.0'
id: unitree_g1
name: G1
aliases: []
entity_type: modell
manufacturer_id: unitree
developer_ids: []
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. Öffentlicher Einstiegspreis;
    Liefertermin und Zielregion separat bestätigen.
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
relations: []
scope: G1 Basisversion. Andere Editionen sind eigene Profile. Technische Tabelle am 30. Oktober 2026.
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
  access: bestellweg
  reason: Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. Öffentlicher Einstiegspreis;
    Liefertermin und Zielregion separat bestätigen.
  source_ids:
  - src_g1_specs_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# G1

## Einordnung

Kompakte zweibeinige Plattform. Die Basisversion besitzt keinen zugesicherten Entwicklerzugang. Für eigene Policies die EDU Edition prüfen.

## Integration und eigene Entwicklung

Eigene Entwicklung benötigt passende Hardware, SDK Version und ein eigenes Testkonzept. Ein öffentliches Repository allein belegt keine Freischaltung dieser Edition. Ausgereifte autonome Arbeitsaufgaben und eine komplette Integration sind kein automatischer Bestandteil des Hardwarepreises.

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
