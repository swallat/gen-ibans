# Implementierung Bundesbank Prüfziffermethode: D1

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D1") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig, ggf. ist die Kontonummer für
die Prüfzifferberechnung durch linksbündige Auffüllung mit
Nullen 10-stellig darzustellen. Die 10. Stelle der Kontonummer
ist die Prüfziffer.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 8 beinhalten sind falsch.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer einen der Werte 0, 1, 2, 3, 4, 5, 6, 7 oder 9
beinhalten sind wie folgt zu prüfen:
Für die Berechnung der Prüfziffer werden die Stellen 2 bis 9
der Kontonummer von links verwendet. Diese Stellen sind
links um eine Zahl (Konstante) gemäß der folgenden Tabelle
zu ergänzen.
1. Stelle von links der 10-
stelligen Kontonummer
Zahl (Konstante)
0 4363380
1 4363381
2 4363382
3 4363383
4 4363384
5 4363385
6 4363386
7 4363387
9 4363389
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
Beispiel:
Kontonummer: 3002000027
Stellen 2 bis 9: 00200002
Ergänzt um Konstante (15 Stellen): 436338300200002
Summe = 43
10 - 3 (Einerstelle) = 7 = Prüfziffer
Testkontonummern (richtig): 0082012203, 1452683581,
2129642505, 3002000027,
4230001407, 5000065514,
6001526215, 7126502149,
9000430223
Testkontonummern (falsch): 0000260986, 1062813622,
2256412314, 3012084101,
4006003027, 5814500990,
6128462594, 7000062035,
8003306026, 9000641509
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D1.py
- Öffentliche API:
  - @register("D1") def validate_method_D1(blz: str, account: str) -> bool
  - @register_generator("D1") def generate_account_method_D1(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D1.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.