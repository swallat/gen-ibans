# Implementierung Bundesbank Prüfziffermethode: 73

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 73") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist durch linksbündiges Auffüllen mit Nullen
10-stellig darzustellen. Die 10. Stelle der Kontonummer ist die
Prüfziffer.
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1
Die Stellen 4 bis 9 der Kontonummer werden von rechts nach
links mit den Ziffern 2, 1, 2, 1, 2, 1 multipliziert. Die Berechnung
und Ergebnisse entsprechen dem Verfahren 00.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: X X X X X X X X X P
Gewichtung: 1 2 1 2 1 2
Testkontonummern: richtig: 0003503398, 0001340967
falsch: 0003503391, 0001340966
Führt die Berechnung nach Variante 1 zu einem Prüfzifferfehler,
ist eine weitere Berechnung nach Variante 2 vorzunehmen:
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Das Berechnungsverfahren entspricht Variante 1, es ist jedoch
zu beachten, dass nur die Stellen 5 bis 9 in das
Prüfziffernberechnungsverfahren einbezogen werden.
Testkontonummern: richtig: 0003503391, 0001340968
falsch: 0003503392, 0001340966
Führt die Berechnung auch nach Variante 2 zu einem
Prüfzifferfehler, ist die Berechnung nach Variante 3
vorzunehmen:
Variante 3
Modulus 7, Gewichtung 2, 1, 2, 1, 2
Das Berechnungsverfahren entspricht Variante 2. Die Summe
der Produkt-Quersummen ist jedoch durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das Ergebnis
ist die Prüfziffer. Verbleibt nach der Division kein Rest, ist die
Prüfziffer = 0
Testkontonummern: richtig: 0003503392, 0001340966, 123456
falsch: 121212, 987654321
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die 3.
Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung gemäß der Ausnahme in Methode 51 mit den
gleichen Ergebnissen und Testkontonummern.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_73.py
- Öffentliche API:
  - @register("73") def validate_method_73(blz: str, account: str) -> bool
  - @register_generator("73") def generate_account_method_73(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_73.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.