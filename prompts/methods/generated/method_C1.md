# Implementierung Bundesbank Prüfziffermethode: C1

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C1") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Kontonummern, die an der 1. Stelle der 10-stelligen
Kontonummer einen Wert ungleich „5“ beinhalten, sind nach
der Variante 1 zu prüfen. Kontonummern, die an der 1. Stelle
der 10-stelligen Kontonummer den Wert „5“ beinhalten, sind
nach der Variante 2 zu prüfen.
Variante 1:
Modulus 11, Gewichtung 1, 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 17. Führt die Berechnung nach der Variante 1 zu
einem Prüfzifferfehler, so ist die Kontonummer falsch.
Testkontonummern (richtig): 0446786040, 0478046940,
0701625830, 0701625840,
0882095630
Testkontonummern (falsch): 0446786240, 0478046340,
0701625730, 0701625440,
0882095130
Variante 2:
Modulus 11, Gewichtung 1, 2, 1, 2, 1, 2
Die Kontonummer ist 10-stellig mit folgendem Aufbau:
KNNNNNNNNP
K = Kontoartziffer
N = laufende Nummer
P = Prüfziffer
Für die Berechnung fließen die Stellen 1 bis 9 ein. Stelle 10
ist die ermittelte Prüfziffer. Die Stellen 1 bis 9 sind von links
nach rechts mit den Ziffern 1, 2, 1, 2, 1, 2, 1, 2, 1 zu
multiplizieren. Die jeweiligen Produkte sind zu addieren,
nachdem aus eventuell zweistelligen Produkten der 2., 4., 6.
und 8. Stelle die Quersumme gebildet wurde. Von der
Summe ist der Wert „1“ zu subtrahieren. Das Ergebnis ist
dann durch 11 zu dividieren. Der verbleibende Rest wird von
10 subtrahiert. Das Ergebnis ist die Prüfziffer. Verbleibt nach
der Division durch 11 kein Rest, ist die Prüfziffer 0.
Beispiel:
Stellen-Nr.: K N N N N N N N N P
Konto-Nr.: 5 4 3 2 1 1 2 3 4 9
Gewichtung: 1 2 1 2 1 2 1 2 1
5 + 8 + 3 + 4 + 1 + 2 + 2 + 6 + 4 = 35
35 - 1 = 34
34 : 11 = 3, Rest 1
10 - 1 = 9 (Prüfziffer)
Testkontonummern richtig: 5432112349, 5543223456,
5654334563, 5765445670,
5876556788
Testkontonummern falsch: 5432112341, 5543223458,
5654334565, 5765445672,
5876556780
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C1.py
- Öffentliche API:
  - @register("C1") def validate_method_C1(blz: str, account: str) -> bool
  - @register_generator("C1") def generate_account_method_C1(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C1.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.