# Implementierung Bundesbank Prüfziffermethode: 06

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 06") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7 (modifiziert)
Die einzelnen Stellen der Kontonummer sind von rechts nach
links mit den Ziffern 2, 3, 4, 5, 6, 7, 2, 3 ff. zu multiplizieren.
Die jeweiligen Produkte werden addiert. Die Summe ist durch
11 zu dividieren. Der verbleibende Rest wird vom Divisor (11)
subtrahiert. Das Ergebnis ist die Prüfziffer. Ergibt sich als
Rest 1, findet von dem Rechenergebnis 10 nur die Einerstelle
(0) als Prüfziffer Verwendung. Verbleibt nach der Division
durch 11 kein Rest, dann ist auch die Prüfziffer 0. Die
Stelle 10 der Kontonummer ist die Prüfziffer.
Testkontonummern: 94012341, 5073321010
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_06.py
- Öffentliche API:
  - @register("06") def validate_method_06(blz: str, account: str) -> bool
  - @register_generator("06") def generate_account_method_06(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_06.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.