---
schema_version: '1.0'
id: boston_dynamics_atlas
name: Atlas · Produktversion 2026
aliases:
- Atlas
- Atlas elektrisch
entity_type: modell
manufacturer_id: boston_dynamics
developer_ids: []
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Produktversion vorgestellt; Partnerkontingente 2026, weitere Kunden für 2027 angekündigt. Allgemeine
    sofortige Bestellbarkeit nicht bestätigt.
  source_ids:
  - src_atlas_sheet_20261015
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: industrie
  basis: herstellerziel
  source_ids:
  - src_atlas_sheet_20261015
- axis: branche
  id: logistik
  basis: herstellerziel
  source_ids:
  - src_atlas_sheet_20261015
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_atlas_sheet_20261015
- axis: aufgabe
  id: transport
  basis: herstellerziel
  source_ids:
  - src_atlas_sheet_20261015
- axis: umgebung
  id: innen
  basis: herstellerziel
  source_ids:
  - src_atlas_sheet_20261015
relations: []
scope: Elektrische Atlas Produktversion 2026, Datenblattrevision 15. Oktober 2026. Hydraulischer Atlas
  und elektrischer Prototyp 2024 ausgeschlossen.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://bostondynamics.com/products/atlas/
  kind: produkt
  source_id: src_atlas_sheet_20261015
  verification: geprueft
screening:
  section: aktuell
  access: projektzugang
  reason: Produktversion vorgestellt; Partnerkontingente 2026, weitere Kunden für 2027 angekündigt. Allgemeine
    sofortige Bestellbarkeit nicht bestätigt.
  source_ids:
  - src_atlas_2026_launch
  - src_atlas_sheet_20261015
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Atlas · Produktversion 2026

## Einordnung

Elektrische industrielle Produktversion von Atlas. Das Datenblatt unterscheidet Dauerlast, Kurzzeitlast und einhändiges Heben. Die Betriebsarten umfassen Autonomie und menschliche Fernsteuerung.

## Integration und eigene Entwicklung

Orbit verbindet Flotte und Unternehmenssysteme. Neue Aufgaben und Integration mit Boston Dynamics abstimmen. Modularität und zertifizierte Kundenreparatur sind dokumentiert. Ein freier Kunden SDK, offene Modellgewichte oder uneingeschränkte eigene Policy Entwicklung sind damit nicht bestätigt.

## Einsatzgrenzen und Beleglage

IP67 und Temperaturgrenzen sind Herstellerangaben zur Produktversion. Sie belegen keine vollständige Eignung für beliebige Außenflächen oder Geröll. Dauerlast und Spitzenlast dürfen nicht addiert werden. Laufzeit sinkt bei schwerem Heben; Batteriewechsel ist vom Laden einer Batterie zu unterscheiden.

## Dokumentationsstand

Originaldatenblatt mit visuell geprüfter Revision, Produktbild und Herstellerseite verlinkt. Daten gelten ausdrücklich für die elektrische Produktversion 2026.

## Offene Entscheidungsfragen

* Welche Lieferkontingente, Preise und Regionen gelten für neue Kunden?
* Welche Lasten und Aufgaben werden vertraglich abgenommen?
* Welche SDK, Policy und Reparaturrechte erhält der Betreiber?
* Welche Schutz und Sicherheitsunterlagen sowie Orbit Verträge sind für den konkreten Prozess nötig?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
