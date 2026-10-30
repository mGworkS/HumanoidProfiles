---
schema_version: '1.0'
id: neura_robotics_r_4ne1_gen_4
name: 4NE1 Gen 4
aliases: []
entity_type: modell
manufacturer_id: neura_robotics
developer_ids: []
form: zweibeinig
classification:
  value: pipeline
  reason: Gen4 im TUM RoboGym vorgestellt und betrieben; Serienfertigung wird vorbereitet. Allgemeine
    Kundenauslieferung nicht bestätigt.
  source_ids:
  - src_neura_gen4_launch_20261030
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: industrie
  basis: herstellerziel
  source_ids:
  - src_neura_4ne1_page_20261030
- axis: branche
  id: logistik
  basis: herstellerziel
  source_ids:
  - src_neura_4ne1_page_20261030
- axis: branche
  id: haushalt
  basis: herstellerziel
  source_ids:
  - src_neura_4ne1_page_20261030
- axis: branche
  id: forschung
  basis: dokumentierter_einsatz
  source_ids:
  - src_neura_gen4_launch_20261030
- axis: aufgabe
  id: manipulation
  basis: herstellerziel
  source_ids:
  - src_neura_4ne1_page_20261030
relations: []
scope: 4NE1 Gen 4 vom Oktober 2026; generische 4NE1 Angaben und Gen3.5 ausdrücklich ausgeschlossen.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://neura-robotics.com/products/4ne1/
  kind: produkt
  source_id: src_neura_gen4_launch_20261030
  verification: geprueft
screening:
  section: aktuell
  access: vorgestellt
  reason: Gen4 im TUM RoboGym vorgestellt und betrieben; Serienfertigung wird vorbereitet. Allgemeine
    Kundenauslieferung nicht bestätigt.
  source_ids:
  - src_neura_gen4_launch_20261030
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# 4NE1 Gen 4

## Einordnung

Neue 4NE1 Generation mit textiler Hülle und NEURON AI. Der Hersteller nennt eine relative Gewichtsreduktion. Daraus wird hier keine absolute Masse berechnet.

## Integration und eigene Entwicklung

Zugang zu NEURA Gym, Integration und Training mit dem Hersteller abklären. Lokale KI Ausführung bedeutet weder offene Modellgewichte noch freie Policy Entwicklung. Neuraverse Werkzeuge für kundenspezifisches NEURON Fine Tuning sind beschrieben. Gen4 spezifische Freischaltung, SDK und Vertragsrechte bleiben zu prüfen.

## Einsatzgrenzen und Beleglage

Die allgemeine Produktseite und das verlinkte Datenblatt haben einen uneindeutigen Generationsbezug. Deshalb bleiben Gen4 Maße, Nutzlast, Laufzeit und Schutzart offen. Branchenziele sind keine bestätigten Einsatzfreigaben.

## Dokumentationsstand

Vorstellungsfoto und Gen4 Produktinformation vorhanden. Das zusätzlich verlinkte V7 PDF wird ausdrücklich als ungeeignet für die Übernahme von Gen4 Kennwerten markiert.

## Offene Entscheidungsfragen

* Wann stehen ein ausdrücklich auf Gen4 bezogenes Datenblatt und Sicherheitsunterlagen bereit?
* Welche Kunden können Geräte erhalten und zu welchem Geschäftsmodell?
* Welche Aufgaben, Geländearten und Eingriffsquoten sind beim Kunden nachgewiesen?
* Welche eigenen Modelle, Policies und Integrationsschnittstellen sind vertraglich erlaubt?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
