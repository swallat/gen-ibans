# Implementierung Bundesbank Prüfziffermethode: E2

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode E2") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2,1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig, ggf. ist die Kontonummer für
die Prüfzifferberechnung durch linksbündige Auffüllung mit
Nullen 10-stellig darzustellen. Die 10. Stelle der Kontonummer
ist die Prüfziffer.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 6, 7, 8 oder 9 beinhalten, sind falsch.
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 0, 1, 2, 3, 4 oder 5 beinhalten, sind
wie folgt zu prüfen:
Für die Berechnung der Prüfziffer werden die Stellen 2 bis 9
der Kontonummer von links verwendet. Diese Stellen sind
links um eine Zahl (Konstante) gemäß der folgenden Tabelle
zu ergänzen.
1. Stelle von links der 10-
stelligen Kontonummer
Zahl (Konstante)
0 4383200
1 4383201
2 4383202
3 4383203
4 4383204
5 4383205
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
Beispiel:
Kontonummer: 3000260983
Stellen 2 bis 9: 00026098
Ergänzt um Konstante (15 Stellen): 438320300026098
Summe = 57
10 - 7 (Einerstelle) = 3 = Prüfziffer
Testkontonummern (richtig): 0003831745, 0051330335,
1730773457, 1987654327,
2012345675, 2220467998,
3190519693, 3011219713,
4131220086, 4110919419,
5000083836, 5069696965,
Testkontonummern (falsch): 0121314151, 0036958466,
1000174716, 1975312468,
2260519349, 2004002175,
3780024149, 3015024274,
4968745438, 4005012150,
5000137454, 5221398871,
6221398879, 6742185327,
7793867322, 7900695413,
8001256238, 8303808900,
9703805111, 9006126433.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_E2.py
- Öffentliche API:
  - @register("E2") def validate_method_E2(blz: str, account: str) -> bool
  - @register_generator("E2") def generate_account_method_E2(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_E2.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
