---
schema_version: '1.0'
id: agility_robotics_digit_generation_4
name: Digit Generation 4
aliases: []
entity_type: modell
manufacturer_id: agility_robotics
developer_ids: []
form: zweibeinig
classification:
  value: gegenwaertig
  reason: Kundenbericht bestätigt bestehenden kommerziellen Betrieb und weitere Digit 4 Einsätze ab 2027.
    Kein frei bestellbarer Standardtarif.
  source_ids:
  - src_digit4_gxo_update_2026
  assessed_at: '2026-10-30'
tags:
- axis: branche
  id: logistik
  basis: dokumentierter_einsatz
  source_ids:
  - src_digit4_gxo_update_2026
- axis: aufgabe
  id: transport
  basis: dokumentierter_einsatz
  source_ids:
  - src_digit4_gxo_update_2026
- axis: aufgabe
  id: manipulation
  basis: dokumentierter_einsatz
  source_ids:
  - src_digit4_gxo_update_2026
- axis: umgebung
  id: innen
  basis: dokumentierter_einsatz
  source_ids:
  - src_digit4_gxo_update_2026
relations:
- type: nachfolger
  target_id: agility_digit5
scope: Digit 4 im kommerziellen GXO Prozess. Zahlen des Piloten 2023 sind als damalige Konfiguration markiert.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
  next_review: '2026-11-29'
  priority: normal
  status: teilweise_geprueft
official_link:
  url: https://www.agilityrobotics.com/solutions
  kind: produkt
  source_id: src_digit4_gxo_update_2026
  verification: geprueft
screening:
  section: aktuell
  access: projektzugang
  reason: Kundenbericht bestätigt bestehenden kommerziellen Betrieb und weitere Digit 4 Einsätze ab 2027.
    Kein frei bestellbarer Standardtarif.
  source_ids:
  - src_digit4_gxo_update_2026
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Digit Generation 4

## Einordnung

Digit 4 besitzt einen dokumentierten kommerziellen Logistikeinsatz. Das ist ein belastbarerer Prozessbeleg als eine reine Vorführung, gilt aber für den konkret integrierten Behältertransfer.

## Integration und eigene Entwicklung

Das belegte Geschäftsmodell ist ein kundenspezifischer RaaS Vertrag mit Agility Arc und Integration vorhandener Automatisierung. Ein öffentlicher Basistarif, frei verfügbare eigene Policies und allgemeiner SDK Zugriff sind damit nicht bestätigt. Integrationsprojekt und Herstellerbetreuung einplanen.

## Einsatzgrenzen und Beleglage

Körpermaße und Last stammen hier aus der datierten Pilotkonfiguration. Spätere Hardwareänderungen sind nicht numerisch dokumentiert. Keine Übertragung der Digit 5 Nutzlast oder Sicherheitsauslegung. Treppen, Geröll und Staub sind keine bestätigten Grenzen dieses Produktionsprozesses.

## Dokumentationsstand

Kundenfoto, technische Pilotquelle und Herstellerdatenblattzugang verlinkt. Ein frei zugängliches, eindeutig versioniertes aktuelles Digit 4 PDF wurde nicht gefunden.

## Offene Entscheidungsfragen

* Welche aktuelle Digit 4 Konfiguration wird neuen Kunden angeboten?
* Wie sehen RaaS Tarif, Laufzeit, Service und Ausstieg aus?
* Welche Durchsatzwerte und Interventionen erreicht der eigene Prozess?
* Welche Daten werden über Arc verarbeitet und welche Schnittstellen bleiben lokal?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
