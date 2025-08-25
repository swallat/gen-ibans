# Implementierung Bundesbank Prüfziffermethode: 51

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 51") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist durch linksbündige Nullenauffüllung
immer 10-stellig darzustellen. Die für die Berechnung
relevante Kundennummer (K) befindet sich bei den
Methoden A und C in den Stellen 4 bis 9 der Kontonummer
und bei den Methoden B und D in den Stellen 5 bis 9, die
Prüfziffer in Stelle 10 der Kontonummer.
Methode A:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 7 6 5 4 3 2
Testkontonummern richtig: 0001156071, 0001156136
Testkontonummern falsch: 0001156078, 0000156079
Ergibt die Berechnung der Prüfziffer nach der Methode A
einen Prüfzifferfehler, ist eine weitere Berechnung mit der
Methode B vorzunehmen.
Methode B:
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 33.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Testkontonummern richtig: 0001156078, 0001234567
Testkontonummern falsch: 0001234566, 0012345678
Ergibt auch die Berechnung der Prüfziffer nach Methode B
einen Prüfzifferfehler, ist eine weitere Berechnung mit der
Methode C vorzunehmen.
Methode C:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1
Die Berechnung und die möglichen Ergebnisse entsprechen
dem Verfahren 00; es ist jedoch zu beachten, dass nur die
Stellen 4 bis 9 in das Prüfzifferberechnungsverfahren
einbezogen werden
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 1 2 1 2 1 2
Testkontonummern richtig: 340968, 201178, 1009588
Testkontonummern falsch: 0023456783, 0076543211
Ergibt auch die Berechnung der Prüfziffer nach Methode C
einen Prüfzifferfehler, ist eine weitere Berechnung mit der
Methode D vorzunehmen.
Methode D:
Kontonummern, die bis zur Methode D gelangen und in der
10. Stelle eine 7, 8 oder 9 haben, sind ungültig.
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Das Berechnungsverfahren entspricht Methode B.
Die Summe der Produkte ist jedoch durch 7 zu dividieren.
Der verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer. Verbleibt kein Rest, ist die
Prüfziffer 0.
Testkontonummern richtig: 0000156071, 101356073
Testkontonummern falsch: 0123412345, 67493647
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung wie folgt:
Variante 1 zur Ausnahme
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Die für die Berechnung relevanten Stellen 3 bis 9 werden von
rechts nach links mit den Ziffern 2, 3, 4, 5, 6, 7, 8 multipliziert.
Die Produkte werden addiert. Die Summe ist durch 11 zu
dividieren. Der verbleibende Rest wird vom Divisor (11)
subtrahiert. Das Ergebnis ist die Prüfziffer. Ergibt sich als
Rest 1 oder 0, ist die Prüfziffer 0.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A=10)
Kontonr.; x x 9 x x x x x x P
Gewichtung: 8 7 6 5 4 3 2
Testkontonummern
richtig: 0199100002, 0099100010, 2599100002
falsch: 0199100004, 2599100003, 0099345678
Führt die Variante 1 zur Ausnahme zu einem Prüfzifferfehler,
ist eine weitere Berechnung nach der Variante 2
vorzunehmen.
Variante 2 zur Ausnahme
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 10
Berechnung und Ergebnisse entsprechen der Variante 1 zur
Ausnahme.
Testkontonummern
richtig: 0199100004, 2599100003, 3199204090
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_51.py
- Öffentliche API:
  - @register("51") def validate_method_51(blz: str, account: str) -> bool
  - @register_generator("51") def generate_account_method_51(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_51.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
