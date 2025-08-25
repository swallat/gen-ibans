# Implementierung Bundesbank Prüfziffermethode: D2

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D2") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2, 3, 4
Die Berechnung, Ausnahmen und möglichen Ergebnisse
entsprechen der Methode 95. Führt die Berechnung nach
Variante 1 zu einem Prüfzifferfehler, so ist nach Variante 2 zu
prüfen.
Testkontonummern (richtig): 189912137, 235308215
Testkontonummern (falsch): 4455667784, 1234567897,
51181008, 71214205
6414241, 179751314
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Berechnung und möglichen Ergebnisse entsprechen der
Methode 00. Führt auch die Berechnung nach Variante 2 zu
einem Prüfzifferfehler, so ist nach Variante 3 zu prüfen.
Testkontonummern (richtig): 4455667784, 1234567897
Testkontonummern (falsch): 51181008, 71214205,
6414241, 179751314
Variante 3:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Berechnung, Ausnahmen und möglichen Ergebnisse
entsprechen der Methode 68. Führt auch die Berechnung
nach Variante 3 zu einem Prüfzifferfehler, so ist die
Kontonummer falsch.
Testkontonummern (richtig): 51181008, 71214205
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D2.py
- Öffentliche API:
  - @register("D2") def validate_method_D2(blz: str, account: str) -> bool
  - @register_generator("D2") def generate_account_method_D2(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D2.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.