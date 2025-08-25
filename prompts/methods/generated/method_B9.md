# Implementierung Bundesbank Prüfziffermethode: B9

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B9") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Kontonummern mit weniger als zwei oder mehr als drei
führenden Nullen sind falsch. Die Kontonummern mit zwei
führenden Nullen sind nach Variante 1, mit drei führenden
Nullen nach Variante 2 zu prüfen.
Variante 1:
Modulus (11,10), Gewichtung 1, 3, 2, 1, 3, 2, 1
Die für die Berechnung relevanten Stellen der Kontonummer
befinden sich - von links nach rechts gelesen - in den Stellen
3-9 (die Prüfziffer ist in Stelle 10). Sie sind – von rechts nach
links – mit den zugehörigen Gewichtungsfaktoren zu
multiplizieren.
Zum jeweiligen Produkt ist der zugehörige Gewichtungsfaktor
zu addieren. Das jeweilige Ergebnis ist durch 11 zu
dividieren. Die sich aus der Division ergebenden Reste sind
zu summieren. Diese Summe ist durch 10 zu dividieren. Der
Rest ist die berechnete Prüfziffer.
Führt die Berechnung zu einem Prüfzifferfehler, so ist die
berechnete Prüfziffer um 5 zu erhöhen und erneut zu prüfen.
Ist die Prüfziffer größer oder gleich 10, ist 10 abzuziehen und
das Ergebnis ist dann die Prüfziffer.
Rechenbeispiel mit der Testkontonummer 0087920187:
8 x 1 = 8 + 1 = 9 9 : 11 = 0 Rest 9
7 x 2 = 14 + 2 = 16 16 : 11 = 1 Rest 5
9 x 3 = 27 + 3 = 30 30 : 11 = 2 Rest 8
2 x 1 = 2 + 1 = 3 3 : 11 = 0 Rest 3
0 x 2 = 0 + 2 = 2 2 : 11 = 0 Rest 2
1 x 3 = 3 + 3 = 6 6 : 11 = 0 Rest 6
8 x 1 = 8 + 1 = 9 9 : 11 = 0 Rest 9
Summe der Reste: 42
42 : 10 = 4 Rest 2 (= falsche Prüfziffer)
==> 2 + 5 = 7 (= Prüfziffer)Testkontonummern (richtig):
87920187, 41203755,
81069577, 61287958,
58467232
Testkontonummern (falsch): 88034023, 43025432,
86521362, 61256523,
54352684
Variante 2:
Modulus 11, Gewichtung 1, 2, 3, 4, 5, 6
Die für die Berechnung relevanten Stellen der Kontonummer
befinden sich - von links nach rechts gelesen- in den Stellen
4-9 (die Prüfziffer ist in Stelle 10). Sie sind von rechts nach
links mit den zugehörigen Gewichtungsfaktoren zu
multiplizieren. Die Summe dieser Produkte ist zu bilden, und
das erzielte Ergebnis ist durch 11 zu dividieren. Der Rest ist
die berechnete Prüfziffer.
Führt die Berechnung zu einem Prüfzifferfehler, so ist die
berechnete Prüfziffer um 5 zu erhöhen und erneut zu prüfen.
Ist die Prüfziffer größer oder gleich 10, ist 10 abzuziehen und
das Ergebnis ist dann die Prüfziffer.
Rechenbeispiel mit der Testkontonummer 7125633:
7 x 6 = 42
1 x 5 = 5
2 x 4 = 8
5 x 3 = 15
6 x 2 = 12
3 x 1 = 3
Summe = 85
85 : 11 = 7 Rest 8 (= falsche Prüfziffer)
==> 8 + 5 = 13 (= Prüfziffer größer 10)
==> 13 - 10 = 3 (= Prüfziffer)
Testkontonummern (richtig): 7125633, 1253657, 4353631
Testkontonummern (falsch): 2356412, 5435886, 9435414
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B9.py
- Öffentliche API:
  - @register("B9") def validate_method_B9(blz: str, account: str) -> bool
  - @register_generator("B9") def generate_account_method_B9(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B9.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
