# Implementierung Bundesbank Prüfziffermethode: B8

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B8") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen. Die
10. Stelle der Kontonummer ist die Prüfziffer.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 3 (modifiziert)
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 20. Führt die Berechnung nach Variante 1 zu einem
Prüfzifferfehler, so ist nach Variante 2 zu prüfen.
Testkontonummern (richtig): 0734192657, 6932875274
Testkontonummern (falsch): 3145863029, 2938692523,
0132572975, 5432198760,
9070873333, 5011654366
9000412340, 9310305011
Variante 2:
Modulus 10, iterierte Transformation
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 29. Führt die Berechnung nach Variante 2 zu einem
Prüfzifferfehler, so ist nach Variante 3 zu prüfen.
Testkontonummern (richtig): 3145863029, 2938692523
Testkontonummern (falsch): 0132572975, 5432198760,
9070873333, 9000412340,
9310305011
Variante 3:
Für die folgenden Kontonummernkreise gilt die Methode 09
(keine Prüfzifferberechnung).
 10-stellige Kontonummer; 1. + 2. Stelle = 51 - 59
Kontonummernkreis 5100000000 – 5999999999
 10-stellige Kontonummer; Stellen 1 - 3 = 901 - 910
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B8.py
- Öffentliche API:
  - @register("B8") def validate_method_B8(blz: str, account: str) -> bool
  - @register_generator("B8") def generate_account_method_B8(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B8.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
