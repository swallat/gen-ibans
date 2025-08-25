# Implementierung Bundesbank Prüfziffermethode: A8

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode A8") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist durch linksbündige Nullenauffüllung 10-
stellig darzustellen. Die 10. Stelle ist per Definition die
Prüfziffer.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Stellen 4 bis 9 der Kontonummer werden von rechts nach
links mit den Ziffern 2, 3, 4, 5, 6, 7 multipliziert. Die weitere
Berechnung und die möglichen Ergebnisse entsprechen dem
Verfahren 06. Führt die Berechnung nach Variante 1 zu
einem Prüfzifferfehler, so sind die Konten nach Variante 2 zu
prüfen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A=10)
Kontonr.: x x x x x x x x x P
Gewichtung: 7 6 5 4 3 2
Testkontonummern (richtig): 7436661, 7436670, 1359100
Testkontonummern (falsch): 7436660, 7436678
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1
Die Stellen 4 bis 9 der Kontonummer werden von rechts nach
links mit den Ziffern 2, 1, 2, 1, 2, 1 multipliziert. Die weiter
Berechnung und die möglichen Ergebnisse entsprechen dem
Verfahren 00.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A=10)
Kontonr.: x x x x x x x x x P
Gewichtung: 1 2 1 2 1 2
Testkontonummern (richtig): 7436660, 7436678,
0003503398, 0001340967
Testkontonummern (falsch): 7436666, 7436677,
0003503391, 0001340966
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung gemäß der Ausnahme in Methode 51 mit den
gleichen Ergebnissen und Testkontonummern.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_A8.py
- Öffentliche API:
  - @register("A8") def validate_method_A8(blz: str, account: str) -> bool
  - @register_generator("A8") def generate_account_method_A8(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_A8.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
