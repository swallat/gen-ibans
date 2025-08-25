# Implementierung Bundesbank Prüfziffermethode: 66

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 66") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 0, 0, 7
Aufbau der 9-stelligen Kontonummer (innerhalb des
zwischenbetrieblich 10-stelligen Feldes)
Stelle 1 = gehört nicht zur Kontonummer, muss
daher 0 sein
2 = Stammnummer
3 - 4 = Unterkontonummer, wird bei der Prüfzifferberechnung
nicht berücksichtigt
5 - 9 = Stammnummer
10 = Prüfziffer
Der 9-stelligen Kontonummer wird für die Prüfzifferberechnung
eine 0 vorangestellt. Die Prüfziffer steht in Stelle 10. Die für die
Berechnung relevante 6-stellige Stammnummer (Kundenummer)
befindet sich in den Stellen 2 und 5 bis 9. Die zweistellige
Unterkontonummer (Stellen 3 und 4) wird nicht in das
Prüfzifferberechnungsverfahren mit einbezogen und daher mit 0
gewichtet. Die einzelnen Stellen der Stammnummer sind von
rechts nach links mit den Ziffern 2, 3, 4, 5, 6, 0, 0, 7 zu
multiplizieren. Die jeweiligen Produkte werden addiert. Die
Summe ist durch 11 zu dividieren. Bei einem verbleibenden Rest
von 0 ist die Prüfziffer 1. Bei einem Rest von 1 ist die Prüfziffer 0.
Verbleibt ein Rest von 2 bis 10, so wird dieser vom Divisor (11)
subtrahiert. Die Differenz ist dann die Prüfziffer.
Zusammengefasst:
Summe dividiert durch 11 = x, Rest
Rest = 0 Prüfziffer = 1
Rest = 1 Prüfziffer = 0
Rest = 2 bis 10 Prüfziffer = 11 minus Rest
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 0 1 0 0 1 5 0 5 0 P
Gewichtung: 0 7 0 0 6 5 4 3 2
0 + 7 + 0 + 0 + 6 +25 + 0 +15 + 0 = 53
53 : 11 = 4, Rest 9, 11-9=2, Prüfziffer = 2
Die vollständige Kontonummer lautet: 100150502
Ausnahme:
Ist die Stelle 2 der Kontonummer der Wert = 9, ist die
Kontonummer nicht prüfziffergesichert; es gilt die Methode 09
(keine Prüfzifferberechnung). Beispiel der Kontonummer:
0983393104.
Testkontonummern: 100154508, 101154508,
100154516, 101154516
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_66.py
- Öffentliche API:
  - @register("66") def validate_method_66(blz: str, account: str) -> bool
  - @register_generator("66") def generate_account_method_66(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_66.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.