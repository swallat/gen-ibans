# Implementierung Bundesbank Prüfziffermethode: 62

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 62") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Die beiden ersten und die beiden letzten Stellen sind nicht zu
berücksichtigen. Die Stellen drei bis sieben sind von rechts nach
links mit den Ziffern 2, 1, 2, 1, 2 zu multiplizieren. Aus
zweistelligen Einzelergebnissen ist eine Quersumme zu bilden.
Alle Ergebnisse sind dann zu addieren. Die Differenz zum
nächsten Zehner ergibt die Prüfziffer auf Stelle acht. Ist die
Differenz 10, ist die Prüfziffer 0.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 5 0 2 9 0 7 6 P 0 1
Gewichtung: 2 1 2 1 2
4 + 9 + 0 + 7 + 3 = 23
(Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert 10 - 3 = 7.
Die Prüfziffer ist in diesem Fall die 7 und die vollständige
Kontonummer lautet: 5 0 2 9 0 7 6 7 0 1
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_62.py
- Öffentliche API:
  - @register("62") def validate_method_62(blz: str, account: str) -> bool
  - @register_generator("62") def generate_account_method_62(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_62.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
