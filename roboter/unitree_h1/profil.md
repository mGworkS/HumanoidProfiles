---
schema_version: '1.0'
id: unitree_h1
name: H1
aliases: []
entity_type: modell
manufacturer_id: unitree
developer_ids:
- unitree
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Produktseite und offizieller Entwicklungsworkflow verfügbar; Produktionsstatus
    separat ungeklärt.
  source_ids:
  - src_h1_product
  - src_h1_rl
  assessed_at: '2026-10-29'
tags:
- axis: branche
  id: forschung
  basis: redaktionelle_zuordnung
  source_ids:
  - src_h1_rl
- axis: aufgabe
  id: policy_training
  basis: dokumentierte_funktion
  source_ids:
  - src_h1_rl
relations: []
scope: H1 Originalmodell. H1-2 ist eine andere Ausführung; deren Nutzlast und Freiheitsgrade
  gelten hier nicht.
maintenance:
  last_search: '2026-10-29'
  reviewed_at: '2026-10-29'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
---

# H1

## Einordnung

Humanoide Entwicklungsplattform mit dokumentiertem Workflow für eigene Bewegungssteuerung. Industrielle Einsatzreife ist aufgabenbezogen zu prüfen.

## Offene Entscheidungsfragen

* Aktuelle H1 Beschaffung einschließlich Konfiguration und Region bestätigen.
* Nutzlast, IP Schutz und Laufzeit für konkrete Aufgaben fehlen.
* Lizenzen aller Trainingsabhängigkeiten und kommerzielle Rechte gesondert prüfen.

## Pflege

Fakten ausschließlich in `fakten.yaml` pflegen. Der lesbare Steckbrief steht in der erzeugten [README.md](README.md).
