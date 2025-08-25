# Implementierung Bundesbank Prüfziffermethode: 86

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 86") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1
Methode A
Die Kontonummer ist durch linksbündige Nullenauffüllung 10-
stellig darzustellen. Die Berechnung und die möglichen
Ergebnisse entsprechen dem Verfahren 00; es ist jedoch zu
beachten, dass nur die Stellen 4 bis 9 in das
Prüfzifferberechnungsverfahren einbezogen werden. Die Stelle
10 der Kontonummer ist die Prüfziffer.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x x x x P
Gewichtung: 1 2 1 2 1 2
Testkontonummern: 340968, 1001171, 1009588
Führt die Berechnung nach Methode A zu einem Prüfzifferfehler,
so ist die Berechnung nach Methode B vorzunehmen.
Methode B
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Kontonummer ist durch linksbündige Nullenauffüllung 10-
stellig darzustellen. Die Stellen 4 bis 9 der Kontonummer
werden von rechts nach links mit den Ziffern 2, 3, 4, 5, 6, 7
multipliziert. Die weitere Berechnung und die möglichen
Ergebnisse entsprechen dem Verfahren 32. Die Stelle 10 ist
die Prüfziffer.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x x x x P
Gewichtung: 7 6 5 4 3 2
Testkontonummern: 123897, 340960
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung gemäß der Ausnahme in Methode 51 mit den
gleichen Ergebnissen und Testkontonummern.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_86.py
- Öffentliche API:
  - @register("86") def validate_method_86(blz: str, account: str) -> bool
  - @register_generator("86") def generate_account_method_86(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_86.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
