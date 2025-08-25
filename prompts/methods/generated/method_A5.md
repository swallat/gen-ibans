# Implementierung Bundesbank Prüfziffermethode: A5

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode A5") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Gewichtung und Berechnung erfolgen nach der Methode 00.
Führt die Berechnung nach Variante 1 zu einem Prüfzifferfehler,
so sind 10-stellige Konten mit einer 9 an Stelle 1
falsch, alle anderen Konten sind nach Variante 2 zu prüfen.
Testkontonummern (richtig): 9941510001, 9961230019
9380027210, 9932290910
Testkontonummern (falsch): 9941510002, 9961230020
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 10
Gewichtung und Berechnung erfolgen nach der Methode 10.
Testkontonummern (richtig): 0000251437, 0007948344
0000159590, 0000051640
Testkontonummern (falsch): 0000251438, 0007948345
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_A5.py
- Öffentliche API:
  - @register("A5") def validate_method_A5(blz: str, account: str) -> bool
  - @register_generator("A5") def generate_account_method_A5(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_A5.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.