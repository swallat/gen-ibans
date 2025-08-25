# Implementierung Bundesbank Prüfziffermethode: 85

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 85") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist immer 10-stellig. Die für die Berechnung
relevante Kundennummer (K) befindet sich bei der Methode A
in den Stellen 4 bis 9 der Kontonummer und bei den Methoden
B + C in den Stellen 5 bis 9, die Prüfziffer in Stelle 10 der
Kontonummer.
Methode A:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 7 6 5 4 3 2
Testkontonummern: 0001156071, 0001156136
Ergibt die Berechnung der Prüfziffer nach der Methode A einen
Prüfzifferfehler, ist eine weitere Berechnung mit der Methode B
vorzunehmen.
Methode B:
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 33.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Testkontonummer: 0000156078
Ergibt auch die Berechnung der Prüfziffer nach Methode B
einen Prüfzifferfehler, ist eine weitere Berechnung mit der
Methode C vorzunehmen.
Methode C:
Kontonummern, die bis zur Methode C gelangen und in der 10.
Stelle eine 7, 8 oder 9 haben, sind ungültig.
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Das Berechnungsverfahren entspricht Methode B.
Die Summe der Produkte ist jedoch durch 7 zu dividieren.
Der verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer. Verbleibt kein Rest, ist die
Prüfziffer 0.
Testkontonummer: 0000156071
Ausnahme:
Sind die 3. und 4. Stelle der Kontonummer = 99, so ist
folgende Prüfzifferberechnung maßgebend:
Modulus: 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Die für die Berechnung relevanten Stellen 3 bis 9 der
Kontonummer werden von rechts nach links mit den Ziffern 2,
3, 4, 5, 6, 7, 8 multipliziert. Die weitere Berechnung und
möglichen Ergebnisse entsprechen dem Verfahren 02.
Testkontonummer: 3199100002
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_85.py
- Öffentliche API:
  - @register("85") def validate_method_85(blz: str, account: str) -> bool
  - @register_generator("85") def generate_account_method_85(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_85.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
