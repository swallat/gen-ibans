# Implementierung Bundesbank Prüfziffermethode: 70

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 70") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Kontonummer ist 10-stellig. Die einzelnen Stellen der
Kontonummer sind von rechts nach links mit den Ziffern 2, 3, 4,
5, 6, 7, 2, 3, 4 zu multiplizieren.
Die Berechnung erfolgt wie bei Verfahren 06.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x x x x P
Gewichtung: 4 3 2 7 6 5 4 3 2
Ausnahme:
Ist die 4. Stelle der Kontonummer = 5 oder die 4. bis 5. Stelle der
Kontonummer = 69, so werden die Stellen 1 bis 3 nicht in die
Prüfzifferermittlung einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x 5 x x x x x P
Kontonr.: x x x 6 9 x x x x P
Gewichtung: 7 6 5 4 3 2
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_70.py
- Öffentliche API:
  - @register("70") def validate_method_70(blz: str, account: str) -> bool
  - @register_generator("70") def generate_account_method_70(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_70.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.