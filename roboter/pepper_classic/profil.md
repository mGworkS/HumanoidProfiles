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
  reason: Frühe soziale Plattform; historische Relevanz sagt nichts über heutige regionale
    Angebote aus.
  source_ids:
  - src_pepper_launch
  assessed_at: '2026-10-29'
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
scope: Klassische Pepper Plattform mit technischen Angaben aus Handbuch 2019. Erstvorstellung
  bezieht sich auf die Plattform 2014. Pepper+ nicht enthalten; Konfiguration beim
  Kauf abgleichen.
maintenance:
  last_search: '2026-10-29'
  reviewed_at: '2026-10-29'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
---

# Pepper · klassische Plattform

## Einordnung

Soziale Plattform für Kommunikation. Healthcare Zuordnung bezieht sich auf genannte Seniorenwohnheime, nicht auf medizinische Behandlung oder Wirksamkeit.

## Offene Entscheidungsfragen

* Regionale Verfügbarkeit, Produktionsende und Supportstatus getrennt prüfen.
* Aktuellen SDK Zugang, Marketplace und Abos versionsbezogen prüfen.
* Technische Tabelle des Originalhandbuchs direkt nachprüfen.

## Pflege

Fakten ausschließlich in `fakten.yaml` pflegen. Der lesbare Steckbrief steht in der erzeugten [README.md](README.md).
