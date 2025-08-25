# Implementierung Bundesbank Prüfziffermethode: 57

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 57") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Die Berechnung der Prüfziffer und die möglichen Ergebnisse
richten sich nach dem jeweils bei der entsprechenden Variante
angegebenen Kontonummernkreis. Führt die Berechnung der
Prüfziffer nach der vorgegebenen Variante zu einem
Prüfzifferfehler, so ist die Kontonummer ungültig.
Kontonummern, die mit 00 beginnen sind immer als falsch zu
bewerten.
Variante 1:
Modulus 10, Gewichtung 1, 2, 1, 2, 1, 2, 1, 2, 1
Anzuwenden ist dieses Verfahren für Kontonummern, die mit
den folgenden Zahlen beginnen:
51, 55, 61, 64, 65, 66, 70, 73 bis 82, 88, 94 und 95
Die Stellen 1 bis 9 der Kontonummer sind von links beginnend
mit den Gewichten zu multiplizieren. Die 10. Stelle ist die
Prüfziffer. Die Berechnung und mögliche Ergebnisse
entsprechen der Methode 00.
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
Konto-Nr.: X X X X X X X X X P
Gewichtung 1 2 1 2 1 2 1 2 1
Ausnahme: Kontonummern, die mit den Zahlen 777777 oder
888888 beginnen sind immer als richtig (= Methode 09; keine
Prüfzifferberechnung) zu bewerten.
Variante 2:
Modulus 10, Gewichtung 1, 2, 1, 2, 1, 2, 1, 2, 1
Anzuwenden ist dieses Verfahren für Kontonummern, die mit
den folgenden Zahlen beginnen:
32 bis 39, 41 bis 49, 52, 53, 54, 56 bis 60, 62, 63, 67, 68, 69,
71, 72, 83 bis 87, 89, 90, 92, 93, 96, 97 und 98
Die Stellen 1, 2, 4, 5, 6, 7, 8, 9 und 10 der Kontonummer sind
von links beginnend mit den Gewichten zu multiplizieren. Die
3. Stelle ist die Prüfziffer. Die Berechnung und mögliche
Ergebnisse entsprechen der Methode 00.
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
Konto-Nr.: X X P X X X X X X X
Gewichtung 1 2 1 2 1 2 1 2 1
Variante 3:
Für die Kontonummern, die mit den folgenden Zahlen beginnen
gilt die Methode 09 (keine Prüfzifferberechnung):
40, 50, 91 und 99
Variante 4:
Kontonummern die mit 01 bis 31 beginnen haben an der dritten
bis vierten Stelle immer einen Wert zwischen 01 und 12 und an
der siebten bis neunten Stelle immer einen Wert kleiner 500.
Ausnahme: Die Kontonummer 0185125434 ist als richtig zu
bewerten.
Testkontonummern (richtig): 7500021766, 9400001734,
7800028282, 8100244186,
3251080371, 3891234567,
7777778800, 5001050352,
5045090090, 1909700805,
9322111030, 7400060823
Testkontonummern (falsch): 5302707782, 6412121212,
1813499124, 2206735010
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_57.py
- Öffentliche API:
  - @register("57") def validate_method_57(blz: str, account: str) -> bool
  - @register_generator("57") def generate_account_method_57(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_57.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.