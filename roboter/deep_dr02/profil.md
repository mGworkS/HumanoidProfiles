---
schema_version: '1.0'
id: deep_dr02
name: DR02
aliases: []
entity_type: modell
manufacturer_id: deep_robotics
developer_ids:
- deep_robotics
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Hersteller meldet kommerzielle Einsätze 2026.
  source_ids:
  - src_dr02_commercial
  assessed_at: '2026-10-29'
tags:
- axis: branche
  id: industrie
  basis: herstellerziel
  source_ids:
  - src_dr02_launch
- axis: aufgabe
  id: inspektion
  basis: herstellerziel
  source_ids:
  - src_dr02_launch
- axis: umgebung
  id: aussen
  basis: herstellerziel
  source_ids:
  - src_dr02_product
relations: []
scope: DR02 Grundmodell. Angaben zu DR02 Pro nicht übernehmen.
maintenance:
  last_search: '2026-10-29'
  reviewed_at: '2026-10-29'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://en.deeprobotics.cn/en/index/dr02.html
  kind: produkt
  source_id: src_dr02_commercial
  verification: aus_bestand
screening:
  section: aktuell
  access: vorgestellt
  reason: Kommerzielle Einsätze laut Hersteller gemeldet; konkreter Beschaffungsweg
    weiterhin zu klären.
  source_ids:
  - src_dr02_commercial
  checked_at: '2026-10-29'
  basis: primaerquelle
---

# DR02

## Einordnung

Industrielle humanoide Plattform mit Herstellerangaben zum Ganzkörperschutz. Keine allgemeine Einsatzfreigabe aus der Produktbeschreibung ableiten.

## Offene Entscheidungsfragen

* Größe, Masse und Nutzlast aus einem direkt zugänglichen Originaldatenblatt verifizieren.
* Konkretes Kaufangebot, Region, Lieferzeit und Vertragsmodell prüfen.
* Autonomie, Policy Zugriff und App Ökosystem prüfen.
* Staubschutzangabe ist kein unabhängiger Testbericht.

## Pflege

Fakten ausschließlich in `fakten.yaml` pflegen. Der lesbare Steckbrief steht in der erzeugten [README.md](README.md).
