# Implementierung Bundesbank Prüfziffermethode: 91

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 91") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
1. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
2. Modulus 11, Gewichtung 7, 6, 5, 4, 3, 2
3. Modulus 11, Gewichtung 2, 3, 4, 0, 5, 6, 7, 8, 9, A (A = 10)
4. Modulus 11, Gewichtung 2, 4, 8, 5, 10, 9
Gemeinsame Hinweise für die Berechnungsvarianten 1 bis 4:
Die Kontonummer ist immer 10-stellig. Die einzelnen Stellen
der Kontonummer werden von links nach rechts von 1 bis 10
durchnummeriert. Die Stelle 7 der Kontonummer ist die
Prüfziffer. Die für die Berechnung relevanten Kundennummern
(K) sind von rechts nach links mit den jeweiligen Gewichten zu
multiplizieren. Die restliche Berechnung und möglichen
Ergebnisse entsprechen dem Verfahren 06.
Ergibt die Berechnung nach der ersten beschriebenen Variante
einen Prüfzifferfehler, so sind in der angegebenen Reihenfolge
weitere Berechnungen mit den anderen Varianten
vorzunehmen, bis die Berechnung keinen Prüfzifferfehler mehr
ergibt. Kontonummern, die endgültig nicht zu einem richtigen
Ergebnis führen, sind nicht prüfbar.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Stellen 8 bis 10 werden nicht in die Berechnung
einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: K K K K K K P x x x
Gewichtung: 7 6 5 4 3 2
Testkontonummern (richtig): 2974118000, 5281741000,
9952810000
Testkontonummern (falsch): 8840017000, 8840023000,
8840041000
Variante 2:
Modulus 11, Gewichtung 7, 6, 5, 4, 3, 2
Die Stellen 8 bis 10 werden nicht in die Berechnung
einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: K K K K K K P x x x
Gewichtung: 2 3 4 5 6 7
Testkontonummern (richtig): 2974117000, 5281770000,
9952812000
Testkontonummern (falsch): 8840014000, 8840026000,
8840045000
Variante 3:
Modulus 11, Gewichtung 2, 3, 4, 0, 5, 6, 7, 8, 9, A (A = 10)
Die Stellen 1 bis 10 werden in die Berechnung einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A= 10)
Kontonr.: K K K K K K P x x x
Gewichtung: 10 9 8 7 6 5 0 4 3 2
Testkontonummern (richtig): 8840019000, 8840050000,
8840087000, 8840045000
Testkontonummern (falsch): 8840011000, 8840025000,
8840062000
Variante 4:
Modulus 11, Gewichtung 2, 4, 8, 5, A, 9 (A = 10)
Die Stellen 8 bis 10 werden nicht in die Berechnung einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A=10)
Kontonr.: K K K K K K P x x x
Gewichtung: 9 10 5 8 4 2
Testkontonummern (richtig): 8840012000, 8840055000,
8840080000
Testkontonummern (falsch): 8840010000, 8840057000
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_91.py
- Öffentliche API:
  - @register("91") def validate_method_91(blz: str, account: str) -> bool
  - @register_generator("91") def generate_account_method_91(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_91.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
