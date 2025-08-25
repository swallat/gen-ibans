# Implementierung Bundesbank Prüfziffermethode: 83

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 83") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
1. Kundenkonten
A. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
B. Modulus 11, Gewichtung 2, 3, 4, 5, 6
C. Modulus 7, Gewichtung 2, 3, 4, 5, 6
Gemeinsame Anmerkungen für die Berechnungsverfahren
Die Kontonummer ist immer 10-stellig. Die für die Berechnung
relevante Kundennummer (K) befindet sich bei der Methode A
in den Stellen 4 bis 9 der Kontonummer und bei den
Methoden B + C in den Stellen 5 - 9, die Prüfziffer in Stelle 10
der Kontonummer.
Ergibt die erste Berechnung der Prüfziffer nach dem
Verfahren A einen Prüfzifferfehler, so sind weitere
Berechnungen mit den anderen Methoden vorzunehmen.
Kontonummern, die nach Durchführung aller
3 Berechnungsmethoden nicht zu einem richtigen Ergebnis
führen, sind nicht prüfbar.
Methode A:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Berechnung und möglichen Ergebnisse entsprechen dem
Verfahren 32.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x K K K K K K P
Gewichtung: 7 6 5 4 3 2
Testkontonummern: 0001156071, 0001156136
Methode B:
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Die Berechnung und möglichen Ergebnisse entsprechen dem
Verfahren 33.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x K K K K K P
Gewichtung: 6 5 4 3 2
Testkontonummer: 0000156078
Methode C:
Kontonummern, die bis zur Methode C gelangen und in der
10. Stelle eine 7, 8 oder 9 haben, sind ungültig.
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Das Berechnungsverfahren entspricht Methode B.
Die Summe der Produkte ist jedoch durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer. Verbleibt kein Rest, ist die
Prüfziffer 0.
Testkontonummer: 0000156071
2. Sachkonten
83 Berechnungsmethode:
A. Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Die Sachkontonummer ist immer 10-stellig.
Die für die Berechnung relevante Sachkontenstammnummer
(S) befindet sich in den Stellen 3 bis 9 der Kontonummer,
wobei die 3. und 4. Stelle immer jeweils 9 sein müssen; die
Prüfziffer ist in Stelle 10 der Sachkontonummer.
Führt die Berechnung nicht zu einem richtigen Ergebnis, ist
die Nummer nicht prüfbar.
Methode A:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Berechnung:
Die einzelnen Stellen der Sachkontonummern sind von rechts
nach links mit den Ziffern 2, 3, 4, 5, 6, 7, 8 zu multiplizieren.
Die jeweiligen Produkte werden addiert.
Die Summe ist durch 11 zu dividieren. Der verbleibende Rest
wird vom Divisor (11) subtrahiert. Das Ergebnis ist die
Prüfziffer.
Verbleibt nach der Division durch die 11 kein Rest, ist die
Prüfziffer "0".
Das Rechenergebnis "10" ist nicht verwendbar und muss auf
eine Stelle reduziert werden. Die rechte Stelle Null findet als
Prüfziffer Verwendung.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x S S S S S S S P
Gewichtung: 8 7 6 5 4 3 2
Testkontonummer: 0099100002
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_83.py
- Öffentliche API:
  - @register("83") def validate_method_83(blz: str, account: str) -> bool
  - @register_generator("83") def generate_account_method_83(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_83.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
