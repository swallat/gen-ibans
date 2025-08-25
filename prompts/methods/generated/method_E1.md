# Implementierung Bundesbank Prüfziffermethode: E1

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode E1") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 1, 2, 3, 4, 5, 6, 11, 10, 9
Die Kontonummer sowohl für Kontokorrentkonten als auch
für Sparkonten ist 9-stellig und für die Prüfzifferberechnung
durch linksbündige Auffüllung mit einer Null 10-stellig
darzustellen. Die 10. Stelle der Kontonummer ist die
Prüfziffer.
Vor der Berechnung der Prüfziffer sind die einzelnen Stellen
der Kontonummer durch folgende Werte (ASCII Wert) zu
ersetzen:
Ziffern der
Kontonummer
0 1 2 3 4 5 6 7 8 9
ASCII-Wert 48 49 50 51 52 53 54 55 56 57
Die einzelnen ASCII-Werte sind von rechts nach links mit
den Ziffern 1, 2, 3, 4, 5, 6, 11, 10, 9 zu multiplizieren. Die
jeweiligen Produkte werden addiert. Die Summe ist durch 11
zu dividieren. Der verbleibende Rest ist die Prüfziffer.
Verbleibt nach der Division durch 11 kein Rest, ist die
Prüfziffer 0. Ergibt sich ein Rest 10, ist die Kontonummer
falsch.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 0 1 3 4 2 1 1 9 0 9
ASCII-Wert 48 49 51 52 50 49 49 57 48 P
Gewichtung 9 10 11 6 5 4 3 2 1
Resultat 432 490 561 312 250 196 147 114 48
Summe = 2550 : 11 = 231; Rest = 9 = Prüfziffer
Testkontonummern (richtig): 0100041104, 0100054106,
0200025107
Testkontonummern (falsch): 0150013107, 0200035101,
0081313890, 4268550840,
0987402008
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_E1.py
- Öffentliche API:
  - @register("E1") def validate_method_E1(blz: str, account: str) -> bool
  - @register_generator("E1") def generate_account_method_E1(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_E1.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
