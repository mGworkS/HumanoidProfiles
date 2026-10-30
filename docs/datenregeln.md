# Datenregeln

## Umfang und Identität

Betrachtungszeitraum ab 2016: vorgestellt, angeboten, eingesetzt oder weiterentwickelt. Ältere Systeme dürfen aufgenommen werden, wenn ein Bezug zum Zeitraum belegt ist. Historische Ergänzungen sind ausdrücklich zulässig. Keine Branchenliste ist abschließend.

Modell, Variante, Familie und Entwicklungsprogramm werden getrennt gezählt. Aliasnamen erzeugen keinen neuen Roboter. Eine neue Softwareversion erzeugt normalerweise kein neues Modell. Wesentlich andere Hardware kann eine eigene Variante rechtfertigen. Beziehungen dürfen nur auf erfasste IDs zeigen; noch offene Verwandte stehen in der Kandidatenliste.

## Aussagen und Quellen

Jede bekannte technische Aussage hat Wert, Einheit, Merkmalschlüssel, Evidenzart, Quelle, Fundstelle und Prüfdatum. Herstellerangabe bedeutet dokumentierte Aussage des Herstellers, nicht unabhängige Verifikation. Eine Suchindexquelle wird ausdrücklich als solche markiert. Direkter Abruf oder Originaldokument soll nachgeholt werden.

Unbekannt: nicht ausreichend belegt. Nicht veröffentlicht: Quelle bestätigt fehlende öffentliche Angabe. Nicht anwendbar: sachlich nicht passend; Begründung im Kontext. Fehlende optionale Aussage bedeutet nicht erfasst. Null ist niemals null Kilogramm oder falsch.

Wertebereiche haben zwei Zahlen in der registrierten Einheit. Bedingungen müssen Last, Tätigkeit, Konfiguration, Steuerung und Softwarestand enthalten, soweit relevant. Alternative Werte bleiben getrennte Aussagen. Konflikte nicht durch Mittelwert oder willkürliche Auswahl verdecken. Ersetzte Aussagen bleiben über supersedes nachvollziehbar und verlassen den aktuellen Export.

## Lebenszyklus

Historische Relevanz ist eine redaktionelle Einordnung mit Begründung. Entwicklung, Produktion, Verkauf, Support und konkrete Nutzung sind eigene Tatsachen. Ein nie vermarkteter Prototyp kann historisch sein. Eine ältere Plattform kann weiter genutzt werden. Fehlende Nachrichten belegen keine Einstellung.

Vorstellung, angekündigte Lieferung und bestätigte Lieferung sind unterschiedliche Ereignisse. Teilgenaue Daten bleiben Jahr, Monat oder Halbjahr; keine erfundenen Tagesdaten. Ein Vorführungsschluss eines Museums ist kein Produktionsende.

## Zugang und Geschäftsmodell

Mehrere Angebote pro Modell sind erlaubt. Anbieter, Region, Zielkunden, Konfiguration, Kauf/Miete/RaaS, Preisbasis, Abo und Vertragsgrenzen getrennt erfassen. Ein Kontaktformular ist kein bestätigtes Kaufangebot. Eine aktuelle Webseite ist kein Liefernachweis. Leere Angebotsliste bedeutet kein bestätigtes Angebot im Bestand.

Der konservative Beschaffungsfilter akzeptiert nur bestätigte Kauf-, Miet-, Leasing- oder RaaS Angebote innerhalb von 90 Tagen mit passender Region und Zielgruppe. Das Zeitfenster ist eine Repository Regel, kein Branchenstandard. Regionencodes werden exakt verglichen; EU umfasst in diesem Prototyp nicht automatisch einzelne Ländercodes. Forschungskooperationen und Pilotprojekte benötigen eine eigene Suchabsicht.

## Offenheit und Integration

SDK, API, Quellcode, Gewichte, Trainingsdaten, Trainingscode, Policy Training, Ausführung eigener Policies, Low Level Zugriff, Firmware, Hardwareunterlagen, Administratorrechte und kommerzielle Rechte sind getrennte Merkmale. Öffentlicher Quellcode belegt nicht uneingeschränktes kommerzielles Nutzungsrecht.

Cloudabhängigkeit, eigenes App Deployment, Marketplace, Integratoren und Betrieb ohne Abo gesondert prüfen. Unterschiedliche Entwicklereditionen gehören in den Geltungsbereich der Aussage.

Fähigkeit und Lieferumfang sind unabhängig. context.bereitstellung beschreibt, ob eine Funktion enthalten, konfigurationsabhängig, ein Zusatzpaket, ein Integrationsprojekt, eigene Entwicklung, eine Demo, angekündigt oder unbekannt ist. Nur ein passender Produkt oder Kundenbeleg darf enthalten bestätigen. Ein SDK, ein Video oder ein Simulationsmodell reicht dafür nicht aus. Navigation, Flottenmanagement und ERP, WMS, WES sowie MES Integration getrennt behandeln.

## Freie Ergänzungen

Ein neuer Merkmalschlüssel wird in schema/merkmale.yaml mit lesbarem Namen, Gruppe, Datentyp und Einheit ergänzt. Erweiterungstexte in extensions erklären individuelle Besonderheiten und verweisen auf konkrete Aussage IDs. Freitext darf keine unbemerkte zweite Datenquelle für Zahlen oder Lieferstatus werden.

Branche, Aufgabe und Umgebung haben getrennte Tags. Neue Tags sind willkommen, aber erst Synonyme und bestehende Begriffe prüfen. Jede Zuordnung nennt ihre Basis und Quelle. Ein Herstellerziel ist kein dokumentierter Kundeneinsatz.

## Medien

Metadaten für Fotos, Renderings, Videos, Logos und PDFs enthalten Quelle, Modellbezug, Rechte, Version, Sprache und gegebenenfalls lokalen Pfad sowie SHA256. Rechte unbekannt: nur verlinken. Große Binärdateien erst nach bewusster Entscheidung über Git LFS oder externe Ablage aufnehmen.

## Übernommene Recherchebestände

access_method bestandsverweis kennzeichnet einen gespeicherten Quellenlink, der beim Import nicht erneut geöffnet wurde. accessed_at ist hier das Datum der Sichtung des Bestandsverweises. Das ist keine Bestätigung der aktuellen Webseite. Profile mit maintenance.status erfasst können reviewed_at und last_search als null führen. Identität, Bauform und redaktionelle Tags stammen aus dem Bestand und sind noch zu prüfen. Importnotizen sind keine belegten technischen Aussagen.

Herstellerzuordnung kann bei Forschungsprojekten eine beteiligte Organisation oder Gruppe bezeichnen. Eine noch ungeklärte Website bleibt null. Familien und Entwicklungsprogramme werden in Zählungen separat ausgewiesen.

## Screening vor Vollständigkeit

Für die Standardansicht gelten docs/screening.md und schema/screening_policy.yaml. Historische Systeme bleiben außerhalb der aktuellen Tabelle, selbst wenn eine Gebrauchtbeschaffung denkbar ist. Forschungsprototypen ohne bestätigten externen Zugang erscheinen separat. Kaufbare Forschungsplattformen bleiben in der aktuellen Auswahl. Ungeklärte Aktualität wird nicht stillschweigend als vorgestellt gewertet.

Projektkatalogdaten werden mit evidence projektkatalog und eingeschränktem Belegstatus gespeichert. Sie sind keine unabhängigen Tests und keine erneute aktuelle Herstellerbestätigung. Maße und Nutzlasttexte mit uneindeutigem Lastbezug bleiben beschreibend.
