# Implementierung Bundesbank Prüfziffermethode: B2

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B2") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Variante 1:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 2
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 0 bis 7 beinhalten, sind nach der
Methode 02 zu rechnen.
Testkontonummern (richtig): 0020012357, 0080012345,
0926801910, 1002345674
Testkontonummern (falsch): 0020012399, 0080012347,
0080012370, 0932100027,
3310123454
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Kontonummern, die an der 1. Stelle von links der 10-stelligen
Kontonummer den Wert 8 oder 9 beinhalten, sind nach der
Methode 00 zu rechnen.
Testkontonummern (richtig): 8000990054, 9000481805
Testkontonummern (falsch): 8000990057, 8011000126,
9000481800, 9980480111
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B2.py
- Öffentliche API:
  - @register("B2") def validate_method_B2(blz: str, account: str) -> bool
  - @register_generator("B2") def generate_account_method_B2(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B2.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.