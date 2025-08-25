# Implementierung Bundesbank Prüfziffermethode: C3

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C3") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Die 10. Stelle der Kontonummer ist die Prüfziffer.
Kontonummern, die an der 1. Stelle der 10-stelligen
Kontonummer einen Wert ungleich „9“ beinhalten, sind nach
der Variante 1 zu prüfen. Kontonummern, die an der 1. Stelle
der 10-stelligen Kontonummer den Wert „9“ beinhalten, sind
nach der Variante 2 zu prüfen.
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
Testkontonummern (richtig): 9294182, 4431276, 19919
Testkontonummern (falsch): 17002, 123451, 122448
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 0, 0, 0, 0
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 58.
Testkontonummern (richtig): 9000420530, 9000010006,
9000577650
Testkontonummern (falsch): 9000734028, 9000733227,
9000731120
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C3.py
- Öffentliche API:
  - @register("C3") def validate_method_C3(blz: str, account: str) -> bool
  - @register_generator("C3") def generate_account_method_C3(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C3.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.