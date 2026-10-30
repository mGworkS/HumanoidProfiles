<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->

# Einordnung und Tags

[Katalog](../KATALOG.md) · [Herstellerübersicht](../HERSTELLER.md)

Einordnung ist genau ein Status pro Profil. Tags sind unabhängige Mehrfachzuordnungen nach Branche, Aufgabe und Umgebung. Beide sagen allein nichts über Kaufbarkeit oder Eignung für einen konkreten Einsatz aus.

## Einordnung

| Status im Steckbrief | Bedeutung |
| --- | --- |
| Aktuelles Modell | Aktuell geführte Plattform. Kaufbarkeit, Produktion, Liefertermin und Einsatzreife werden separat belegt. |
| Angekündigtes Modell | Vorgestellte oder reservierbare Entwicklung mit noch nicht ausreichend bestätigter regulärer Bereitstellung. |
| Frühere Generation | Durch eine neuere Generation abgelöste Ausführung. Nutzung, Verkauf und Support können weiterbestehen. |
| Historisch bedeutsam | Für die Entwicklung humanoider Robotik wichtige ältere Plattform. Kein pauschaler Nachweis einer Einstellung. |
| Historische Entwicklungsplattform | Früherer Prototyp oder Forschungsträger. Eine damalige Serienproduktion oder Vermarktung wird nicht vorausgesetzt. |
| Historisches Produkt | Historisch eingeordnetes Produkt beziehungsweise frühere Einsatzflotte. Produktionsende, Support und mögliche Restangebote separat prüfen. |
| Noch zu prüfen | Aktueller Lebenszyklus oder passende Einordnung noch nicht ausreichend geklärt. |

<details>
<summary>Stabile Codes für Datenpflege und RAG</summary>

| Anzeigename | Code |
| --- | --- |
| Aktuelles Modell | `gegenwaertig` |
| Angekündigtes Modell | `pipeline` |
| Frühere Generation | `fruehere_generation` |
| Historisch bedeutsam | `historisch_relevant` |
| Historische Entwicklungsplattform | `historischer_entwicklungstraeger` |
| Historisches Produkt | `historisches_produkt` |
| Noch zu prüfen | `ungeklaert` |

</details>

## Tags

Ein Profil darf mehrere Tags derselben Gruppe besitzen. Die Liste ist erweiterbar. Vor neuen Tags vorhandene Begriffe und Synonyme prüfen. Zählungen umfassen alle erfassten Profile einschließlich Varianten, Historie und ungeprüfter Zuordnungen.

## Branchen

| Verfügbarer Tag | Erfasste Profile |
| --- | --- |
| [Industrie](../katalog/branche_industrie.md) | 29 |
| [Logistik](../katalog/branche_logistik.md) | 16 |
| [Gesundheit und Pflege](../katalog/branche_gesundheit_pflege.md) | 7 |
| [Einzelhandel](../katalog/branche_einzelhandel.md) | 1 |
| [Bildung](../katalog/branche_bildung.md) | 17 |
| [Forschung](../katalog/branche_forschung.md) | 80 |
| [Unterhaltung](../katalog/branche_unterhaltung.md) | 9 |
| [Service](../katalog/branche_service.md) | 26 |
| [Landwirtschaft](../katalog/branche_landwirtschaft.md) | 0 |
| [Bau und Bauwirtschaft](../katalog/branche_bau.md) | 1 |
| [Haushalt](../katalog/branche_haushalt.md) | 7 |
| [Sicherheit und Rettung](../katalog/branche_sicherheit_rettung.md) | 7 |
| [Raumfahrt](../katalog/branche_raumfahrt.md) | 2 |

## Aufgaben

| Verfügbarer Tag | Erfasste Profile |
| --- | --- |
| [Transport](../katalog/aufgabe_transport.md) | 3 |
| [Interaktion](../katalog/aufgabe_interaktion.md) | 9 |
| [Manipulation](../katalog/aufgabe_manipulation.md) | 9 |
| [Policy Training](../katalog/aufgabe_policy_training.md) | 3 |
| [Inspektion](../katalog/aufgabe_inspektion.md) | 1 |

## Umgebungen

| Verfügbarer Tag | Erfasste Profile |
| --- | --- |
| [Innenraum](../katalog/umgebung_innen.md) | 3 |
| [Außenbereich](../katalog/umgebung_aussen.md) | 1 |
| [Umgebung mit Besuchern oder Kunden](../katalog/umgebung_publikum.md) | 1 |

## Grundlage einer Zuordnung

| Angabe im Steckbrief | Bedeutung |
| --- | --- |
| Herstellerziel | Vom Anbieter vorgesehener Bereich oder Einsatz. |
| Dokumentierter Einsatz | Ein Einsatz im genannten Bereich ist mit Quelle erfasst. |
| Dokumentierte Funktion | Eine technische Funktion begründet die Zuordnung. |
| Redaktionelle Zuordnung | Fachliche Einordnung des Datenbestands; kein unabhängiger Einsatzbeleg. |

Eine Healthcare Zuordnung bestätigt keine medizinische Wirksamkeit. Ein Umgebungstag für Besucher oder Kunden ist kein Sicherheitsnachweis.
