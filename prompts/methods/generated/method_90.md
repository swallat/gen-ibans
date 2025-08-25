# Implementierung Bundesbank Prüfziffermethode: 90

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 90") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist immer 10-stellig, ggf. ist die
Kontonummer durch linksbündige Auffüllung mit Nullen 10-
stellig darzustellen. Die Stelle 10 der Kontonummer ist per
Definition die Prüfziffer. Kontonummern, die nach
Durchführung der unten näher aufgeführten Berechnungsmethoden
nicht zu einem richtigen Ergebnis führen, sind nicht
gültig.
Die für die Berechnung relevante Kundennummer (K) befindet
sich bei der Methode A und G in den Stellen 4 bis 9 der
Kontonummer und bei den Methoden B bis E in den Stellen 5
bis 9.
Ausnahme:
Ist nach linksbündigem Auffüllen mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten) befindet sich die
für die Berechnung relevante Sachkontonummer (S) in den
Stellen 3 bis 9. Diese Kontonummern sind ausschließlich
nach Methode F zu prüfen.
Kundenkonten
Kundenkonten haben im Gegensatz zu Sachkonten an der
Stelle 3 nicht die Ziffer 9 stehen.
Ergibt die Berechnung der Prüfziffer nach dem Verfahren A
einen Prüfzifferfehler, so sind weitere Berechnungen mit den
Methoden B bis E und G vorzunehmen. kundenkontonummern,
die nach Durchführung aller Berechnungsmethoden
A bis E und G nicht zu einem richtigen Ergebnis
führen, ist nicht gültig.
Methode A:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 7 6 5 4 3 2
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06.
Testkontonummern:
richtig: 0001975641, 0001988654
falsch: 0001924592
falsch: 0000654321 (testbar nach Methode C)
Methode B
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Die Berechnung und die möglichen Ergebnisse entsprechen
dem Verfahren 06.
Testkontonummern:
richtig: 0001863530, 0001784451
falsch: 0000901568
falsch: 0000997664 (testbar nach Methode C)
falsch: 0000863536 (testbar nach Methode D)
Methode C
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Gewichten zu multiplizieren. Die jeweiligen
Produkte werden addiert. Die Summe der Produkte ist durch
7 zu dividieren. Der verbleibende Rest wird vom Divisor (7)
subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt kein
Rest, ist die Prüfziffer 0.
Kontonummern, die in der Stelle 10 die Werte 7, 8 oder 9
haben, sind nach dieser Methode nicht gültig.
Testkontonummern:
richtig: 0000654321, 0000824491
falsch: 0000820487
falsch: 0000820484 (testbar nach Methode D)
falsch: 0000654328 (testbar nach Methode E)
Methode D
Modulus 9, Gewichtung 2, 3, 4, 5, 6
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Gewichten zu multiplizieren. Die jeweiligen
Produkte werden addiert. Die Summe der Produkte ist durch
9 zu dividieren. Der verbleibende Rest wird vom Divisor (9)
subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt kein
Rest, ist die Prüfziffer 0.
Kontonummern, die an der Stelle 10 den Wert 9 haben sind
nach dieser Methode nicht gültig.
Testkontonummern:
richtig: 0000677747, 0000840507
falsch: 0000726393
falsch: 0000677742 (testbar nach Methode E)
falsch: 0000726390 (testbar nach Methode G)
Methode E
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 2 1 2 1 2
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Gewichten zu multiplizieren. Die jeweiligen
Produkte werden addiert. Die Summe der Produkte ist durch
10 zu dividieren. Der verbleibende Rest wird vom Divisor (10)
subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt kein
Rest, ist die Prüfziffer 0.
Testkontonummern:
richtig: 0000996663, 0000666034
falsch: 0000924591
falsch: 0000465431 (testbar nach Methode G)
Methode G
Modulus 7, Gewichtung 2, 1, 2, 1, 2, 1
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 1 2 1 2 1 2
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Gewichten zu multiplizieren. Die jeweiligen
Produkte werden addiert. Die Summe der Produkte ist durch
7 zu dividieren. Der verbleibende Rest wird vom Divisor (7)
subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt kein
Rest, ist die Prüfziffer 0.
Testkontonummern:
richtig: 0004923250, 0003865960
falsch: 0003865964
Sachkonten
Sachkonten haben im Gegensatz zu Kundenkonten an der
Stelle 3 die Ziffer 9 stehen.
Methode F
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x S S S S S S S P
Gewichtung: 8 7 6 5 4 3 2
Die Berechnung und die möglichen Ergebnisse entsprechen
dem Verfahren 06. Es ist jedoch die vorgenannte
Gewichtung zu beachten.
Testkontonummern:
richtig: 0099100002
falsch: 0099100007
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_90.py
- Öffentliche API:
  - @register("90") def validate_method_90(blz: str, account: str) -> bool
  - @register_generator("90") def generate_account_method_90(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_90.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.