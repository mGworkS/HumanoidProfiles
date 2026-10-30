# Übersicht zur Vorauswahl

Die Haupttabelle in katalog/aktuelle_auswahl.md enthält aktuell angebotene, vorbestellbare oder als kommerzielle Entwicklung vorgestellte Systeme. Ein allgemein zugänglicher Produktkatalog und eine konkrete Lieferzusage sind unterschiedliche Nachweise. Der Zugang steht deshalb ausdrücklich in der Tabelle.

## Getrennte Ansichten

* Aktuelle Auswahl: Kaufangebot, Vorbestellung, Kaufanfrage, Projektzugang oder aktuelle kommerzielle Vorstellung mit datierter Quelle.
* Historie: frühere beziehungsweise ausgemusterte Systeme und historisch eingeordnete Plattformen. Diese erscheinen auch dann nicht im Screening, wenn es etwa ein Gebrauchtangebot gäbe.
* Forschung: Forschungsprototypen, deren externer Zugang nicht bestätigt ist. Eine aktuelle frei zugängliche Entwicklungsplattform mit Kaufangebot darf dagegen in die Haupttabelle.
* Ungeklärt: Aktualität oder Zugang noch nicht ausreichend geklärt. Keine automatische Aufnahme allein aus einer alten Modellnennung.

Die Erstvorstellung ist kein Ablaufdatum. Ein 2016 vorgestellter Roboter mit aktuellem Angebot bleibt relevant. Umgekehrt macht die heutige Sichtung eines alten Artikels dessen Inhalt nicht aktuell.

## Quellen und Aktualität

screening hält Abschnitt, Zugangsart, Begründung, Quellen, Datum und Grundlage fest. Projektkatalogangaben sind als K markiert. Herstellerangaben tragen H. Katalogeinordnung ist kein erneut bestätigtes Herstellerangebot.

schema/screening_policy.yaml bestimmt das maximale Alter der Screeningprüfung, derzeit 180 Tage. Das ist eine Pflegeentscheidung und kein Standard der Robotikbranche. Ein veralteter oder unbelegter aktueller Eintrag fällt bei der nächsten Berechnung in die offene Prüfung. Historische Einordnung und bestätigtes Entwicklungsende haben Vorrang.

Die eingecheckten Markdown Ansichten verwenden snapshot_date aus derselben Datei und bleiben dadurch reproduzierbar. Bei jeder fachlichen Aktualisierung dieses Datum mit aktualisieren und build ausführen. Query und Export verwenden das tatsächliche Datum beziehungsweise --as-of. Ein alter Tabellenstand ist im Seitenkopf sichtbar.

## Spalten

Hersteller und Ursprungsland, Erstvorstellung und Verkaufsstart, Zugang mit Quellenstand, Höhe und Payload mit Lastbezug. Das Herkunftsland beschreibt die Entwicklungsherkunft und ist kein Fertigungsnachweis. Familien sind ausdrücklich als solche beschriftet. Ungeprüfte Maße aus einem Projektkatalog sind gekennzeichnet. Fehlende Daten bleiben als nicht erfasst sichtbar.

Nutzlast je Arm, beidhändige Nutzlast, Tragen beim Gehen, Spitzenlast und demonstrierte Einzellast werden nicht gleichgesetzt. Ein Zahlenwert ohne klaren Lastbezug bleibt als beschreibende Angabe mit Einschränkung stehen. Geplante Werte tragen den Zusatz angekündigt.

## Kategorien

Branchen, Aufgaben und Umgebungen bleiben getrennte Achsen. Derselbe Roboter darf in mehreren Ansichten verlinkt werden. Jede registrierte Branche erhält eine sichtbare Seite, auch ohne bestätigten aktuellen Treffer. Die Baukategorie enthält deshalb getrennt das Forschungsbeispiel HRP-5P, ohne daraus einen kaufbaren Baustellenroboter zu machen.

Umgebung mit Besuchern oder Kunden ist ein Umgebungstag für Empfang, Laden oder Museum. Er ist keine Branche, kein Nachweis medizinischer Eignung und keine Sicherheitsfreigabe für den Betrieb neben Personen.

## Offizieller Link

official_link enthält URL, Quellentyp, Quellen ID und Prüfstand. Aus dem Bestand übernommene Herstellerlinks werden als noch nicht erneut geprüft angezeigt. Händlerseiten und allgemeine Verzeichnisse werden nicht automatisch zu offiziellen Modellseiten erklärt. Wenn eine offizielle Modellseite ungeklärt ist, bleibt der bestehende Quellenhinweis direkt erreichbar.
