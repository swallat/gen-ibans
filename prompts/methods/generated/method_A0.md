# Implementierung Bundesbank Prüfziffermethode: A0

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode A0") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 4, 8, 5, 10, 0, 0, 0, 0
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen. Die
Stelle 10 ist die Prüfziffer. Die einzelnen Stellen der
Kontonummer (ohne Prüfziffer) sind von rechts nach links mit
dem zugehörigen Gewicht (2, 4, 8, 5, 10, 0, 0, 0, 0) zu
multiplizieren. Die Produkte werden addiert. Das Ergebnis ist
durch 11 zu dividieren. Ergibt sich nach der Division ein Rest
von 0 oder 1, so ist die Prüfziffer 0. Ansonsten ist der Rest
vom Divisor (11) zu subtrahieren. Das Ergebnis ist die
Prüfziffer.
Ausnahme: 3-stellige Kontonummern bzw. Kontonummern,
deren Stellen 1 bis 7 = 0 sind, enthalten keine Prüfziffer und
sind als richtig anzusehen.
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: x x x x x x x x x P
Gewichtung: 0 0 0 0 10 5 8 4 2
Summe der Produkte dividiert durch 11 = x, Rest
Rest = 0 oder 1 Prüfziffer = 0
Rest = 2 bis 10 Prüfziffer = 11 – Rest
Beispiel:
Kontonr.: 0 5 2 1 0 0 3 2 8 7
Gewichtung: 0 0 0 0 10 5 8 4 2 P
Produkt: 0+ 0+ 0+ 0+ 0+ 0+ 24+ 8+ 16 =48
48 : 11 = 4, Rest 4
11 - 4 = 7 = P
Testkontonummern:
521003287, 54500, 3287, 18761, 28290
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_A0.py
- Öffentliche API:
  - @register("A0") def validate_method_A0(blz: str, account: str) -> bool
  - @register_generator("A0") def generate_account_method_A0(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_A0.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
