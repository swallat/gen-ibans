# Implementierung Bundesbank Prüfziffermethode: 17

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 17") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig mit folgendem Aufbau;
KSSSSSSPUU
K = Kontoartziffer
S = Stammnummer
P = Prüfziffer
U = Unterkontonummer
Die für die Berechnung relevante 6-stellige Stammnummer
(Kundennummer) befindet sich in den Stellen 2 bis 7 der
Kontonummer, die Prüfziffer in der Stelle 8. Die einzelnen
Stellen der Stammnummer (S) sind von links nach rechts mit
den Ziffern 1, 2, 1, 2, 1, 2 zu multiplizieren. Die jeweiligen
Produkte sind zu addieren, nachdem aus eventuell
zweistelligen Produkten der 2., 4. und 6. Stelle der
Stammnummer die Quersumme gebildet wurde. Von der
Summe ist der Wert "1" zu subtrahieren. Das Ergebnis ist
dann durch 11 zu dividieren. Der verbleibende Rest wird von
10 subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt nach
der Division durch 11 kein Rest, ist die Prüfziffer 0.
Beispiel:
Stellennr.: K S S S S S S P U U
Kontonummer: 0 4 4 6 7 8 6 0 4 0
Gewichtung: 1 2 1 2 1 2
4+ 8+ 6+ 5+ 8+ 3 = 34
Q Q
Q = Quersumme nur der jeweiligen Stellen lt. Beschreibung
34 - 1 = 33
33 : 11 = 3, Rest 0
0 = Prüfziffer
Testkontonummer: 0446786040
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_17.py
- Öffentliche API:
  - @register("17") def validate_method_17(blz: str, account: str) -> bool
  - @register_generator("17") def generate_account_method_17(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_17.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.