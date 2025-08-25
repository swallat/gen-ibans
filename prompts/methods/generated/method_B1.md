# Implementierung Bundesbank Prüfziffermethode: B1

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B1") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung
durchlinksbündige Auffüllung mit Nullen 10-stellig
darzustellen.
Variante 1:
Modulus 10, Gewichtung 7,3,1,7,3,1,7,3,1
Gewichtung und Berechnung erfolgen nach der Methode 05.
Führt die Berechnung nach Variante 1 zu einem
Prüfzifferfehler, so ist nach Variante 2 zu prüfen.
Testkontonummern (richtig): 1434253150, 2746315471
Testkontonummern (falsch): 1501824, 1501832,539290858,
0123456789, 2345678901,
5678901234, 7414398260,
7414398268, 8347251693,
8347251699
Variante 2:
Modulus 10, Gewichtung 3,7,1,3,7,1,3,7,1
Gewichtung und Berechnung erfolgen nach der Methode 01.
Führt die Berechnung nach Variante 2 zu einem
Prüfzifferfehler, so ist nach Variante 3 zu prüfen.
Testkontonummern (richtig): 7414398260, 8347251693
Testkontonummern (falsch): 1501824, 1501832, 539290858,
0123456789, 2345678901,
5678901234, 7414398268,
8347251699
Variante 3:
Modulus 10, Gewichtung 2,1,2,1,2,1, 2, 1,2
Gewichtung und Berechnung erfolgen nach der Methode 00.
Testkontonummern (richtig): 1501824, 1501832, 539290858,
7414398268, 8347251699
Testkontonummern (falsch): 0123456789, 2345678901,
5678901234
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B1.py
- Öffentliche API:
  - @register("B1") def validate_method_B1(blz: str, account: str) -> bool
  - @register_generator("B1") def generate_account_method_B1(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B1.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.