# Implementierung Bundesbank Prüfziffermethode: 71

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 71") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 6, 5, 4, 3, 2, 1
Die Kontonummer ist immer 10-stellig. Die Stellen 2 bis 7 sind
von links nach rechts mit den Ziffern 6, 5, 4, 3, 2, 1 zu
multiplizieren. Die Summe ist durch 11 zu dividieren. Der
verbleibende Rest wird vom Divisor (11) subtrahiert. Das
Ergebnis ist die Prüfziffer.
Ausnahmen:
Verbleibt nach der Division durch 11 kein Rest, ist die
Prüfziffer 0. Ergibt sich als Rest 1, entsteht bei der Subtraktion
11 - 1 = 10; die Zehnerstelle (1) ist dann die Prüfziffer.
Darstellung der Kontonummer:
S G G K K K K U U P
S = Sachgebiet
G = Geschäftsstelle
K = Kundennummer
U = Unternummer
P = Prüfziffer
Prüfzifferberechnung:
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 7 1 0 1 2 3 4 0 0 P
Gewichtung: 6 5 4 3 2 1
6 + 0 + 4 + 6 + 6 + 4 = 26
26 : 11 = 2, Rest 4
11 - 4 = 7
Die Prüfziffer ist in diesem Fall die 7 und die vollständige
Kontonummer lautet: 7 1 0 1 2 3 4 0 0 7
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_71.py
- Öffentliche API:
  - @register("71") def validate_method_71(blz: str, account: str) -> bool
  - @register_generator("71") def generate_account_method_71(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_71.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.