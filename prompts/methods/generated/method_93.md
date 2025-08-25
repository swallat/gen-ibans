# Implementierung Bundesbank Prüfziffermethode: 93

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 93") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Variante 1
Die Kontonummer ist 10-stellig. Die für die Berechnung
relevante Kundennummer (K) befindet sich entweder
a) in den Stellen 1 bis 5, die Prüfziffer in Stelle 6 der
Kontonummer oder
b) in den Stellen 5 bis 9, die Prüfziffer in Stelle 10 der
Kontonummer.
Die 2-stellige Unternummer (U) und die 2-stellige
Kontoartnummer (A) werden nicht in die Berechnung
einbezogen. Sie befinden sich im Fall a) an Stelle 7 bis 10
(UUAA). Im Fall b) befinden sie sich an Stelle 1 bis 4 und
müssen "0000" lauten. Die 5-stellige Kundennummer wird von
rechts nach links mit den Gewichten multipliziert. Die weitere
Berechnung und die möglichen Ergebnisse entsprechen dem
Verfahren 06.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: Fall a) K K K K K P U U A A
Gewichtung: 6 5 4 3 2
Kontonr.: Fall b) 0 0 0 0 K K K K K P
Gewichtung: 6 5 4 3 2
Führt die Berechnung nach Variante 1 zu einem Prüfzifferfehler,
so ist die Berechnung nach Variante 2 vorzunehmen.
Variante 2
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Das Berechnungsverfahren entspricht Variante 1. Die Summe
der Produkte ist jedoch durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist dann die Prüfziffer. Verbleibt nach der Division
durch 7 kein Rest, lautet die Prüfziffer 0.
Testkontonummern:
Modulus 11: 6714790000 bzw. 0000671479
Modulus 7: 1277830000 bzw. 0000127783
1277910000 bzw. 0000127791
Modulus 11 und 7: 3067540000 bzw. 0000306754
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_93.py
- Öffentliche API:
  - @register("93") def validate_method_93(blz: str, account: str) -> bool
  - @register_generator("93") def generate_account_method_93(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_93.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.