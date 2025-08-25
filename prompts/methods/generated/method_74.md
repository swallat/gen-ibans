# Implementierung Bundesbank Prüfziffermethode: 74

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 74") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2 ff.
Die Kontonummer (2- bis 10-stellig) ist durch linksbündige
Nullenauffüllung 10-stellig darzustellen. Die 10. Stelle ist per
Definition die Prüfziffer.
Variante 1:
Die für die Berechnung relevanten Stellen werden von rechts
nach links mit den Ziffern 2, 1, 2, 1, 2 ff. multipliziert. Die
weitere Berechnung und die Ergebnisse entsprechen dem
Verfahren 00.
Ausnahme:
Bei 6-stelligen Kontonummern ist folgende Besonderheit zu
beachten:
Ergibt die erste Berechnung der Prüfziffer nach dem
Verfahren 00 einen Prüfzifferfehler, so ist eine weitere
Berechnung vorzunehmen. Hierbei ist die Summe der
Produkte auf die nächste Halbdekade hochzurechnen. Die
Differenz ist die Prüfziffer.
Beispiel:
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: 2 3 9 3 1 P
Gewichtung: 2 1 2 1 2
4 + 3 + 9 + 3 + 2 = 21
(Q)
(Q = Quersumme)
1. Berechnung (Verfahren 00) 10 - 1 = 9
2. Berechnung 21 + 4 = 25 (nächste
Halbdekade)
In diesem Fall kann die Prüfziffer 4 oder 9 lauten.
Testkontonummern (richtig): 1016, 26260, 242243, 242248,
18002113, 1821200043
Testkontonummern (falsch): 1011, 26265, 18002118,
6160000024
Führt die Berechnung nach Variante 1 zu einem
Prüfzifferfehler, so ist nach Variante 2 zu prüfen.
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2, 3, 4
Gewichtung und Berechnung erfolgen nach der Methode 04.
Testkontonummer (richtig): 1015, 26263, 242241, 18002116,
1821200047, 3456789012
Testkontonummern (falsch) 1011, 26265, 242249,
18002118,123456789
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_74.py
- Öffentliche API:
  - @register("74") def validate_method_74(blz: str, account: str) -> bool
  - @register_generator("74") def generate_account_method_74(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_74.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.