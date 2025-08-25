# Implementierung Bundesbank Prüfziffermethode: D4

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D4") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig, ggf. ist die Kontonummer für
die Prüfziffernberechnung durch linksbündiges Auffüllung mit
Nullen 10-stellig darzustellen. Die 10. Stelle der Kontonummer
ist die Prüfziffer.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 0 beinhalten, sind falsch.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer einen der Werte 1, 2, 3, 4, 5, 6, 7, 8 oder 9
beinhalten, sind wie folgt zu prüfen:
Für die Berechnung der Prüfziffer werden die Stellen 1 bis 9
der Kontonummer von links verwendet. Diese Stellen sind
links um die Zahl (Konstante) „428259“ zu ergänzen.
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
Beispiel:
Kontonummer: 3000005012
Stellen 1 bis 9: 300000501
Ergänzt um Konstante (15 Stellen): 428259300000501
Summe = 38
10 - 8 (Einerstelle) = 2 = Prüfziffer
Testkontonummern (richtig): 1112048219, 2024601814,
3000005012, 4143406984,
5926485111, 6286304975,
7900256617, 8102228628,
9002364588
Testkontonummern (falsch): 0359432843, 1000062023,
2204271250, 3051681017,
4000123456, 5212744564,
6286420010, 7859103459,
8003306026, 9916524534
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D4.py
- Öffentliche API:
  - @register("D4") def validate_method_D4(blz: str, account: str) -> bool
  - @register_generator("D4") def generate_account_method_D4(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D4.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.