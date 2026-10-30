# Gesicherte Arbeitsunterbrechung

Der Nutzer hat die Bearbeitung am 30. Oktober 2026 gestoppt. main ist unverändert. Dieser Branch dient ausschließlich der dauerhaften Sicherung.

[Fortsetzungsnotiz](ARBEITSSTAND.md) · [Abrufindex](quellenabrufe.json) · [Vollständiger Git Zwischenstand](HumanoidProfiles_checkpoint.bundle)

Das Git Bundle enthält den lokalen Commit 5d87a8cf02650e231bd5b156cc8c8e395c0cf6c4 mit allen 313 geänderten beziehungsweise neuen Dateien. Es benötigt den bereits auf main vorhandenen Ausgangscommit 7d98f5186eb9011874abf9e88e9884eab0b07581. SHA256: f137506f72f2748e205b5881001c752db2dc63744f7fdfd031d84a9d02d670b3.

Der normale Git Push stand ohne Zugangsdaten nicht zur Verfügung. Deshalb wurde dieses wiederherstellbare Git Bundle über die verbundene GitHub Schnittstelle gesichert. Die eingebetteten Quelldateien und generierten Ansichten sind im Bundle enthalten; die Arbeitskopie dieses Sicherungsbranches selbst zeigt weiterhin die Ausgangsdateien.

Nach neuer Nutzeranweisung: Bundle herunterladen, SHA256 vergleichen, im Repository prüfen und den enthaltenen Branch laden:

```sh
git bundle verify HumanoidProfiles_checkpoint.bundle
git fetch HumanoidProfiles_checkpoint.bundle refs/heads/work/profile-expansion-checkpoint-20261030
git switch -c fortsetzung-profile FETCH_HEAD
```

Dann zuerst ARBEITSSTAND.md lesen. Keine automatische Weiterarbeit. Vor einer Veröffentlichung auf main sind die abschließenden Prüfungen erforderlich.
