# Implementierung Bundesbank Prüfziffermethode: 54

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 54") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2
Die Kontonummer ist 10-stellig, wobei die Stellen 1 u. 2
generell mit 49 belegt sind. Die einzelnen Stellen der
Kontonummer sind von rechts nach links mit den Ziffern 2, 3, 4,
5, 6, 7, 2 zu multiplizieren. Die jeweiligen Produkte werden addiert.
Die Summe ist durch 11 zu dividieren. Der verbleibende
Rest wird vom Divisor (11) subtrahiert. Das Ergebnis ist die
Prüfziffer. Ergibt sich als Rest 0 oder 1, ist die Prüfziffer
zweistellig und kann nicht verwendet werden. Die
Kontonummer ist dann nicht verwendbar.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 4 9 K K K K K K K P
Gewichtung: 2 7 6 5 4 3 2
Testkontonummern: (49) 64137395, (49) 00010987
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_54.py
- Öffentliche API:
  - @register("54") def validate_method_54(blz: str, account: str) -> bool
  - @register_generator("54") def generate_account_method_54(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_54.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
