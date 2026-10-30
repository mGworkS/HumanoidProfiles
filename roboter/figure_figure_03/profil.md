---
schema_version: '1.0'
id: figure_figure_03
name: Figure 03
aliases: []
entity_type: modell
manufacturer_id: figure
developer_ids: []
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Aktuelle Generation mit dokumentierter Produktion und Herstellerdemo bei BMW; allgemeiner Kaufzugang
    nicht bestätigt.
  source_ids:
  - src_figure03_specs_20261030
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: industrie
  basis: dokumentierter_einsatz
  source_ids:
  - src_figure03_bmw_2026
- axis: branche
  id: logistik
  basis: dokumentierter_einsatz
  source_ids:
  - src_figure03_bmw_2026
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_figure03_specs_20261030
- axis: branche
  id: haushalt
  basis: herstellerziel
  source_ids:
  - src_figure_helix02_2026
relations:
- type: vorgaenger
  target_id: figure_figure_02
scope: Figure 03. Daten und Fähigkeiten anderer Generationen werden nicht übertragen.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.figure.ai/figure
  kind: produkt
  source_id: src_figure03_specs_20261030
  verification: geprueft
screening:
  section: aktuell
  access: projektzugang
  reason: Aktuelle Generation mit dokumentierter Produktion und Herstellerdemo bei BMW; allgemeiner Kaufzugang
    nicht bestätigt.
  source_ids:
  - src_figure03_specs_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Figure 03

## Einordnung

Figure 03 ist die aktuelle Generation mit Helix basierter Ganzkörpersteuerung und industriellen sowie häuslichen Entwicklungszielen.

## Integration und eigene Entwicklung

Herstellerinterne KI Entwicklung ist dokumentiert. Offene Gewichte, Trainingsdaten, frei verfügbare Kunden SDKs und eigene Policy Bereitstellung sind nicht bestätigt. Beschaffung und Integration erfolgen nach individueller Abstimmung; allgemeine Kaufpreise und öffentliche RaaS Tarife sind hier nicht belegt.

## Einsatzgrenzen und Beleglage

Kennwerte, Lebenszyklus und Erfolge bleiben auf diese Generation begrenzt. 20 kg Payload ist ohne präzisen Lastbezug veröffentlicht. Herstellerdemos ersetzen keine kundenspezifischen Abnahmetests. Staubschutz und Außeneinsatz sind nicht allein aus Gehfähigkeit ableitbar.

## Dokumentationsstand

Generationsbezogenes Herstellerbild und technische HTML Quellen verlinkt. Ein separates öffentliches Herstellerdatenblatt als PDF wurde nicht gefunden. Historische und aktuelle Generationen bleiben getrennt.

## Offene Entscheidungsfragen

* Welche Originalunterlagen und genaue Hardwarekonfiguration sind zugänglich?
* Welche Aufgabenleistung und menschlichen Eingriffe sind nachvollziehbar belegt?
* Welche aktuellen Beschaffungs, Support und Entwicklungsrechte bestehen?
* Welche Sicherheits und Umgebungsgrenzen sind für den konkreten Einsatz bestätigt?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
