---
schema_version: '1.0'
id: honda_asimo_2011
name: ASIMO · Version 2011
aliases: []
entity_type: modell
manufacturer_id: honda
developer_ids:
- honda
form: zweibeinig
classification:
  value: historischer_entwicklungstraeger
  reason: Historische Forschungsplattform; dokumentierter Museumseinsatz bis 2022.
    Kein aktueller Beschaffungsnachweis.
  source_ids:
  - src_asimo_launch
  - src_asimo_museum
  assessed_at: '2026-10-29'
tags:
- axis: branche
  id: forschung
  basis: herstellerziel
  source_ids:
  - src_asimo_launch
- axis: branche
  id: bildung
  basis: dokumentierter_einsatz
  source_ids:
  - src_asimo_museum
- axis: aufgabe
  id: interaktion
  basis: herstellerziel
  source_ids:
  - src_asimo_museum
- axis: umgebung
  id: publikum
  basis: dokumentierter_einsatz
  source_ids:
  - src_asimo_museum
relations: []
scope: Spezifikationsstand November 2011. Frühere ASIMO Versionen und die Familie
  ab 2000 sind nicht derselbe Datensatz.
maintenance:
  last_search: '2026-10-29'
  reviewed_at: '2026-10-29'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://global.honda/en/ASIMO/about/
  kind: produkt
  source_id: src_asimo_specs
  verification: aus_bestand
screening:
  section: historie
  access: unbekannt
  reason: Aktuelle Marktverfügbarkeit beziehungsweise Marktvorstellung noch nicht
    ausreichend geprüft.
  source_ids:
  - src_asimo_launch
  checked_at: null
  basis: bestandsimport
---

# ASIMO · Version 2011

## Einordnung

Historischer humanoider Entwicklungsträger. Erfasst wegen der Nutzung im Betrachtungszeitraum ab 2016. Kein reguläres Kaufprodukt aus der historischen Bedeutung ableiten.

## Offene Entscheidungsfragen

* Exaktes Entwicklungsende separat belegen.
* Keine Annahme über Verkauf, Gebrauchtmarkt oder Support aus dem Museumseinsatz treffen.

## Pflege

Fakten ausschließlich in `fakten.yaml` pflegen. Der lesbare Steckbrief steht in der erzeugten [README.md](README.md).
