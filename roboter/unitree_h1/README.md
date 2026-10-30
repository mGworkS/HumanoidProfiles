<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->

# H1

[Katalog](../../KATALOG.md) · [Herstellerübersicht](../../HERSTELLER.md) · [Einordnung und alle Tags](../../docs/einordnung_und_tags.md)

Humanoide Entwicklungsplattform mit dokumentiertem Workflow für eigene Bewegungssteuerung. Industrielle Einsatzreife ist aufgabenbezogen zu prüfen.

## Steckbrief

[Legende zu Merkmalen, Einheiten und Nachweisen](../../docs/legende.md)

| Merkmal | Angabe | Nachweisstand |
| --- | --- | --- |
| Hersteller | [Unitree Robotics](../../hersteller/unitree/README.md) | Organisationsprofil |
| Offizielle Website | [https://www.unitree.com/h1/](https://www.unitree.com/h1/) | geprüft |
| Vorstellung und weitere Videos | Noch kein geprüfter Link erfasst | Links auf Originale; Vorführung ist kein unabhängiger Test |
| Datenblatt und Dokumentation | Noch kein geprüfter Link erfasst | Versions und Konfigurationshinweise im Linktext beachten |
| Bauform und Entität | zweibeinig; modell | Geltungsbereich unten beachten |
| Einordnung | [Aktuelles Modell](../../docs/einordnung_und_tags.md#einordnung) | Produktseite und offizieller Entwicklungsworkflow verfügbar; Produktionsstatus separat ungeklärt. |
| Geltungsbereich | H1 Originalmodell. H1-2 ist eine andere Ausführung; deren Nutzlast und Freiheitsgrade gelten hier nicht. | Daten anderer Generationen werden nicht automatisch übertragen |
| Prüfumfang | teilweise_geprueft | 2026-10-29 |
| Branchen | [Forschung](../../katalog/branche_forschung.md) (Redaktionelle Zuordnung) | [Alle verfügbaren Tags](../../docs/einordnung_und_tags.md#branchen); keine Eignungsfreigabe |
| Aufgaben | [Policy Training](../../katalog/aufgabe_policy_training.md) (Dokumentierte Funktion) | [Alle verfügbaren Tags](../../docs/einordnung_und_tags.md#aufgaben); keine Eignungsfreigabe |
| Umgebungen | Noch nicht zugeordnet | [Alle verfügbaren Tags](../../docs/einordnung_und_tags.md#umgebungen); keine Eignungsfreigabe |
| Modellspezifische Besonderheiten | [Spezialinformationen zu diesem Typ](#modellspezifische-besonderheiten) | Freie Ergänzungen mit Belegbezug |
| Erstvorstellung | 2023-08-15 | [belegt / herstellerangabe](#lifecycle-first-presented) |
| Entwicklung | Unbekannt | [unbekannt / keine](#lifecycle-development) |
| Produktion | Unbekannt | [unbekannt / keine](#lifecycle-production) |
| Support | Unbekannt | [unbekannt / keine](#lifecycle-support) |
| Erste bestätigte Auslieferung | Unbekannt | [unbekannt / keine](#lifecycle-first-delivery) |
| Entwicklungsende | Unbekannt | [unbekannt / keine](#lifecycle-development-end) |
| Produktionsende | Unbekannt | [unbekannt / keine](#lifecycle-production-end) |
| Supportende | Unbekannt | [unbekannt / keine](#lifecycle-support-end) |
| Höhe | 1.8 m (ungefähr) | [belegt / herstellerangabe](#hardware-height) |
| Breite | 0.57 m | [belegt / herstellerangabe](#hardware-width) |
| Tiefe | 0.22 m | [belegt / herstellerangabe](#hardware-depth) |
| Eigenmasse | 47 kg (ungefähr; Batteriebezug nicht ausdrücklich angegeben) | [belegt / herstellerangabe](#hardware-mass) |
| Nutzlast je Arm | Unbekannt | [unbekannt / keine](#hardware-payload-arm) |
| Nutzlast beidhändig | Unbekannt | [unbekannt / keine](#hardware-payload-two-arms) |
| Nutzlast beim Gehen | Unbekannt | [unbekannt / keine](#hardware-payload-walking) |
| Reichweite | Unbekannt | [unbekannt / keine](#hardware-reach) |
| Geschwindigkeit | 3.3 m/s (Kein Nachweis einer Dauerarbeitsgeschwindigkeit) | [belegt / herstellerangabe](#hardware-speed) |
| Laufzeit | Unbekannt | [unbekannt / keine](#hardware-runtime) |
| Batterieenergie | 864 Wh | [belegt / herstellerangabe](#hardware-battery) |
| IP Schutzart | Unbekannt | [unbekannt / keine](#environment-ip) |
| Autonomie nach Aufgabe | Unbekannt | [unbekannt / keine](#autonomy-scope) |
| SDK und API | Unbekannt | [unbekannt / keine](#openness-sdk) |
| Eigenes Policy Training | Training für H1 dokumentiert | [belegt / herstellerangabe](#openness-policy-training) |
| Ausführung eigener Policies | Physischer Deploymentpfad für H1 dokumentiert (Passende Konfiguration und Debugmodus; keine allgemeine Sicherheitsfreigabe) | [belegt / herstellerangabe](#openness-policy-deployment) |
| Cloudabhängigkeit | Unbekannt | [unbekannt / keine](#ecosystem-cloud) |
| Aboabhängigkeit | Unbekannt | [unbekannt / keine](#ecosystem-subscription) |
| Ursprungsland der Entwicklung | China (Entwicklungsherkunft laut Katalog; kein Nachweis des Fertigungslands) | [eingeschraenkt / projektkatalog](#identity-origin-country) |
| Höhe mit Konfigurationsbezug | Ca. 1,80 m (H1; Katalogangabe; Revision und Ausstattung beachten) | [eingeschraenkt / projektkatalog](#hardware-height-description) |
| Nutzlast mit Lastbezug | Nominelle Armnutzlast nicht veröffentlicht (H1; Keine Umrechnung zwischen Armnutzlast, Heben und Tragen) | [eingeschraenkt / projektkatalog](#hardware-payload-description) |
| KI und Steuerungsmodelle im Einsatz | Nicht erfasst | [Rolle, Bezug und Bedingungen](#ki-modelle-und-software) |
| Weitere belegte KI Integrationen | Nicht erfasst | [Rolle, Bezug und Bedingungen](#ki-modelle-und-software) |

## KI, Modelle und Software

Noch keine belegten modellspezifischen KI Systeme erfasst. Das bedeutet keine grundsätzliche Inkompatibilität.

Eingebaute Steuerung, Referenzintegration, Simulation und Forschungskooperation sind unterschiedliche Bezüge. Hardware und Softwareversion sowie Lizenz und Kundenrechte gemeinsam prüfen. Eine Plattform wie Isaac GR00T oder ein Rechner wie Jetson Thor belegen keine bestimmte vorinstallierte Modellversion.

## Fähigkeiten und Lieferumfang

| Funktion | Was ist belegt? | Direkt nutzbar oder Zusatzaufwand? | Bedingungen und Nachweis |
| --- | --- | --- | --- |
| Gehen oder rollende Fortbewegung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Dynamisches Laufen | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Springen | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Tanzen und Bewegungssequenzen | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Treppen aufwärts | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Treppen abwärts | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Unebener Boden | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Geröll | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Bodenhindernisse | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Selbstständiges Aufstehen | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Pick and Place | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |

## Navigation, Flotte und Unternehmens IT

| Funktion | Was ist belegt? | Direkt nutzbar oder Zusatzaufwand? | Bedingungen und Nachweis |
| --- | --- | --- | --- |
| Autonome Navigation | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Kartenaufbau und Lokalisierung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Hindernisvermeidung bei Navigation | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Flottenmanagement | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| ERP Anbindung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| WMS Anbindung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| WES Anbindung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| MES Anbindung | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |
| Integrationsschnittstellen für Unternehmens IT | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |

Eine API oder ein SDK ist keine fertige ERP oder WMS Anbindung. Zusatzpakete, Cloud, Lizenzen, Kartenaufbau und Inbetriebnahme werden nur bei passendem Beleg als enthalten behandelt. Nicht erfasst und unbekannt bedeuten keine Verneinung.

## Screening

**Ansicht:** Aktuelle Auswahl. **Zugang:** Kaufanfrage.

H1 wird im Herstellershop geführt; Preis und Lieferkonfiguration auf Anfrage.

Einordnung geprüft: 2026-10-30. Grundlage: primaerquelle. [src_h1_shop](../../quellen/src_h1_shop.md)


## Beschaffung und Geschäftsmodell

Kein konkretes aktuelles Angebot in diesem Bestand bestätigt. Das ist kein Nachweis der Nichtverfügbarkeit. Preis, Abo, RaaS und Integrationsleistungen bleiben offen.

## Offene Entscheidungsfragen

* Aktuelle H1 Beschaffung einschließlich Konfiguration und Region bestätigen.
* Nutzlast, IP Schutz und Laufzeit für konkrete Aufgaben fehlen.
* Lizenzen aller Trainingsabhängigkeiten und kommerzielle Rechte gesondert prüfen.

## Ereignisse und Termine

Keine zusätzlichen Ereignisse erfasst.

## Modellspezifische Besonderheiten

Noch keine zusätzlichen Spezialinformationen erfasst. Dieses Feld nimmt Besonderheiten auf, die sich durch die gemeinsamen Merkmale und Tags nicht ausreichend beschreiben lassen.

## Medien und Dokumente

[Alle Bilder und Videos](assets/README.md) · [Datenblätter und Dokumentation](dokumente/README.md). Externe Originale bleiben beim Anbieter.


## Belege und Detailangaben

Details sind nach Fachgruppen aufklappbar. Unbekannte Angaben bedeuten keine Verneinung. Fehlende optionale Merkmale sind nicht erfasst.

<details>
<summary>Lebenszyklus: 1 Angaben und Belege</summary>

### lifecycle first presented

**Erstvorstellung:** 2023-08-15. Status: belegt. Evidenz: herstellerangabe.

* [Unternehmensgeschichte](../../quellen/src_h1_launch.md), Fundstelle: Unternehmensgeschichte 2023. Zugang: suchindex. Aussage geprüft: 2026-10-29.


</details>

<details>
<summary>Technik: 8 Angaben und Belege</summary>

### hardware height

**Höhe:** 1.8 m. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: precision: ungefähr

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Body Size. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware width

**Breite:** 0.57 m. Status: belegt. Evidenz: herstellerangabe.

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Key Dimensions. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware depth

**Tiefe:** 0.22 m. Status: belegt. Evidenz: herstellerangabe.

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Key Dimensions. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware mass

**Eigenmasse:** 47 kg. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: precision: ungefähr; configuration: Batteriebezug nicht ausdrücklich angegeben

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Total Weight. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware speed

**Geschwindigkeit:** 3.3 m/s. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: limit: Kein Nachweis einer Dauerarbeitsgeschwindigkeit

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Mobility. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware battery

**Batterieenergie:** 864 Wh. Status: belegt. Evidenz: herstellerangabe.

* [H1 und H1-2 Spezifikationen](../../quellen/src_h1_product.md), Fundstelle: H1 Battery. Zugang: direkt. Aussage geprüft: 2026-10-29.

### hardware height description

**Höhe mit Konfigurationsbezug:** Ca. 1,80 m. Status: eingeschraenkt. Evidenz: projektkatalog.

Bedingungen: scope: H1; note: Katalogangabe; Revision und Ausstattung beachten

* [Projektkatalog 04-Humanoide_Roboter_Katalog_Forschung_und_EDU_2026_10_29_123420_CET.docx](../../quellen/src_catalog_04.md), Fundstelle: Technik: Körper und Achsen. Zugang: lokale_kopie. Aussage geprüft: 2026-10-30.

### hardware payload description

**Nutzlast mit Lastbezug:** Nominelle Armnutzlast nicht veröffentlicht. Status: eingeschraenkt. Evidenz: projektkatalog.

Bedingungen: scope: H1; note: Keine Umrechnung zwischen Armnutzlast, Heben und Tragen

* [Projektkatalog 04-Humanoide_Roboter_Katalog_Forschung_und_EDU_2026_10_29_123420_CET.docx](../../quellen/src_catalog_04.md), Fundstelle: Technik: Nutzlast. Zugang: lokale_kopie. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Offenheit: 4 Angaben und Belege</summary>

### openness policy training

**Eigenes Policy Training:** Training für H1 dokumentiert. Status: belegt. Evidenz: herstellerangabe.

* [Unitree RL GYM](../../quellen/src_h1_rl.md), Fundstelle: Training --task h1. Zugang: direkt. Aussage geprüft: 2026-10-29.

### openness policy deployment

**Ausführung eigener Policies:** Physischer Deploymentpfad für H1 dokumentiert. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: requirement: Passende Konfiguration und Debugmodus; keine allgemeine Sicherheitsfreigabe

* [Unitree RL GYM](../../quellen/src_h1_rl.md), Fundstelle: Sim2Real; h1.yaml. Zugang: direkt. Aussage geprüft: 2026-10-29.

### openness training code

**Trainingscode:** Öffentliches Unitree RL GYM Repository. Status: belegt. Evidenz: herstellerangabe.

* [Unitree RL GYM](../../quellen/src_h1_rl.md), Fundstelle: README und Repository. Zugang: direkt. Aussage geprüft: 2026-10-29.

### openness simulation

**Simulation:** Trainingssimulation und Übertragung zwischen Simulatoren dokumentiert. Status: belegt. Evidenz: herstellerangabe.

* [Unitree RL GYM](../../quellen/src_h1_rl.md), Fundstelle: Train / Sim2Sim. Zugang: direkt. Aussage geprüft: 2026-10-29.


</details>

<details>
<summary>Identität: 1 Angaben und Belege</summary>

### identity origin country

**Ursprungsland der Entwicklung:** China. Status: eingeschraenkt. Evidenz: projektkatalog.

Bedingungen: definition: Entwicklungsherkunft laut Katalog; kein Nachweis des Fertigungslands

* [Projektkatalog 04-Humanoide_Roboter_Katalog_Forschung_und_EDU_2026_10_29_123420_CET.docx](../../quellen/src_catalog_04.md), Fundstelle: Modellkopf: Hersteller und Land. Zugang: lokale_kopie. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Offene und nicht veröffentlichte Angaben (17)</summary>

### lifecycle development

**Entwicklung:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle production

**Produktion:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle support

**Support:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle first delivery

**Erste bestätigte Auslieferung:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle development end

**Entwicklungsende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle production end

**Produktionsende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle support end

**Supportende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware payload arm

**Nutzlast je Arm:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware payload two arms

**Nutzlast beidhändig:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware payload walking

**Nutzlast beim Gehen:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware reach

**Reichweite:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware runtime

**Laufzeit:** Unbekannt. Status: unbekannt. Evidenz: keine.


### environment ip

**IP Schutzart:** Unbekannt. Status: unbekannt. Evidenz: keine.


### autonomy scope

**Autonomie nach Aufgabe:** Unbekannt. Status: unbekannt. Evidenz: keine.


### openness sdk

**SDK und API:** Unbekannt. Status: unbekannt. Evidenz: keine.


### ecosystem cloud

**Cloudabhängigkeit:** Unbekannt. Status: unbekannt. Evidenz: keine.


### ecosystem subscription

**Aboabhängigkeit:** Unbekannt. Status: unbekannt. Evidenz: keine.



</details>
