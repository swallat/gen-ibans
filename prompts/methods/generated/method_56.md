# Implementierung Bundesbank Prüfziffermethode: 56

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 56") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2, 3, 4
Die Stellen 1 bis 9 der Kontonummer werden von rechts nach
links mit den Ziffern 2, 3, 4, 5, 6, 7, 2, 3, 4 multipliziert. Die
jeweiligen Produkte werden addiert und die Summe durch 11
dividiert. Der Rest wird von 11 abgezogen, das Ergebnis ist die
Prüfziffer. Prüfziffer ist die 10. Stelle der Kontonummer.
Beispiel 1)
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 0 2 9 0 5 4 5 0 0 P
Gewichtung: 4 3 2 7 6 5 4 3 2
0 + 6 + 18 + 0 + 30 + 20 + 20 + 0 + 0 =
94 : 11 = 8, Rest 6
11 - 6 = 5
Die Prüfziffer ist 5
Bei dem Ergebnis 10 oder 11 ist die Kontonummer ungültig.
Beispiel 2)
Beginnt eine 10-stellige Kontonummer mit 9, so wird beim
Ergebnis 10 die Prüfziffer = 7 und beim Ergebnis 11 die
Prüfziffer = 8 gesetzt.
Stellennr.:
Kontonr.:
1
9
2
7
3
1
4
8
5
3
6
0
7
4
8
0
9
3
A
P
(A = 10)
Gewichtung: 4 3 2 7 6 5 4 3 2
36 + 21 + 2 + 56 + 18 + 0 + 16 + 0 + 6 =
155 : 11 = 14, Rest 1
11 - 1 = 10
Die Prüfziffer ist 7.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_56.py
- Öffentliche API:
  - @register("56") def validate_method_56(blz: str, account: str) -> bool
  - @register_generator("56") def generate_account_method_56(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_56.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
