# Pflegeprozess

## Neues Modell

1. Hersteller, Aliasnamen, Varianten und bestehende IDs prüfen.
2. Bei unklarer Identität zunächst Recherchekandidat anlegen.
3. Herstellerprofil und Quellen anlegen oder wiederverwenden.
4. Mit `python scripts/new_robot.py --id beispiel_01 --name "Beispiel 01" --manufacturer hersteller_id --source src_id` ein Profil erzeugen.
5. Einordnung begründen und Quellenverweise ergänzen. Pflichtfelder dürfen unbekannt bleiben.
6. Nur belegte Fähigkeiten ergänzen. Individuelle Merkmale zuerst registrieren.
7. `python scripts/kb.py validate`, `python scripts/kb.py build`, `python -m unittest discover -s tests -v`, `python scripts/kb.py export` ausführen.
8. Änderungen und Quellen prüfen, dann committen. Größere Änderungen über einen Branch und Pull Request prüfen.

## Schnelle Aktualisierung

Gezielter Lauf: nur fällige Modelle, offene Liefertermine und beobachtete Herstellerseiten. Vorherige Quellen und Fragen wiederverwenden. Geänderte Dokumentversionen prüfen. Neue Nachrichten liefern Kandidaten, nicht automatisch bestätigte Fakten.

Breiter Lauf: ergänzend neue Hersteller, neue Modelle und bisher schwach erfasste Branchen, Regionen und Sprachen suchen. Bekannte Namen und Aliase gegen den Bestand abgleichen. Suchstrategie und Abdeckung protokollieren.

Jeder Lauf nennt Datum, Suchumfang, Suchbegriffe, geprüfte Quellen, neue Funde, Änderungen, offene Punkte und erfolglose Prüfungen. Letzter Suchversuch und letzte sachliche Verifikation bleiben getrennt.

## Pipeline

Angekündigte Modelle sind normale Profile mit Einordnung pipeline. Noch unklare Funde stehen in recherche/kandidaten. Verstrichene Termine lösen eine Prüfung aus, ändern aber keinen Status. Eine spätere Quelle bestätigt die Umsetzung oder dokumentiert die Verschiebung.

## Versionierung

Git dokumentiert Änderungen an der Wissensbasis. Ereignisse dokumentieren die Geschichte des Roboters. CHANGELOG.md erklärt wesentliche Änderungen. Schemaänderungen benötigen eine explizite Migration; bloß neue Tags oder Merkmale nicht.

## Automatisierung

GitHub Actions prüft Daten, Tests und reproduzierbare Ansichten bei Push und Pull Request. Die Webrecherche ist nicht zeitgesteuert eingerichtet. Quellenmonitoring beschreibt geplante Prüfintervalle, keinen laufenden Dienst.
