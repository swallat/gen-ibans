# Implementierung Bundesbank Prüfziffermethode: C6

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C6") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig, ggf. ist die Kontonummer für
die Prüfzifferberechnung durch linksbündige Auffüllung mit
Nullen 10-stellig darzustellen. Die 10. Stelle der Kontonummer
ist die Prüfziffer.
Alle Kontonummern sind wie folgt zu prüfen:
Für die Berechnung der Prüfziffer werden die Stellen 2 bis 9
der Kontonummer von links verwendet. Diese Stellen sind
links um eine Zahl (Konstante) gemäß der folgenden Tabelle
zu ergänzen.
1. Stelle von links der 10-
stelligen Kontonummer
Zahl (Konstante)
0 4451970
1 4451981
2 4451992
3 4451993
4 4344992
5 4344990
6 4344991
7 5499570
8 4451994
9 5499579
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
Beispiel:
Kontonummer: 7000005024
Stellen 2 bis 9: 00000502
Ergänzt um Konstante (15 Stellen): 549957000000502
15 Stellen 5 4 9 9 5 7 0 0 0 0 0 0 5 0 2 4(=P)
Gewichtung 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
Produkt 10 4 18 9 10 7 0 0 0 0 0 0 10 0 4
Quersumme 1 4 9 9 1 7 0 0 0 0 0 0 1 0 4
Summe = 36
10 - 6 (Einerstelle) = 4 = Prüfziffer
Testkontonummern (richtig): 0000065516, 0203178249,
1031405209, 1082012201,
2003455189, 2004001016,
3110150986, 3068459207,
5035105948, 5286102149,
4012660028, 4100235626,
6028426119, 6861001755,
7008199027, 7002000023,
8526080015, 8711072264,
9000430223, 9000781153
Testkontonummern (falsch): 0525111212, 0091423614,
1082311275, 1000118821,
2004306518, 2016001206,
3462816371, 3622548632
4232300158, 4000456126,
5002684526, 5564123850,
6295473774, 6640806317,
7000062022, 7006003027,
8348300002, 8654216984,
9000641509, 9000260986
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C6.py
- Öffentliche API:
  - @register("C6") def validate_method_C6(blz: str, account: str) -> bool
  - @register_generator("C6") def generate_account_method_C6(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C6.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.