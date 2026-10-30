---
schema_version: '1.0'
id: neura_4ne1_mini_pro
name: 4NE1 Mini Pro
aliases: []
entity_type: variante
manufacturer_id: neura_robotics
developer_ids: []
form: zweibeinig
classification:
  value: pipeline
  reason: Standard und Pro reservierbar; Verfügbarkeit 2026 angekündigt. Keine bestätigte Kundenauslieferung
    in den geprüften Quellen.
  source_ids:
  - src_neura_mini_reservation_20261030
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: bildung
  basis: herstellerziel
  source_ids:
  - src_neura_mini_reservation_20261030
- axis: branche
  id: unterhaltung
  basis: herstellerziel
  source_ids:
  - src_neura_mini_reservation_20261030
- axis: branche
  id: forschung
  basis: herstellerziel
  source_ids:
  - src_neura_mini_reservation_20261030
- axis: aufgabe
  id: interaktion
  basis: herstellerziel
  source_ids:
  - src_neura_mini_reservation_20261030
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_neura_mini_reservation_20261030
relations:
- type: variante_von
  target_id: neura_robotics_r_4ne1_mini
scope: 4NE1 Mini Pro. Reservierungsstand Oktober 2026.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://neura-robotics.com/product/4ne1-mini-reservation/
  kind: produkt
  source_id: src_neura_mini_reservation_20261030
  verification: geprueft
screening:
  section: aktuell
  access: vorbestellung
  reason: Standard und Pro reservierbar; Verfügbarkeit 2026 angekündigt. Keine bestätigte Kundenauslieferung
    in den geprüften Quellen.
  source_ids:
  - src_neura_mini_reservation_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# 4NE1 Mini Pro

## Einordnung

Kompakte reservierbare Plattform für Bildung und Interaktion. Standard und Pro unterscheiden sich beim Manipulationspaket und Entwicklerumfang.

## Integration und eigene Entwicklung

Python und ROS 2 sind angekündigt. Pro ergänzt C++, digitalen Zwilling, Teleoperation und Vorbereitung auf NEURA Gym. Daraus folgen keine bestätigten offenen Gewichte, Trainingsdaten oder uneingeschränkten Policy Rechte. Ein Integrationsangebot sollte Hardware, Software, Neuraverse und Betreuung einzeln ausweisen.

## Einsatzgrenzen und Beleglage

Treppen sind noch Entwicklungsgegenstand. Die angegebenen Plattformwerte sind Ankündigungsdaten. Dauerbetrieb und Bewegungsausdauer sind unterschiedliche Größen. Der frühere Frühjahrstermin im PDF belegt keine erfolgte Auslieferung.

## Dokumentationsstand

Original PDF V1 und aktuelle Konfigurationstabelle sind verlinkt. Konflikte zwischen pauschaler PDF Schnittstellenliste und editionsbezogener Tabelle sind ausdrücklich beschrieben.

## Offene Entscheidungsfragen

* Ist diese konkrete Edition lieferbar und welche finale Ausstattung besitzt sie?
* Welche Manipulationsfunktionen und Nutzlastgrenzen gelten für Pro?
* Welche eigenen Policies und kommerziellen Anwendungen sind erlaubt?
* Welche Kosten entstehen für Cloud, Updates, Apps, Training und Support?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
