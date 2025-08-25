# Implementierung Bundesbank Prüfziffermethode: 61

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 61") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2
Darstellung der Kontonummer:
B B B S S S S P A U (10-stellig)
B = Betriebsstellennummer
S = Stammnummer
P = Prüfziffer
A = Artziffer
U = Unternummer
Ausnahme:
Ist die Artziffer (neunte Stelle der Kontonummer) eine 8, so
werden die neunte und zehnte Stelle der Kontonummer in die
Prüfzifferermittlung einbezogen.
Die Berechnung erfolgt dann über Betriebsstellennummer,
Stammnummer, Artziffer und Unternummer mit der
Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2.
Beispiel 1:
Stellennr.: B B B S S S S P A U
Kontonr.: 2 0 6 3 0 9 9 0 0
Gewichtung: 2 1 2 1 2 1 2
4 + 0 + 3 + 3 + 0 + 9 + 9 = 28
(Q) (Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert (10 - 8 = 2).
Die Prüfziffer ist in diesem Fall die 2 und die vollständige
Kontonummer lautet: 2 0 6 3 0 9 9 2 0 0
Beispiel 2:
Stellennr.: B B B S S S S P A U
Kontonr.: 0 2 6 0 7 6 0 8 1
Gewichtung: 2 1 2 1 2 1 2 1 2
0 + 2 + 3 + 0 + 5 + 6 + 0 + 8 + 2 = 26
(Q) (Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert (10 - 6 = 4). Die
Prüfziffer ist in diesem Fall die 4 und die vollständige
Kontonummer lautet: 0 2 6 0 7 6 0 4 8 1
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_61.py
- Öffentliche API:
  - @register("61") def validate_method_61(blz: str, account: str) -> bool
  - @register_generator("61") def generate_account_method_61(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_61.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
