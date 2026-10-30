# RAG und strukturierte Auswahl

## Zwei unterschiedliche Aufgaben

Vollständige Aufzählungen, Zahlenfilter und Beschaffungslisten benötigen strukturierte Abfragen über export/robots.json. Semantische Suche über export/chunks.jsonl liefert Erklärungen und Belege innerhalb der geeigneten Modellmenge. Ein Top K Ergebnis ist niemals eine vollständige Liste aller Modelle.

## Metadaten und Belege

Jeder Abschnitt enthält eine stabile chunk_id, Modell ID, Geltungsbereich, Einordnung, Tags, Commit und Originalpfad. Fakten enthalten zusätzlich Status, Evidenzart, Bedingungen und Quellenfundstellen. Redaktionelle Abschnitte sind als editorial markiert und nicht als technische Nachweise zu verwenden.

Der Import muss die Metadaten tatsächlich als Filterfelder ablegen. YAML oder Markdown allein erzeugen noch kein zuverlässiges RAG Verhalten. Herstellerbehauptungen dürfen im Antworttext nicht als unabhängig getestet erscheinen. Historische Daten und Zukunftsankündigungen behalten ihren Zeitbezug.

## Auswahl

Vor der Retrievalsuche die Absicht bestimmen: aktuelle Beschaffung, Pilotzugang, technische Forschung, Pipeline oder historische Übersicht. Historische Einordnung allein ist kein Ausschluss bei Beschaffung; maßgeblich ist ein bestätigtes passendes Angebot. Unbekannte Fähigkeiten werden nicht als erfüllt gewertet. Eine weiche Vorauswahl darf offene Kandidaten getrennt zeigen.

Der mitgelieferte Query Befehl demonstriert konservative Beschaffungsfilter. Ein aufgabenspezifisches Ranking und die fachliche Einsatzbewertung sind noch nicht implementiert. Eine Anwendung soll Anforderungen mit Modell IDs und genauem Wissensbasis Commit verbinden.

## Aktualisierung des Index

Export überschreibt die abgeleiteten Dateien vollständig. manifest.json enthält alle aktuellen IDs und Inhaltshashes. Beim Import neue und geänderte Abschnitte aktualisieren und nicht mehr vorhandene IDs entfernen. Modelländerungen dürfen keine alten widersprüchlichen Abschnitte im Index zurücklassen. Gespeicherte Embeddings gehören nicht in die Originalprofile.

## Qualitätsprüfung

Tests prüfen Filter, unbekannte Werte, Quellenreferenzen und Löschung aus dem Export. evaluation/fragen.jsonl ist zusätzlich für die spätere Antwortprüfung des tatsächlichen RAG Systems vorgesehen. Diese Fragen sind noch kein ausgeführter LLM Benchmark.

## Gemeinsame Screeningregeln

Exportabschnitte enthalten screening_section, screening und official_link. Die Hauptansicht und query --mode screening verwenden dieselbe Auswahlfunktion. Ein RAG Import muss dieses Feld als echten Filter übernehmen. reference bleibt für vollständige historische und wissenschaftliche Recherche verfügbar. procurement verlangt weiterhin konkrete bestätigte Angebote mit passender Region und Zielgruppe; die bloße Aufnahme in die Screeningübersicht erfüllt diese strengere Bedingung nicht.
