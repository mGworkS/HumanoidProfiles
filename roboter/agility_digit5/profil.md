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
  reason: In Entwicklung. Früher Kundenzugang für erstes Halbjahr 2027, allgemeine Verfügbarkeit bis Ende
    2027 erwartet.
  source_ids:
  - src_digit5_product
  assessed_at: '2026-10-30'
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
relations:
- type: vorgaenger
  target_id: agility_robotics_digit_generation_4
scope: Digit 5, angekündigte nächste Generation; sämtliche Leistungswerte vorläufig.
maintenance:
  last_search: '2026-10-30'
  reviewed_at: '2026-10-30'
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
  reason: In Entwicklung. Früher Kundenzugang für erstes Halbjahr 2027, allgemeine Verfügbarkeit bis Ende
    2027 erwartet.
  source_ids:
  - src_digit5_product
  checked_at: '2026-10-30'
  basis: primaerquelle
---

# Digit 5

## Einordnung

Digit 5 ist die angekündigte nächste industrielle Generation. Bestehende Digit 4 Kundenerfahrung wird nicht als bereits erreichte Digit 5 Leistung ausgewiesen.

## Integration und eigene Entwicklung

Agility Arc, wechselbare Greifer und Schnittstellen zu Lager und Produktionssystemen sind vorgesehen. Beschaffung, RaaS, Integrationskosten und Eigenentwicklung benötigen eine konkrete Anbietervereinbarung. Keine offenen Gewichte oder frei trainierbaren Kunden Policies bestätigt.

## Einsatzgrenzen und Beleglage

Leistungswerte stammen aus Vorserie und Planung. Ein Arbeitstag mit Ladeunterbrechungen ist keine ununterbrochene Batterielaufzeit. Ein geplantes Sicherheitskonzept ersetzt keinen Nachweis für den späteren Einsatz.

## Dokumentationsstand

Produktbild und technische HTML Angaben verfügbar. Product Sheet führt zu einer Formularseite. Ein direktes öffentliches PDF wurde nicht gefunden und kein Formular übermittelt.

## Offene Entscheidungsfragen

* Wer erhält 2027 tatsächlich Zugang und in welcher Region?
* Welche finalen Daten, Zertifikate und Abnahmebedingungen gelten?
* Welche Preise und RaaS Modelle gelten für neue Kunden?
* Welcher SDK, Daten und Policy Zugriff ist vertraglich vorgesehen?

## Pflege

Stand 30. Oktober 2026. Fachlich im genannten Umfang geprüft. Offene Felder bleiben unbekannt. Fakten und Medien werden aus `fakten.yaml` erzeugt.
