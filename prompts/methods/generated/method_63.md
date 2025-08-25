# Implementierung Bundesbank Prüfziffermethode: 63

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 63") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1
Aufbau der 9-stelligen Kontonummer (innerhalb des
zwischenbetrieblichen 10-stelligen Feldes)
Stelle 1 = gehört nicht zur Kontonummer, muss
daher »0« oder »blank« sein
2-7 = Grundnummer (Kundennummer; kann
auch führende Nullen enthalten)
8 = Prüfziffer
9-10 = Unterkontonummer
Die für die Berechnung relevante 6-stellige Grundnummer
(Kundennummer) befindet sich in den Stellen 2 bis 7, die
Prüfziffer in Stelle 8 der Kontonummer. Die zweistellige
Unterkontonummer (Stellen 9 und 10) ist nicht in das
Prüfzifferverfahren mit einzubeziehen. Die einzelnen Stellen der
Grundnummer sind von rechts nach links mit den Ziffern 2, 1, 2,
1, 2, 1 zu multiplizieren. Die jeweiligen Produkte werden addiert,
nachdem jeweils aus den zweistelligen Produkten die
Quersumme gebildet wurde (z. B. Produkt 16 = Quersumme 7).
Nach der Addition bleiben außer der Einerstelle alle anderen
Stellen unberücksichtigt. Die Einerstelle wird von dem Wert 10
subtrahiert. Das Ergebnis ist die Prüfziffer (Stelle 8). Hat die
Einerstelle den Wert »0«, ist die Prüfziffer »0«.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 0 1 2 3 4 5 6 P 0 0
Gewichtung: 1 2 1 2 1 2
1 + 4 + 3 + 8 + 5 + 3 = 24
(Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert (10 - 4 = 6).
Die Prüfziffer ist in dem Beispiel die 6 und die vollständige
Kontonummer lautet: 1 2 3 4 5 6 6 0 0
Ausnahmen:
Ist die Ziffer in Stelle 1 vor der sechsstelligen Grundnummer
nicht »0« (oder »blank«), ist das Ergebnis als falsch zu werten.
Ist die Unterkontonummer »00«, kann es vorkommen, dass sie
auf den Zahlungsverkehrsbelegen nicht angegeben ist, die
Kontonummer jedoch um führende Nullen ergänzt wurde. In
diesem Fall sind z. B. die Stellen 1 bis 3 »000« (oder »blank«),
die Prüfziffer ist an der Stelle 10 und die Berechnung ist wie
folgt durchzuführen:
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 0 0 0 1 2 3 4 5 6 6
Gewichtung: 0 0 0 1 2 1 2 1 2
1 + 4 + 3 + 8 + 5 + 3 = 24
(Q)
(Q = Quersumme)
10 - 4 = 6 Prüfziffer richtig
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_63.py
- Öffentliche API:
  - @register("63") def validate_method_63(blz: str, account: str) -> bool
  - @register_generator("63") def generate_account_method_63(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_63.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.