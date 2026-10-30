---
schema_version: '1.0'
id: figure_figure_02
name: Figure 02
aliases: []
entity_type: modell
manufacturer_id: figure
developer_ids: []
form: zweibeinig
classification:
  value: historisches_produkt
  reason: Hersteller dokumentiert Ausmusterung der Flotte am 30. September 2026; wenige Geräte bleiben
    eingelagert.
  source_ids:
  - src_figure02_retirement
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: industrie
  basis: dokumentierter_einsatz
  source_ids:
  - src_figure02_bmw_2025
- axis: branche
  id: logistik
  basis: dokumentierter_einsatz
  source_ids:
  - src_figure02_bmw_2025
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_figure02_retirement
relations:
- type: vorgaenger
  target_id: figure_figure_01
- type: nachfolger
  target_id: figure_figure_03
scope: Figure 02. Daten und Fähigkeiten anderer Generationen werden nicht übertragen.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.figure.ai/news/f-02-decommission
  kind: produkt
  source_id: src_figure02_retirement
  verification: geprueft
screening:
  section: historie
  access: kein_bestaetigter_zugang
  reason: Hersteller dokumentiert Ausmusterung der Flotte am 30. September 2026; wenige Geräte bleiben
    eingelagert.
  source_ids:
  - src_figure02_retirement
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Figure 02

## Einordnung

Figure 02 wurde im Produktionspilot eingesetzt und 2026 ausgemustert.

## Integration und eigene Entwicklung

Herstellerinterne KI Entwicklung ist dokumentiert. Offene Gewichte, Trainingsdaten, frei verfügbare Kunden SDKs und eigene Policy Bereitstellung sind nicht bestätigt. Für aktuelle Integrationsvorhaben Figure 03 und spätere Produkte prüfen.

## Einsatzgrenzen und Beleglage

Kennwerte, Lebenszyklus und Erfolge bleiben auf diese Generation begrenzt. Für historische Körpermaße wurde keine verlässlich zugängliche Originaltabelle gefunden; verbreitete Verzeichniswerte bleiben deshalb offen.

## Dokumentationsstand

Generationsbezogenes Herstellerbild und technische HTML Quellen verlinkt. Ein separates öffentliches Herstellerdatenblatt als PDF wurde nicht gefunden. Historische und aktuelle Generationen bleiben getrennt.

## Offene Entscheidungsfragen

* Welche Originalunterlagen und genaue Hardwarekonfiguration sind zugänglich?
* Welche Aufgabenleistung und menschlichen Eingriffe sind nachvollziehbar belegt?
* Welche aktuellen Beschaffungs, Support und Entwicklungsrechte bestehen?
* Welche Sicherheits und Umgebungsgrenzen sind für den konkreten Einsatz bestätigt?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
