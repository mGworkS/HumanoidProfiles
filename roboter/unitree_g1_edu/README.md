<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->

# G1 EDU

Kompakte zweibeinige Plattform. Die EDU Edition ist für eigene Entwicklung vorgesehen.

![Offizielle G1 Plattformabbildung; gezeigte Hände und Zubehör sind keine Zusage für die Basisversion.](https://www.unitree.com/images/4e6266ec20b849af968750d5d432d391_1372x798.jpg)

Bildquelle: [Unitree](../../quellen/src_g1_specs_20261030.md). Rechte beim jeweiligen Rechteinhaber. Nur externer Originalverweis; keine Kopie im Repository und keine freie Nachnutzungslizenz behauptet.

## Steckbrief

[Legende zu Merkmalen, Einheiten und Nachweisen](../../docs/legende.md)

| Merkmal | Angabe | Nachweisstand |
| --- | --- | --- |
| Hersteller | [Unitree Robotics](../../hersteller/unitree/README.md) | Organisationsprofil |
| Offizielle Website | [https://www.unitree.com/g1/](https://www.unitree.com/g1/) | geprüft |
| Vorstellung und weitere Videos | [G1 Herstellerclip aus der offiziellen Produktseite. Plattformdarstellung; Edition, Hände und Softwarestand prüfen.](https://www.unitree.com/images/7504897529034b05890225e149d3af28.mp4)<br>[Weiterer offizieller G1 Produktclip. Gezeigte Funktionen nicht pauschal als Lieferumfang werten.](https://www.unitree.com/images/fadc6f0bc26747d6b4110fd5e5657857.mp4) | Links auf Originale; Vorführung ist kein unabhängiger Test |
| Datenblatt und Dokumentation | [G1 EDU: offizielle technische HTML Tabelle; keine separate allgemeine PDF gefunden.](https://www.unitree.com/g1/)<br>[G1 Benutzerhandbuch und Montageanleitungen im offiziellen Downloadbereich.](https://www.unitree.com/app/g1/)<br>[G1 Fernsteuerungsfunktionen. Genaue Konfiguration und Firmware vor Nutzung bestätigen.](https://oss-global-cdn.unitree.com/static/5014b2b84df94951b1e2197081e02822.pdf) | Versions und Konfigurationshinweise im Linktext beachten |
| Bauform und Entität | zweibeinig; variante | Geltungsbereich unten beachten |
| Einordnung | gegenwaertig | Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. EDU über Vertrieb abzustimmen. |
| Geltungsbereich | G1 EDU. Andere Editionen sind eigene Profile. Technische Tabelle am 30. Oktober 2026. | Daten anderer Generationen werden nicht automatisch übertragen |
| Prüfumfang | teilweise_geprueft | 2026-10-30 |
| Branchen, Aufgaben und Umgebung | Forschung (herstellerziel), Bildung (herstellerziel), Interaktion (herstellerziel), Policy Training (herstellerziel) | Tags sind keine Eignungsfreigabe |
| Modellspezifische Besonderheiten | [Spezialinformationen zu diesem Typ](#modellspezifische-besonderheiten) | Freie Ergänzungen mit Belegbezug |
| Erstvorstellung | Unbekannt (Separates Datum der EDU Ausführung nicht bestätigt; Grundmodell separat erfasst.) | [unbekannt / keine](#lifecycle-first-presented) |
| Entwicklung | Unbekannt | [unbekannt / keine](#lifecycle-development) |
| Produktion | Unbekannt | [unbekannt / keine](#lifecycle-production) |
| Support | Hersteller nennt 18 Monate Garantie; kein bestätigtes Supportende (Garantie ist kein allgemeiner Software Supportvertrag; regionale Bedingungen prüfen) | [eingeschraenkt / herstellerangabe](#v20261030-lifecycle-support) |
| Erste bestätigte Auslieferung | Unbekannt | [unbekannt / keine](#lifecycle-first-delivery) |
| Entwicklungsende | Unbekannt | [unbekannt / keine](#lifecycle-development-end) |
| Produktionsende | Unbekannt | [unbekannt / keine](#lifecycle-production-end) |
| Supportende | Unbekannt | [unbekannt / keine](#lifecycle-support-end) |
| Höhe | 1.32 m (aufrecht) | [belegt / herstellerangabe](#v20261030-hardware-height) |
| Breite | 0.45 m | [belegt / herstellerangabe](#v20261030-hardware-width) |
| Tiefe | 0.2 m | [belegt / herstellerangabe](#v20261030-hardware-depth) |
| Eigenmasse | 35 kg (ungefährer Basiswert mit Batterie; EDU Zubehör kann die Masse erhöhen) | [eingeschraenkt / herstellerangabe](#v20261030-hardware-mass) |
| Nutzlast je Arm | 3 kg (ungefährer Maximalwert je Arm; stark von der Armhaltung abhängig; keine bestätigte Dauerlast beim Gehen) | [eingeschraenkt / herstellerangabe](#v20261030-hardware-payload-arm) |
| Nutzlast beidhändig | Unbekannt | [unbekannt / keine](#hardware-payload-two-arms) |
| Nutzlast beim Gehen | Unbekannt | [unbekannt / keine](#hardware-payload-walking) |
| Reichweite | Unbekannt | [unbekannt / keine](#hardware-reach) |
| Geschwindigkeit | Unbekannt | [unbekannt / keine](#hardware-speed) |
| Laufzeit | 120 min (ungefähr zwei Stunden; Testprofil nicht benannt) | [eingeschraenkt / herstellerangabe](#v20261030-hardware-runtime) |
| Batterieenergie | Unbekannt | [unbekannt / keine](#hardware-battery) |
| IP Schutzart | Unbekannt (Keine eindeutige IP Schutzart in der geprüften Konfigurationstabelle) | [unbekannt / keine](#v20261030-environment-ip) |
| Autonomie nach Aufgabe | Unbekannt (Lieferumfang autonomer Aufgaben und Umfang der Vorführsoftware sind nicht präzise zugesichert) | [unbekannt / keine](#v20261030-autonomy-scope) |
| SDK und API | Sekundärentwicklung unterstützt; genaue Schnittstellen und Freischaltung im Angebot prüfen | [belegt / herstellerangabe](#v20261030-openness-sdk) |
| Eigenes Policy Training | Eigenes Training von G1 Bewegungsreglern über RL Gym dokumentiert (Bewegungsregelung; kein allgemeines vortrainiertes Industrieaufgabenmodell) | [eingeschraenkt / herstellerangabe](#v20261030-openness-policy-training) |
| Ausführung eigener Policies | Sim2Real Bereitstellung für passende G1 EDU Konfiguration dokumentiert | [eingeschraenkt / herstellerangabe](#v20261030-openness-policy-deployment) |
| Cloudabhängigkeit | Unbekannt | [unbekannt / keine](#ecosystem-cloud) |
| Aboabhängigkeit | Unbekannt | [unbekannt / keine](#ecosystem-subscription) |
| Ursprungsland der Entwicklung | China (Entwicklungsherkunft laut Katalog; kein Nachweis des Fertigungslands) | [eingeschraenkt / projektkatalog](#identity-origin-country) |
| Freiheitsgrade | 23 (Grundausstattung; zusätzliche Hände und Achsen gesondert) | [belegt / herstellerangabe](#v20261030-hardware-dof) |
| KI und Steuerungsmodelle im Einsatz | Unbekannt | [Rolle, Bezug und Bedingungen](#ki-modelle-und-software) |
| Weitere belegte KI Integrationen | [NVIDIA GR00T N](#ai-gr00t-reference) (eingeschraenkt)<br>[NVIDIA AGILE](#ai-agile-reference) (eingeschraenkt)<br>[NVIDIA GR00T-N1.6-Rheo-PickNPlaceTray Checkpoint laut Quelle](#ai-gr00t16-tray-sim) (eingeschraenkt)<br>[NVIDIA GR00T-N1.6-Rheo-Sim-PushCart Checkpoint laut Quelle](#ai-gr00t16-cart-sim) (eingeschraenkt)<br>[NVIDIA GR00T-N1.5-RL-Rheo-AssembleTrocar Checkpoint laut Quelle](#ai-gr00t15-trocar-sim) (eingeschraenkt)<br>[UnifoLM-VLA-Base](#g1-unifolm-vla) (eingeschraenkt)<br>[UnifoLM-VLM-Base](#g1-unifolm-vlm) (eingeschraenkt) | [Rolle, Bezug und Bedingungen](#ki-modelle-und-software) |

## KI, Modelle und Software

| System | Version | Rolle | Bezug und Grenzen | Nachweis |
| --- | --- | --- | --- | --- |
| NVIDIA GR00T N | nicht benannt | Manipulationsmodell | referenzintegration. G1 mit Dex3 Händen, zusätzlicher RealSense Kamera, freigeschaltetem Entwicklerzugriff und NVIDIA Compute; aufgabenspezifisch feinabgestimmt. Nicht Bestandteil eines jeden EDU Pakets. | [eingeschraenkt](#ai-gr00t-reference) |
| NVIDIA AGILE | nicht benannt | Bewegungsregelung | referenzintegration. Isaac ROS Physical AI Release 4.5 für geeigneten G1 Aufbau; keine generelle Freischaltung jeder Seriennummer. | [eingeschraenkt](#ai-agile-reference) |
| NVIDIA GR00T-N1.6-Rheo-PickNPlaceTray | Checkpoint laut Quelle | Aufgabenpolicy | simulation. Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage. | [eingeschraenkt](#ai-gr00t16-tray-sim) |
| NVIDIA GR00T-N1.6-Rheo-Sim-PushCart | Checkpoint laut Quelle | Aufgabenpolicy | simulation. Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage. | [eingeschraenkt](#ai-gr00t16-cart-sim) |
| NVIDIA GR00T-N1.5-RL-Rheo-AssembleTrocar | Checkpoint laut Quelle | Aufgabenpolicy | simulation. Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage. | [eingeschraenkt](#ai-gr00t15-trocar-sim) |
| UnifoLM-VLA-Base | VLA-0 Framework | Manipulations VLA | herstellerworkflow. G1 Trainingsdaten und reales Deployment dokumentiert. Handkonfiguration, Kameras, Entwicklungsrechte und Client Server Inferenz müssen passen. Kein sofortiger Standardliefer Skill. | [eingeschraenkt](#g1-unifolm-vla) |
| UnifoLM-VLM-Base | Base Checkpoint | Wahrnehmungs und Sprachkomponente | komponente_des_herstellerworkflows. Komponente im dokumentierten UnifoLM Workflow; kein eigenständiger universeller G1 Bewegungsregler. | [eingeschraenkt](#g1-unifolm-vlm) |

Eingebaute Steuerung, Referenzintegration, Simulation und Forschungskooperation sind unterschiedliche Bezüge. Hardware und Softwareversion sowie Lizenz und Kundenrechte gemeinsam prüfen. Eine Plattform wie Isaac GR00T oder ein Rechner wie Jetson Thor belegen keine bestimmte vorinstallierte Modellversion.

## Fähigkeiten und Lieferumfang

| Funktion | Was ist belegt? | Direkt nutzbar oder Zusatzaufwand? | Bedingungen und Nachweis |
| --- | --- | --- | --- |
| Gehen oder rollende Fortbewegung | Regular Mode und Running Mode per Fernsteuerung | Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen | Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen. [eingeschraenkt / herstellerangabe](#cap20261030-mobility-walking) |
| Dynamisches Laufen | Running Mode mit niedriger und hoher Geschwindigkeit | Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen | Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen. [eingeschraenkt / herstellerangabe](#cap20261030-mobility-running) |
| Springen | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Keine belastbare editionsbezogene Lieferfunktion im geprüften Umfang; spektakuläre Vorführungen nicht ungeprüft übernehmen. [unbekannt / keine](#cap20261030-mobility-jumping) |
| Tanzen und Bewegungssequenzen | Dance Mode mit mehreren vorbereiteten Sequenzen | Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen | Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen. [eingeschraenkt / herstellerangabe](#cap20261030-mobility-dancing) |
| Treppen aufwärts | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt [unbekannt / keine](#v20261030-mobility-steps-up) |
| Treppen abwärts | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt [unbekannt / keine](#v20261030-mobility-steps-down) |
| Unebener Boden | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-mobility-uneven-ground) |
| Geröll | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt [unbekannt / keine](#v20261030-mobility-rubble) |
| Bodenhindernisse | Climb Mode in der Fernsteuerungsübersicht dokumentiert; keine bestätigte allgemeine Hindernisgrenze | Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen | Konfiguration und Firmware prüfen; daraus keine Zusage für normale Treppen oder loses Geröll ableiten. [eingeschraenkt / herstellerangabe](#cap-final-mobility-obstacles) |
| Selbstständiges Aufstehen | Lie to Stand und Roll Up als Bedienfunktionen dokumentiert | Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen | Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen. [eingeschraenkt / herstellerangabe](#cap20261030-mobility-self-recovery) |
| Pick and Place | Apfel aufnehmen und auf Teller ablegen im NVIDIA GR00T Referenzworkflow | Eigene Anwendung, Policy oder Integration erforderlich | EDU Entwicklerzugriff, Dex3 Hände, RealSense, NVIDIA Compute und angepasstes Training; kein universeller Liefer Skill. [eingeschraenkt / herstellerangabe](#cap20261030-manipulation-pick-place) |

## Navigation, Flotte und Unternehmens IT

| Funktion | Was ist belegt? | Direkt nutzbar oder Zusatzaufwand? | Bedingungen und Nachweis |
| --- | --- | --- | --- |
| Autonome Navigation | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-navigation-scope) |
| Kartenaufbau und Lokalisierung | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-navigation-mapping) |
| Hindernisvermeidung bei Navigation | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-navigation-obstacle-avoidance) |
| Flottenmanagement | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-fleet-management) |
| ERP Anbindung | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Keine bestätigte direkte ERP Anbindung. WMS, MES, SDK oder eine API sind kein Nachweis eines fertigen ERP Konnektors. [unbekannt / keine](#cap20261030-integration-erp) |
| WMS Anbindung | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-integration-wms) |
| WES Anbindung | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-integration-wes) |
| MES Anbindung | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-integration-mes) |
| Integrationsschnittstellen für Unternehmens IT | Unbekannt | Lieferumfang und mögliche Zusatzkosten unbekannt | Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang. [unbekannt / keine](#cap20261030-integration-api) |

Eine API oder ein SDK ist keine fertige ERP oder WMS Anbindung. Zusatzpakete, Cloud, Lizenzen, Kartenaufbau und Inbetriebnahme werden nur bei passendem Beleg als enthalten behandelt. Nicht erfasst und unbekannt bedeuten keine Verneinung.

## Screening

**Ansicht:** Aktuelle Auswahl. **Zugang:** Kaufanfrage.

Aktuelle Herstellerseite mit eigenständiger Konfigurationsspalte. EDU über Vertrieb abzustimmen.

Einordnung geprüft: 2026-10-30. Grundlage: primaerquelle. [src_g1_specs_20261030](../../quellen/src_g1_specs_20261030.md)


## Beschaffung und Geschäftsmodell

Kein konkretes aktuelles Angebot in diesem Bestand bestätigt. Das ist kein Nachweis der Nichtverfügbarkeit. Preis, Abo, RaaS und Integrationsleistungen bleiben offen.

## Integration und eigene Entwicklung

Eigene Entwicklung benötigt passende Hardware, SDK Version und ein eigenes Testkonzept. G1 RL Gym dokumentiert Bewegungslernen und Sim2Real. Ausgereifte autonome Arbeitsaufgaben und eine komplette Integration sind kein automatischer Bestandteil des Hardwarepreises.

## Einsatzgrenzen und Beleglage

Armnutzlast ist haltungsabhängig. Aus Sensorik und Herstelleraufnahmen folgt keine garantierte Sturzvermeidung. Für Treppen, Geröll, Staub und dynamische Hindernisse fehlen hier konfigurationsbezogene Betriebsgrenzen.

## Dokumentationsstand

Technische HTML Tabelle und offizieller Handbucheinstieg verlinkt. Allgemeine PDF nicht gefunden. Bilder sind externe Herstellerverweise mit Konfigurationshinweis.

## Offene Entscheidungsfragen

* Welche genaue Achsen, Hände und Rechenmodule enthält das Angebot?
* Welche SDK und Policy Funktionen sind auf dieser Seriennummer freigeschaltet?
* Welche Nutzlast, Betriebsdauer und Bodenbedingungen werden im Abnahmetest erreicht?
* Welche regionalen Lieferbedingungen, Lizenzen, Abos und Sicherheitsunterlagen gelten?

## Ereignisse und Termine

Keine zusätzlichen Ereignisse erfasst.

## Modellspezifische Besonderheiten

**Edition entscheidet über Eigenentwicklung:** Gleiche Familienbezeichnung bedeutet keinen gleichen Entwicklerumfang. Basisversion, EDU, Hände und zusätzliche Rechenmodule sind vor der Beschaffung konkret festzulegen. Belege: [v20261030_hardware_end_effectors](#v20261030-hardware-end-effectors), [v20261030_openness_sdk](#v20261030-openness-sdk), [v20261030_openness_policy_training](#v20261030-openness-policy-training).


## Medien und Dokumente

[Alle Bilder und Videos](assets/README.md) · [Datenblätter und Dokumentation](dokumente/README.md). Externe Originale bleiben beim Anbieter.

| Typ | Original und Geltungsbereich | Version | Herkunft und Rechte |
| --- | --- | --- | --- |
| datenblatt | [G1 EDU: offizielle technische HTML Tabelle; keine separate allgemeine PDF gefunden.](https://www.unitree.com/g1/) | Webstand 2026-10-30 | [Unitree](../../quellen/src_g1_specs_20261030.md). Rechte beim jeweiligen Rechteinhaber. Nur externer Originalverweis; keine Kopie im Repository und keine freie Nachnutzungslizenz behauptet. |
| handbuch | [G1 Benutzerhandbuch und Montageanleitungen im offiziellen Downloadbereich.](https://www.unitree.com/app/g1/) | Nicht angegeben | [Unitree](../../quellen/src_g1_downloads_20261030.md). Rechte beim jeweiligen Rechteinhaber. Nur externer Originalverweis; keine Kopie im Repository und keine freie Nachnutzungslizenz behauptet. |
| rendering | [Offizielle G1 Plattformabbildung; gezeigte Hände und Zubehör sind keine Zusage für die Basisversion.](https://www.unitree.com/images/4e6266ec20b849af968750d5d432d391_1372x798.jpg) | Nicht angegeben | [Unitree](../../quellen/src_g1_specs_20261030.md). Rechte beim jeweiligen Rechteinhaber. Nur externer Originalverweis; keine Kopie im Repository und keine freie Nachnutzungslizenz behauptet. |
| video | [G1 Herstellerclip aus der offiziellen Produktseite. Plattformdarstellung; Edition, Hände und Softwarestand prüfen.](https://www.unitree.com/images/7504897529034b05890225e149d3af28.mp4) | Nicht angegeben | [Unitree](../../quellen/src_g1_specs_20261030.md). Rechte beim jeweiligen Rechteinhaber. Externer Originalverweis, keine Kopie und keine freie Nachnutzungslizenz behauptet. |
| video | [Weiterer offizieller G1 Produktclip. Gezeigte Funktionen nicht pauschal als Lieferumfang werten.](https://www.unitree.com/images/fadc6f0bc26747d6b4110fd5e5657857.mp4) | Nicht angegeben | [Unitree](../../quellen/src_g1_specs_20261030.md). Rechte beim jeweiligen Rechteinhaber. Externer Originalverweis, keine Kopie und keine freie Nachnutzungslizenz behauptet. |
| handbuch | [G1 Fernsteuerungsfunktionen. Genaue Konfiguration und Firmware vor Nutzung bestätigen.](https://oss-global-cdn.unitree.com/static/5014b2b84df94951b1e2197081e02822.pdf) | ohne Firmwaredatum; G1 29 DoF Dateititel | [Unitree](../../quellen/src_g1_remote_29dof_20261030.md). Rechte beim jeweiligen Rechteinhaber. Externer Originalverweis; keine Kopie im Repository und keine freie Nachnutzungslizenz behauptet. |


## Belege und Detailangaben

Details sind nach Fachgruppen aufklappbar. Unbekannte Angaben bedeuten keine Verneinung. Fehlende optionale Merkmale sind nicht erfasst.

<details>
<summary>Identität: 1 Angaben und Belege</summary>

### identity origin country

**Ursprungsland der Entwicklung:** China. Status: eingeschraenkt. Evidenz: projektkatalog.

Bedingungen: definition: Entwicklungsherkunft laut Katalog; kein Nachweis des Fertigungslands

* [Projektkatalog 04-Humanoide_Roboter_Katalog_Forschung_und_EDU_2026_10_29_123420_CET.docx](../../quellen/src_catalog_04.md), Fundstelle: Modellkopf: Hersteller und Land. Zugang: lokale_kopie. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Technik: 12 Angaben und Belege</summary>

### v20261030 hardware height

**Höhe:** 1.32 m. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: zustand: aufrecht

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Mechanical Dimensions, jeweilige Konfigurationsspalte. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware width

**Breite:** 0.45 m. Status: belegt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Mechanical Dimensions, Stand. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware depth

**Tiefe:** 0.2 m. Status: belegt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Mechanical Dimensions, Stand. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware mass

**Eigenmasse:** 35 kg. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: konfiguration: ungefährer Basiswert mit Batterie; EDU Zubehör kann die Masse erhöhen

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Weight with battery. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware dof

**Freiheitsgrade:** 23. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: konfiguration: Grundausstattung; zusätzliche Hände und Achsen gesondert

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Total Degrees of Freedom. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware dof max

**Freiheitsgrade maximal nach Ausbau:** 43. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: konfiguration: höchster angegebener Ausbau; konkrete Bestellung prüfen

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Total Degrees of Freedom, EDU. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware payload arm

**Nutzlast je Arm:** 3 kg. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: condition: ungefährer Maximalwert je Arm; stark von der Armhaltung abhängig; keine bestätigte Dauerlast beim Gehen

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Arm Maximum Load und Fußnote. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware runtime

**Laufzeit:** 120 min. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: lastprofil: ungefähr zwei Stunden; Testprofil nicht benannt

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Battery Life. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware battery capacity

**Batteriekapazität:** 9 Ah. Status: belegt. Evidenz: herstellerangabe.

Bedingungen: umrechnung: 9000 mAh entsprechen 9 Ah; kein daraus abgeleiteter Wh Wert

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Smart Battery Quick Release. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware sensors

**Sensorik:** Tiefenkamera, 3D LiDAR und vier Mikrofone. Status: belegt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Sensing Sensors und Wahrnehmungsabschnitt. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware compute

**Rechenhardware:** Achtkern CPU; zusätzliche Rechenmodule nach EDU Konfiguration. Status: belegt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Basic Computing Power und High Computing Power Module. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 hardware end effectors

**Hände und Endeffektoren:** Dexteröse Hände und zusätzliche Handgelenkachsen je EDU Bestellung. Status: eingeschraenkt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Single Hand Degrees of Freedom. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Lebenszyklus: 1 Angaben und Belege</summary>

### v20261030 lifecycle support

**Support:** Hersteller nennt 18 Monate Garantie; kein bestätigtes Supportende. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: grenze: Garantie ist kein allgemeiner Software Supportvertrag; regionale Bedingungen prüfen

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Warranty Period. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Offenheit: 8 Angaben und Belege</summary>

### v20261030 openness sdk

**SDK und API:** Sekundärentwicklung unterstützt; genaue Schnittstellen und Freischaltung im Angebot prüfen. Status: belegt. Evidenz: herstellerangabe.

* [Unitree G1 und G1 EDU: technische Vergleichstabelle](../../quellen/src_g1_specs_20261030.md), Fundstelle: Secondary Development, EDU. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness low level

**Steuerungszugriff:** SDK2 enthält G1 Steuerungsbeispiele; Zugriff nur mit passender EDU Hardware und Firmware. Status: eingeschraenkt. Evidenz: herstellerangabe.

* [Unitree SDK2](../../quellen/src_unitree_sdk2_20261030.md), Fundstelle: README und example/g1. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness source code

**Quellcode:** SDK2 und RL Gym sind öffentlich; dies umfasst nicht die gesamte Firmware. Status: eingeschraenkt. Evidenz: herstellerangabe.

* [Unitree SDK2](../../quellen/src_unitree_sdk2_20261030.md), Fundstelle: README und LICENSE. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness training code

**Trainingscode:** G1 RL Trainingsablauf im offiziellen RL Gym Repository. Status: belegt. Evidenz: herstellerangabe.

* [Unitree RL Gym: G1 Training und Sim2Real](../../quellen/src_unitree_rl_20261030.md), Fundstelle: README: Training, Play, Deployment. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness policy training

**Eigenes Policy Training:** Eigenes Training von G1 Bewegungsreglern über RL Gym dokumentiert. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: umfang: Bewegungsregelung; kein allgemeines vortrainiertes Industrieaufgabenmodell

* [Unitree RL Gym: G1 Training und Sim2Real](../../quellen/src_unitree_rl_20261030.md), Fundstelle: G1 Training und Sim2Real. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness policy deployment

**Ausführung eigener Policies:** Sim2Real Bereitstellung für passende G1 EDU Konfiguration dokumentiert. Status: eingeschraenkt. Evidenz: herstellerangabe.

* [Unitree RL Gym: G1 Training und Sim2Real](../../quellen/src_unitree_rl_20261030.md), Fundstelle: Deployment. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness simulation

**Simulation:** Trainingssimulation und Bereitstellungsschritte im RL Gym Repository. Status: belegt. Evidenz: herstellerangabe.

* [Unitree RL Gym: G1 Training und Sim2Real](../../quellen/src_unitree_rl_20261030.md), Fundstelle: README. Zugang: direkt. Aussage geprüft: 2026-10-30.

### v20261030 openness commercial rights

**Kommerzielle Nutzungsrechte:** BSD 3 Clause für die genannten öffentlichen Repositories; weitere Komponenten separat prüfen. Status: eingeschraenkt. Evidenz: herstellerangabe.

* [Unitree SDK2](../../quellen/src_unitree_sdk2_20261030.md), Fundstelle: LICENSE. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>KI und Software: 8 Angaben und Belege</summary>

### ai gr00t reference

**Weitere belegte KI Integrationen:** NVIDIA GR00T N. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: NVIDIA GR00T N; version: nicht benannt; rolle: Manipulationsmodell; bezug: referenzintegration; grenze: G1 mit Dex3 Händen, zusätzlicher RealSense Kamera, freigeschaltetem Entwicklerzugriff und NVIDIA Compute; aufgabenspezifisch feinabgestimmt. Nicht Bestandteil eines jeden EDU Pakets.

* [NVIDIA GR00T Referenzworkflow für G1](../../quellen/src_g1_gr00t_workflow_20261030.md), Fundstelle: Requirements und Workflow. Zugang: direkt. Aussage geprüft: 2026-10-30.

### ai agile reference

**Weitere belegte KI Integrationen:** NVIDIA AGILE. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: NVIDIA AGILE; version: nicht benannt; rolle: Bewegungsregelung; bezug: referenzintegration; grenze: Isaac ROS Physical AI Release 4.5 für geeigneten G1 Aufbau; keine generelle Freischaltung jeder Seriennummer.

* [Isaac ROS Physical AI und AGILE für G1](../../quellen/src_g1_agile_20261030.md), Fundstelle: Supported Unitree G1 features. Zugang: direkt. Aussage geprüft: 2026-10-30.

### ai gr00t16 tray sim

**Weitere belegte KI Integrationen:** NVIDIA GR00T-N1.6-Rheo-PickNPlaceTray Checkpoint laut Quelle. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: NVIDIA GR00T-N1.6-Rheo-PickNPlaceTray; version: Checkpoint laut Quelle; rolle: Aufgabenpolicy; bezug: simulation; grenze: Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage.

* [NVIDIA G1 Simulationsworkflows mit GR00T](../../quellen/src_g1_gr00t_sim_20261030.md), Fundstelle: Supported Environments, Robots, and Models. Zugang: direkt. Aussage geprüft: 2026-10-30.

### ai gr00t16 cart sim

**Weitere belegte KI Integrationen:** NVIDIA GR00T-N1.6-Rheo-Sim-PushCart Checkpoint laut Quelle. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: NVIDIA GR00T-N1.6-Rheo-Sim-PushCart; version: Checkpoint laut Quelle; rolle: Aufgabenpolicy; bezug: simulation; grenze: Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage.

* [NVIDIA G1 Simulationsworkflows mit GR00T](../../quellen/src_g1_gr00t_sim_20261030.md), Fundstelle: Supported Environments, Robots, and Models. Zugang: direkt. Aussage geprüft: 2026-10-30.

### ai gr00t15 trocar sim

**Weitere belegte KI Integrationen:** NVIDIA GR00T-N1.5-RL-Rheo-AssembleTrocar Checkpoint laut Quelle. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: NVIDIA GR00T-N1.5-RL-Rheo-AssembleTrocar; version: Checkpoint laut Quelle; rolle: Aufgabenpolicy; bezug: simulation; grenze: Offizieller G1 Simulationsworkflow; kein bestätigter Einsatz auf physischem Seriengerät und keine medizinische Eignungszusage.

* [NVIDIA G1 Simulationsworkflows mit GR00T](../../quellen/src_g1_gr00t_sim_20261030.md), Fundstelle: Supported Environments, Robots, and Models. Zugang: direkt. Aussage geprüft: 2026-10-30.

### software frameworks g1

**Trainings und Simulationswerkzeuge:** Unitree RL Gym; NVIDIA Isaac ROS Physical AI; Isaac Lab und MuJoCo je Workflow. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: grenze: Werkzeuge sind keine vorinstallierten universellen Aufgabenmodelle

* [Isaac ROS Physical AI und AGILE für G1](../../quellen/src_g1_agile_20261030.md), Fundstelle: Simulation und Real Hardware. Zugang: direkt. Aussage geprüft: 2026-10-30.

### g1 unifolm vla

**Weitere belegte KI Integrationen:** UnifoLM-VLA-Base. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: UnifoLM-VLA-Base; version: VLA-0 Framework; rolle: Manipulations VLA; bezug: herstellerworkflow; grenze: G1 Trainingsdaten und reales Deployment dokumentiert. Handkonfiguration, Kameras, Entwicklungsrechte und Client Server Inferenz müssen passen. Kein sofortiger Standardliefer Skill.

* [UnifoLM VLA: Herstellerworkflow für G1](../../quellen/src_g1_unifolm_vla_20261030.md), Fundstelle: Model Checkpoints, G1 Datasets und Real World Inference. Zugang: direkt. Aussage geprüft: 2026-10-30.

### g1 unifolm vlm

**Weitere belegte KI Integrationen:** UnifoLM-VLM-Base. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: system: UnifoLM-VLM-Base; version: Base Checkpoint; rolle: Wahrnehmungs und Sprachkomponente; bezug: komponente_des_herstellerworkflows; grenze: Komponente im dokumentierten UnifoLM Workflow; kein eigenständiger universeller G1 Bewegungsregler.

* [UnifoLM VLA: Herstellerworkflow für G1](../../quellen/src_g1_unifolm_vla_20261030.md), Fundstelle: Model Checkpoints und vlm_pretrained_path. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Mobilität: 5 Angaben und Belege</summary>

### cap20261030 mobility walking

**Gehen oder rollende Fortbewegung:** Regular Mode und Running Mode per Fernsteuerung. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: konfigurationsabhaengig; bedingung: Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen.

* [G1 Fernsteuerung: dokumentierte Firmwarefunktionen](../../quellen/src_g1_remote_29dof_20261030.md), Fundstelle: Seite 2: Motion Control Switching. Zugang: direkt. Aussage geprüft: 2026-10-30.

### cap20261030 mobility running

**Dynamisches Laufen:** Running Mode mit niedriger und hoher Geschwindigkeit. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: konfigurationsabhaengig; bedingung: Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen.

* [G1 Fernsteuerung: dokumentierte Firmwarefunktionen](../../quellen/src_g1_remote_29dof_20261030.md), Fundstelle: Seite 2: Motion Control Switching. Zugang: direkt. Aussage geprüft: 2026-10-30.

### cap20261030 mobility dancing

**Tanzen und Bewegungssequenzen:** Dance Mode mit mehreren vorbereiteten Sequenzen. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: konfigurationsabhaengig; bedingung: Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen.

* [G1 Fernsteuerung: dokumentierte Firmwarefunktionen](../../quellen/src_g1_remote_29dof_20261030.md), Fundstelle: Seite 2: Motion Control Switching. Zugang: direkt. Aussage geprüft: 2026-10-30.

### cap20261030 mobility self recovery

**Selbstständiges Aufstehen:** Lie to Stand und Roll Up als Bedienfunktionen dokumentiert. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: konfigurationsabhaengig; bedingung: Dokumentierte G1 Konfiguration; Firmwareversion, 29 DoF Bezug und Serienfreigabe vor Kauf abgleichen.

* [G1 Fernsteuerung: dokumentierte Firmwarefunktionen](../../quellen/src_g1_remote_29dof_20261030.md), Fundstelle: Seite 2: Motion Control Switching. Zugang: direkt. Aussage geprüft: 2026-10-30.

### cap final mobility obstacles

**Bodenhindernisse:** Climb Mode in der Fernsteuerungsübersicht dokumentiert; keine bestätigte allgemeine Hindernisgrenze. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: konfigurationsabhaengig; bedingung: Konfiguration und Firmware prüfen; daraus keine Zusage für normale Treppen oder loses Geröll ableiten.

* [G1 Fernsteuerung: dokumentierte Firmwarefunktionen](../../quellen/src_g1_remote_29dof_20261030.md), Fundstelle: Seite 2: Climb Mode. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Fähigkeiten: 1 Angaben und Belege</summary>

### cap20261030 manipulation pick place

**Pick and Place:** Apfel aufnehmen und auf Teller ablegen im NVIDIA GR00T Referenzworkflow. Status: eingeschraenkt. Evidenz: herstellerangabe.

Bedingungen: bereitstellung: eigene_entwicklung; bedingung: EDU Entwicklerzugriff, Dex3 Hände, RealSense, NVIDIA Compute und angepasstes Training; kein universeller Liefer Skill.

* [NVIDIA GR00T Referenzworkflow für G1](../../quellen/src_g1_gr00t_workflow_20261030.md), Fundstelle: Apple to plate und Requirements. Zugang: direkt. Aussage geprüft: 2026-10-30.


</details>

<details>
<summary>Offene und nicht veröffentlichte Angaben (31)</summary>

### lifecycle first presented

**Erstvorstellung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: scope: Separates Datum der EDU Ausführung nicht bestätigt; Grundmodell separat erfasst.


### lifecycle development

**Entwicklung:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle production

**Produktion:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle first delivery

**Erste bestätigte Auslieferung:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle development end

**Entwicklungsende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle production end

**Produktionsende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### lifecycle support end

**Supportende:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware payload two arms

**Nutzlast beidhändig:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware payload walking

**Nutzlast beim Gehen:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware reach

**Reichweite:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware speed

**Geschwindigkeit:** Unbekannt. Status: unbekannt. Evidenz: keine.


### hardware battery

**Batterieenergie:** Unbekannt. Status: unbekannt. Evidenz: keine.


### ecosystem cloud

**Cloudabhängigkeit:** Unbekannt. Status: unbekannt. Evidenz: keine.


### ecosystem subscription

**Aboabhängigkeit:** Unbekannt. Status: unbekannt. Evidenz: keine.


### v20261030 environment ip

**IP Schutzart:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Keine eindeutige IP Schutzart in der geprüften Konfigurationstabelle


### v20261030 autonomy scope

**Autonomie nach Aufgabe:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Lieferumfang autonomer Aufgaben und Umfang der Vorführsoftware sind nicht präzise zugesichert


### v20261030 mobility steps up

**Treppen aufwärts:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt; bereitstellung: unbekannt


### v20261030 mobility steps down

**Treppen abwärts:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt; bereitstellung: unbekannt


### v20261030 mobility rubble

**Geröll:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Für diese bestellbare Konfiguration kein belastbares Grenzprofil mit Last, Boden und Softwarestand festgestellt; bereitstellung: unbekannt


### unknown software ai stack

**KI und Steuerungsmodelle im Einsatz:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: offen: Kein belastbarer modellspezifischer Name oder weiterer Integrationsnachweis im geprüften Umfang. Unbekannt bedeutet keine Inkompatibilität.


### cap20261030 mobility jumping

**Springen:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Keine belastbare editionsbezogene Lieferfunktion im geprüften Umfang; spektakuläre Vorführungen nicht ungeprüft übernehmen.


### cap20261030 mobility uneven ground

**Unebener Boden:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 navigation scope

**Autonome Navigation:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 navigation mapping

**Kartenaufbau und Lokalisierung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 navigation obstacle avoidance

**Hindernisvermeidung bei Navigation:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 fleet management

**Flottenmanagement:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 integration erp

**ERP Anbindung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Keine bestätigte direkte ERP Anbindung. WMS, MES, SDK oder eine API sind kein Nachweis eines fertigen ERP Konnektors.


### cap20261030 integration wms

**WMS Anbindung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 integration wes

**WES Anbindung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 integration mes

**MES Anbindung:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.


### cap20261030 integration api

**Integrationsschnittstellen für Unternehmens IT:** Unbekannt. Status: unbekannt. Evidenz: keine.

Bedingungen: bereitstellung: unbekannt; bedingung: Kein modellspezifischer Nachweis oder konkretes Lieferpaket im geprüften Umfang.



</details>
