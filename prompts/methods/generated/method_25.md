# Implementierung Bundesbank Prüfziffermethode: 25

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 25") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9 ohne Quersumme
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Ziffern 2, 3, 4, 5, 6, 7, 8 und 9 zu multiplizieren.
Die jeweiligen Produkte werden addiert. Die Summe ist durch
11 zu dividieren. Der verbleibende Rest wird vom Divisor
subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt nach der
Division durch 11 kein Rest, ist die Prüfziffer = 0. Ergibt sich als
Rest 1, so ist die Prüfziffer immer 0 und kann nur für die
Arbeitsziffern 8 und 9 verwendet werden. Die Kontonummer ist
für die Arbeitsziffern 0, 1, 2, 3, 4, 5, 6 und 7 dann nicht
verwendbar.
Die Arbeitsziffer (Geschäftsbereich oder Kontoart) befindet sich
in der 2. Stelle (von links) des 10-stelligen
Kontonummernfeldes.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x x x x P
Gewichtung: 9 8 7 6 5 4 3 2
Die Kontonummer ist 9-stellig, wobei die 1. Stelle die
Arbeitsziffer und die letzte Stelle die Prüfziffer ist.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 5 2 1 3 8 2 1 8 P
Gewichtung: 9 8 7 6 5 4 3 2
45 + 16 + 7 + 18 + 40 + 8 + 3 + 16 = 153
153 : 11 = 13, Rest 10
11 - 10 = 1, Prüfziffer = 1
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_25.py
- Öffentliche API:
  - @register("25") def validate_method_25(blz: str, account: str) -> bool
  - @register_generator("25") def generate_account_method_25(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_25.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.