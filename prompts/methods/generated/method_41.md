# Implementierung Bundesbank Prüfziffermethode: 41

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 41") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2 (modifiziert)
Die Berechnung erfolgt wie bei Verfahren 00
Ausnahme:
Ist die 4. Stelle der Kontonummer (von links) = 9, so werden die
Stellen 1 bis 3 nicht in die Prüfzifferberechnung einbezogen.
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 4 0 1 9 1 1 0 0 0 8
Ktonr.
umgesetzt
0 0 0 9 1 1 0 0 0 8
Gewichtung: 1 2 1 2 1 2
9 + 2 + 1 + 0 + 0 + 0 = 12
10 - 2 = 8
8 = Prüfziffer
Testkontonummern: 4013410024, 4016660195, 0166805317
4019310079, 4019340829, 4019151002
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_41.py
- Öffentliche API:
  - @register("41") def validate_method_41(blz: str, account: str) -> bool
  - @register_generator("41") def generate_account_method_41(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_41.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.