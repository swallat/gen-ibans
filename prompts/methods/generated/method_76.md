# Implementierung Bundesbank Prüfziffermethode: 76

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 76") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5 ff.
Die einzelnen Stellen der für die Berechnung der Prüfziffer
relevanten 5-, 6- oder 7-stelligen Stammnummer sind von
rechts nach links mit den Ziffern 2, 3, 4, 5 ff. zu multiplizieren.
Die jeweiligen Produkte werden addiert. Die Summe ist durch
11 zu dividieren. Der verbleibende Rest ist die Prüfziffer. Ist
der Rest 10, kann die Kontonummer nicht geprüft werden.
Zusammensetzung der Kontonummer:
S = Stammnummer (5-, 6- oder 7-stellig; die letzte Stelle
dieser Nummer ist die Prüfziffer, sie wird jedoch nicht
in die Prüfzifferberechnung einbezogen)
A = Kontoart (1-stellig)*) werden nicht in die
P = Prüfziffer Prüfzifferberech-
U = Unterkontonummer (2-stellig) nung einbezogen
*) Die Kontoart kann den Wert 0, 4, 6, 7, 8 oder 9 haben.
Darstellung der Kontonummer:
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
5stell. Stammnr.: A 0 0 S S S S P U U
6stell. Stammnr.: A 0 S S S S S P U U
7stell. Stammnr.: A S S S S S S P U U
Beispiel:
Prüfzifferberechnung für eine 6-stellige Kontonummer,
Kontoart ist "0".
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 0 0 1 2 3 4 5 6 0 0
Gewichtung: 6 5 4 3 2
6 + 10 + 12 + 12 + 10 = 50
50 : 11 = 4
Rest 6 = Prüfziffer
Ausnahme:
Ist die Unterkontonummer "00" kann es vorkommen, dass sie
auf den Zahlungsverkehrsbelegen oder in beleglosen
Datensätzen nicht angegeben ist, die Kontonummer jedoch
um führende Nullen ergänzt wurde. Die Prüfziffer ist dann an
die 10. Stelle gerückt. Die Berechnung der Prüfziffer ist wie
folgt durchzuführen:
Beispiel: (Kontoart = 0)
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 0 0 0 0 1 2 3 4 5 6
Gewichtung: 6 5 4 3 2
6 + 10 + 12 + 12 + 10 = 50
50 : 11 = 4
Rest 6 = Prüfziffer
Testkontonummern:
5-stellige Kontonr. (Kontoart = 0) 0006543200
6-stellige Kontonr. (Kontoart = 9) 9012345600
7-stellige Kontonr. (Kontoart = 7) 7876543100
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_76.py
- Öffentliche API:
  - @register("76") def validate_method_76(blz: str, account: str) -> bool
  - @register_generator("76") def generate_account_method_76(blz: str, rng: random.Random) -> str
- Qualitätskriterien:
  - Rein deterministische Validatoren (keine Seiteneffekte)
  - Vollständige Abdeckung von Sonderfällen laut Spezifikation
  - Generator erzeugt ausschließlich laut Validator gültige Kontonummern
  - Berücksichtige führende Nullen und eventuelle Längen-/Segmentregeln

Aufgaben:
1) Validator implementieren oder prüfen
- Beschreibe die Rechenschritte exakt gemäß Spezifikation (Gewichte, Modulus, Sonderregeln, Varianten).
- Implementiere/prüfe Hilfsfunktionen (lokal in der Datei), die zur Berechnung nötig sind.
- Stelle sicher, dass invalid/edge-cases korrekt behandelt werden (z. B. check==10 -> invalid/9/0 je nach Methode).

2) Generator implementieren oder prüfen
- Implementiere/prüfe eine direkte Generatorfunktion, die gültige Kontonummern gemäß der Methode konstruiert.
- Wenn die Spezifikation mehrere Varianten erlaubt, stelle sicher, dass die Ausgabe jeweils zur Variante passt oder wähle eine gültige Standardvariante.
- Generator sollte effizient sein (kein exzessiver Retry), sofern der Algorithmus eine direkte Ableitung der Prüfziffer zulässt.

3) Verifikation
- Führe nachvollziehbare Beispielrechnungen an (aus der Spezifikation oder selbst konstruiert) und überprüfe, dass die Implementierung übereinstimmt.
- Prüfe, dass der Generator ausschließlich Werte produziert, die der Validator als gültig einstuft.

Abgabe:
- Vollständiger Python-Codeausschnitt für method_76.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
