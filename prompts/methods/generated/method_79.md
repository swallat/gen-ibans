# Implementierung Bundesbank Prüfziffermethode: 79

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 79") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2 ff.
Die Kontonummer ist 10-stellig. Die Berechnung und
Ergebnisse entsprechen dem Verfahren 00. Es ist jedoch zu
beachten, dass die Berechnung vom Wert der 1. Stelle der
Kontonummer abhängig ist.
Variante 1
Die 1. Stelle der Kontonummer hat die Ziffer 3, 4, 5, 6, 7
oder 8
Die für die Berechnung relevanten Stellen der Kontonummer
befinden sich in den Stellen 1 bis 9. Die 10. Stelle ist per
Definition die Prüfziffer.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 3 2 3 0 0 1 2 6 8 8
Gewichtung: 2 1 2 1 2 1 2 1 2
Variante 2
Die 1. Stelle der Kontonummer hat die Ziffer 1, 2 oder 9
Die für die Berechnung relevanten Stellen der Kontonummer
befinden sich in den Stellen 1 bis 8. Die 9. Stelle ist die
Prüfziffer der 10-stelligen Kontonummer.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 9 0 1 1 2 0 0 1 4 0
Gewichtung: 1 2 1 2 1 2 1 2
Kontonummern, die in der 1. Stelle eine 0 haben, wurden
nicht vergeben und gelten deshalb als falsch.
Testkontonummern: 3230012688, 4230028872,
5440001898, 6330001063, 7000149349,
8000003577, 1550167850, 9011200140
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_79.py
- Öffentliche API:
  - @register("79") def validate_method_79(blz: str, account: str) -> bool
  - @register_generator("79") def generate_account_method_79(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_79.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.