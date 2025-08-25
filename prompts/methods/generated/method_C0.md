# Implementierung Bundesbank Prüfziffermethode: C0

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C0") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Kontonummern mit zwei führenden Nullen sind nach
Variante 1 zu prüfen. Führt die Berechnung nach der Variante
1 zu einem Prüfzifferfehler, ist die Berechnung nach Variante
2 vorzunehmen.
Kontonummern mit weniger oder mehr als zwei führenden
Nullen sind ausschließlich nach der Variante 2 zu prüfen.
Variante 1:
Modulus 11, Gewichtung 2, 4, 8, 5, 10, 9, 7, 3, 6, 1, 2, 4
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 52.
Testkontonummern (richtig) mit BLZ 130 511 72:
43001500, 48726458
Testkontonummern (falsch) mit BLZ 130 511 72:
82335729, 29837521
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 3
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 20.
Testkontonummern (richtig): 0082335729, 0734192657,
6932875274
Testkontonummern (falsch): 0132572975, 3038752371
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C0.py
- Öffentliche API:
  - @register("C0") def validate_method_C0(blz: str, account: str) -> bool
  - @register_generator("C0") def generate_account_method_C0(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C0.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.