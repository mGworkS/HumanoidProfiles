---
schema_version: '1.0'
id: agility_digit5
name: Digit 5
aliases: []
entity_type: modell
manufacturer_id: agility_robotics
developer_ids:
- agility_robotics
form: zweibeinig
classification:
  value: pipeline
  reason: Produktseite bezeichnet Digit 5 ausdrücklich als in Entwicklung.
  source_ids:
  - src_digit5_product
  assessed_at: '2026-10-29'
tags:
- axis: branche
  id: industrie
  basis: herstellerziel
  source_ids:
  - src_digit5_launch
- axis: branche
  id: logistik
  basis: herstellerziel
  source_ids:
  - src_digit5_launch
- axis: aufgabe
  id: transport
  basis: herstellerziel
  source_ids:
  - src_digit5_launch
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_digit5_launch
relations: []
scope: Digit 5. Betriebserfahrung, Einsatzzahlen und Kundenbelege von Digit 4 werden
  nicht übertragen.
maintenance:
  last_search: '2026-10-29'
  reviewed_at: '2026-10-29'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.agilityrobotics.com/solutions/digit-5
  kind: produkt
  source_id: src_digit5_product
  verification: geprueft
screening:
  section: aktuell
  access: vorgestellt
  reason: Digit 5 Entwicklung vorgestellt; Zugang für 2027 angekündigt. Keine bestätigte
    Auslieferung.
  source_ids:
  - src_digit5_launch
  - src_digit5_product
  checked_at: '2026-10-29'
  basis: primaerquelle
---

# Digit 5

## Einordnung

Angekündigte nächste Digit Generation. Vorläufige Werte und geplante Arbeitsabläufe sind keine bestätigten Kundenleistungen.

## Offene Entscheidungsfragen

* Lieferbeginn 2027 erneut prüfen; Termin nicht automatisch als erfüllt behandeln.
* Kauf oder RaaS, Vertragskosten, Regionen und Kundenzugang konkret bestätigen.
* Offene Entwicklungsrechte, Cloudzwang und Integrationsleistungen abklären.

## Pflege

Fakten ausschließlich in `fakten.yaml` pflegen. Der lesbare Steckbrief steht in der erzeugten [README.md](README.md).
