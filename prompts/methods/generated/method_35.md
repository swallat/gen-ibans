# Implementierung Bundesbank Prüfziffermethode: 35

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 35") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 10
Die Kontonummer ist ggf. durch linksbündige Nullenauffüllung
10-stellig darzustellen. Die 10. Stelle der Kontonummer ist die
Prüfziffer. Die Stellen 1 bis 9 der Kontonummer werden von
rechts nach links mit den Ziffern 2, 3, 4, ff. multipliziert. Die
jeweiligen Produkte werden addiert. Die Summe der Produkte
ist durch 11 zu dividieren. Der verbleibende Rest ist die
Prüfziffer. Sollte jedoch der Rest 10 ergeben, so ist die
Kontonummer unabhängig vom eigentlichen Berechnungsergebnis
richtig, wenn die Ziffern an 10. und 9. Stelle identisch
sind.
Beispiel 1: P
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 0 0 0 0 1 0 8 4 4 3
Gewichtung: 10 9 8 7 6 5 4 3 2
0+ 0+ 0+ 0+ 6+ 0+ 32+ 12+ 8 = 58
58 : 11 = 5 Rest 3
3 ist die Prüfziffer
Beispiel 2: P
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 0 0 0 0 1 0 1 5 9 9
Gewichtung: 10 9 8 7 6 5 4 3 2
0+ 0+ 0+ 0+ 6+ 0+ 4+ 15+ 18 = 43:11 Rest 10
Testkontonummern: 0000108443, 0000107451, 0000102921,
0000102349, 0000101709, 0000101599
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_35.py
- Öffentliche API:
  - @register("35") def validate_method_35(blz: str, account: str) -> bool
  - @register_generator("35") def generate_account_method_35(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_35.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
