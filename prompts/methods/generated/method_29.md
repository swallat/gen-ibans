# Implementierung Bundesbank Prüfziffermethode: 29

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 29") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, iterierte Transformation
Die einzelnen Ziffern der Kontonummer werden über eine
Tabelle in andere Werte transformiert. Jeder einzelnen Stelle
der Kontonummer ist hierzu eine der Zeilen 1 bis 4 der
Transformationstabelle fest zugeordnet. Die
Transformationswerte werden addiert. Die Einerstelle der
Summe wird von 10 subtrahiert. Das Ergebnis ist die
Prüfziffer. (Ist das Ergebnis = 10, ist die Prüfziffer = 0).
Beispiel:
Kontonummer: 3 1 4 5 8 6 3 0 2 P (P = Prüfziffer)
Die Kontonummer ist 10-stellig. Die 10. Stelle ist die
Prüfziffer.
Zugeordnete Zeile der
Transformationstabelle: 1 4 3 2 1 4 3 2 1
Transformationstabelle:
Ziffer: 0 1 2 3 4 5 6 7 8 9
Zeile 1: 0 1 5 9 3 7 4 8 2 6
Zeile 2: 0 1 7 6 9 8 3 2 5 4
Zeile 3: 0 1 8 4 6 2 9 5 7 3
Zeile 4: 0 1 2 3 4 5 6 7 8 9
Transformation
von rechts nach
links: Ziffer 2 wird 5 (Tabelle: Zeile 1)
" 0 wird 0 (" " 2)
" 3 wird 4 (" " 3)
" 6 wird 6 (" " 4)
" 8 wird 2 (" " 1)
" 5 wird 8 (" " 2)
" 4 wird 6 (" " 3)
" 1 wird 1 (" " 4)
" 3 wird 9 (" " 1)
___
Summe: 41 (Einerstelle = 1)
Subtraktion : (10 - 1) = 9 (= Prüfziffer)
Kontonummer mit Prüfziffer: 3 1 4 5 8 6 3 0 2 9
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_29.py
- Öffentliche API:
  - @register("29") def validate_method_29(blz: str, account: str) -> bool
  - @register_generator("29") def generate_account_method_29(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_29.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.