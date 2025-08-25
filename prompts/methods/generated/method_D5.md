# Implementierung Bundesbank Prüfziffermethode: D5

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D5") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
1. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 0, 0
2. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
3. Modulus 7, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
4. Modulus 10, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
Die Kontonummer ist einschließlich der Prüfziffer (P)
10-stellig, ggf. ist die Kontonummer für die Prüfzifferberechnung
durch linksbündige Auffüllung mit Nullen
10-stellig darzustellen.
Konten mit der Ziffernfolge 99 an Stelle 3 und 4 (xx99xxxxxx)
sind nur nach Variante 1 zu prüfen. Alle übrigen Konten sind
nacheinander nach den Varianten 2, ggf. 3 und ggf. 4 zu
prüfen.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 0, 0
In die Prüfzifferberechnung werden nur die Stellen 3 bis 9
einbezogen. Die Stelle 10 ist die Prüfziffer (P). Die weitere
Berechnung erfolgt nach dem Verfahren 06.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 5 9 9 9 2 4 2 1 3 3
Gewichtung 0 0 8 7 6 5 4 3 2 P
Produkt 0 0 72 63 12 20 8 3 6 184
184 : 11 = 16, Rest 8
11 - 8 = 3 = P
Testkontonummern (richtig): 5999718138, 1799222116,
0099632004
Testkontonummern (falsch): 3299632008, 1999204293,
0399242139
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
In die Prüfzifferberechnung werden nur die Stellen 4 bis 9
einbezogen. Die Stelle 10 ist die Prüfziffer (P). Die weitere
Berechnung erfolgt nach dem Verfahren 06.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 0 0 0 4 7 1 1 1 7 4
Gewichtung 0 0 0 7 6 5 4 3 2 P
Produkt 0 0 0 28 42 5 4 3 14 96
96 : 11 = 8, Rest 8
11 - 8 = 3 = P
Testkontonummern (richtig): 0004711173, 0007093330,
0000127787
Testkontonummern (falsch): 0004711172, 8623420004,
0001123458
Führt die Berechnung zu einem Fehler, ist nach Variante 3 zu
prüfen.

Variante 3:
Modulus 7, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
Die Stellen 4 bis 9 der Kontonummer werden von rechts nach
links mit den Gewichten multipliziert. Die jeweiligen Produkte
werden addiert. Die Summe ist durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer (Stelle 10). Verbleibt nach der
Division durch 7 kein Rest, ist die Prüfziffer 0.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 0 0 0 4 7 1 1 1 7 4
Gewichtung 0 0 0 7 6 5 4 3 2 P
Produkt 0 0 0 28 42 5 4 3 14 96
96 : 7 = 13, Rest 5
7 - 5 = 2 = P
Testkontonummern (richtig): 0004711172, 0007093335
Testkontonummern (falsch) : 8623410000, 0001123458
Führt die Berechnung zu einem Fehler, ist nach Variante 4 zu
prüfen.
Variante 4:
Modulus 10, Gewichtung 2, 3, 4, 5, 6, 7, 0, 0, 0
Die Berechnung erfolgt analog zu Variante 3, jedoch ist als
Divisor der Wert 10 zu verwenden. Verbleibt nach der
Division durch 10 kein Rest, ist die Prüfziffer 0.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 0 0 0 4 7 1 1 1 7 4
Gewichtung 0 0 0 7 6 5 4 3 2 P
Produkt 0 0 0 28 42 5 4 3 14 96
96 : 10 = 9, Rest 6
10 - 6 = 4 = P
Testkontonummern (richtig): 0000100062, 0000100088
Testkontonummern (falsch): 0000100084, 0000100085
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D5.py
- Öffentliche API:
  - @register("D5") def validate_method_D5(blz: str, account: str) -> bool
  - @register_generator("D5") def generate_account_method_D5(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D5.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.