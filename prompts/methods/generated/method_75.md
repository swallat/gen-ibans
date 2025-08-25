# Implementierung Bundesbank Prüfziffermethode: 75

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 75") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Die Kontonummer (6-, 7- oder 9-stellig) ist durch linksbündige
Nullenauffüllung 10-stellig darzustellen. Die für die Berechnung
relevante 5-stellige Stammnummer (S) wird von
links nach rechts mit den Ziffern 2, 1, 2, 1, 2 multipliziert. Die
weitere Berechnung und die Ergebnisse entsprechen dem
Verfahren 00.
Zusammensetzung der Kontonummer:
S = Stammnummer
X = Weitere Ziffern der Kontonummer, die jedoch nicht in
die Prüfzifferberechnung mit einbezogen werden
P = Prüfziffer
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
6stell. Kontonr.: 0 0 0 0 S S S S S P
7stell. Kontonr.: 0 0 0 X S S S S S P
9stell. Kontonr.: 0 9 S S S S S P X X
10stell. Kontonr.: 0 S S S S S P X X X
Anmerkungen:
Bei 6- und 7-stelligen Kontonummern befindet sich die für die
Berechnung relevante Stammnummer in den Stellen 5 bis 9,
die Prüfziffer in Stelle 10 der Kontonummer.
Bei 9-stelligen Kontonummern befindet sich die für die
Berechnung relevante Stammnummer in den Stellen 2 bis 6,
die Prüfziffer in der 7. Stelle der Kontonummer. Ist die erste
Stelle der 9-stelligen Kontonummer = 9 (2. Stelle der
»gedachten« Kontonummer), so befindet sich die für die
Berechnung relevante Stammnummer in den Stellen 3 bis 7,
die Prüfziffer in der 8. Stelle der Kontonummer.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_75.py
- Öffentliche API:
  - @register("75") def validate_method_75(blz: str, account: str) -> bool
  - @register_generator("75") def generate_account_method_75(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_75.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
