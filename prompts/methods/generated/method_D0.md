# Implementierung Bundesbank Prüfziffermethode: D0

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D0") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Kontonummern, die an der 1. und 2. Stelle der 10-stelligen
Kontonummer einen Wert ungleich „57“ beinhalten, sind nach
der Variante 1 zu prüfen. Kontonummern, die an der 1. und 2.
Stelle der 10-stelligen Kontonummer den Wert „57“
beinhalten, sind nach der Variante 2 zu prüfen.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 3 (modifiziert)
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 20. Führt die Berechnung nach der Variante 1 zu
einem Prüfzifferfehler, so ist die Kontonummer falsch.
Testkontonummern (richtig): 6100272324, 6100273479
Testkontonummern (falsch): 6100272885, 6100273377,
6100274012
Variante 2:
Für den Kontonummernkreis 5700000000 bis 5799999999 gilt
die Methode 09 (keine Prüfzifferberechnung, alle
Kontonummern sind als richtig zu werten).
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D0.py
- Öffentliche API:
  - @register("D0") def validate_method_D0(blz: str, account: str) -> bool
  - @register_generator("D0") def generate_account_method_D0(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D0.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.