# Implementierung Bundesbank Prüfziffermethode: A4

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode A4") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
1. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
2. Modulus 7, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
3. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 0, 0, 0, 0
4. Modulus 11, Gewichtung 2, 3, 4, 5, 6
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen. Zur
Prüfung einer Kontonummer sind die folgenden Varianten zu
rechnen. Dabei ist zu beachten, dass Kontonummern mit der
Ziffernfolge 99 an den Stellen 3 und 4 (XX99XXXXXX) nur
nach Variante 3 und ggf. 4 zu prüfen sind. Alle anderen
Kontonummern sind nacheinander nach den Varianten 1, ggf.
2 und ggf. 4 zu prüfen.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
In die Prüfzifferberechnung werden nur die Stellen 4 bis 9
einbezogen. Die Stelle 10 ist die Prüfziffer. Die weitere
Berechnung erfolgt nach dem Verfahren 06.
Beispiel:
Kontonr.: 0 0 0 4 7 1 1 1 7 3
Gewichtung: 0 0 0 7 6 5 4 3 2 P
Produkt: 0+ 0+ 0+28+42+ 5+ 4+ 3+14=96
96 : 11 = 8, Rest 8
11 - 8 = 3 = P
Testkontonummern (richtig): 0004711173, 0007093330
Testkontonummern (falsch): 0004711172, 8623420004,
0001123458
Führt die Berechnung zu einem Fehler, ist nach Variante 2 zu
prüfen.
Variante 2:
Modulus 7, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
Die Stellen 4 bis 9 der Kontonummer werden von rechts nach
links mit den Gewichten multipliziert. Die jeweiligen Produkte
werden addiert. Die Summe ist durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer (Stelle 10). Verbleibt nach der
Division kein Rest, ist die Prüfziffer 0.
Beispiel:
Kontonr.: 0 0 0 4 7 1 1 1 7 2
Gewichtung: 0 0 0 7 6 5 4 3 2 P
Produkt: 0+ 0+ 0+28+42+ 5+ 4+ 3+ 14 =96
96 : 7 = 13, Rest 5
7 - 5 = 2 = P
Testkontonummern (richtig): 0004711172, 0007093335
Testkontonummern (falsch): 8623420000, 0001123458
Führt die Berechnung zu einem Fehler, ist nach Variante 4 zu
prüfen

Variante 3:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 0, 0, 0, 0
In die Prüfzifferberechnung werden nur die Stellen 5 bis 9
einbezogen. Die Stelle 10 ist die Prüfziffer. Die weitere
Berechnung erfolgt nach dem Verfahren 06.
Beispiel:
1 1 9 9 5 0 3 0 1 0
Gewichtung: 0 0 0 0 6 5 4 3 2 P
Produkt: 0+ 0+ 0+ 0+30+0+12+ 0+ 2 =44
44: 11 = 4, Rest 0 = P
Testkontonummern (richtig): 1199503010, 8499421235
Testkontonummern (falsch): 1299503117, 6099702031
Führt die Berechnung zu einem Fehler, ist nach Variante 4 zu
prüfen.
Variante 4:
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Die Gewichtung und Berechnung erfolgen nach Methode 93.
Testkontonummern (richtig):
0000862342, 8997710000, 0664040000 (Modulus 7)
0000905844, 5030101099 (Modulus 11)
0001123458, 1299503117
Testkontonummern (falsch): 0000399443, 0000553313
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_A4.py
- Öffentliche API:
  - @register("A4") def validate_method_A4(blz: str, account: str) -> bool
  - @register_generator("A4") def generate_account_method_A4(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_A4.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.