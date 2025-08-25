# Implementierung Bundesbank Prüfziffermethode: 27

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 27") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2 (modifiziert)
Die Berechnung erfolgt wie bei Verfahren 00, jedoch nur für
die Kontonummern von 1 bis 999 999 999. Ab
Konto 1 000 000 000 kommt das Prüfziffernverfahren M10H
(iterierte Transformation) zum Einsatz.
Es folgt die Beschreibung der iterierten Transformation:
Die Position der einzelnen Ziffern von rechts nach links
innerhalb der Kontonummer gibt die Zeile 1 bis 4 der
Transformationstabelle noch an. Aus ihr sind die
Übersetzungswerte zu summieren. Die Einerstelle wird von
10 subtrahiert. Die Differenz stellt die Prüfziffer dar.
Beispiel:
Kontonummer
2 8 4 7 1 6 9 4 8 P (P = Prüfziffer)
1 4 3 2 1 4 3 2 1 (Transf.-Zeile)
Transformationstabelle:
Ziffer: 0 1 2 3 4 5 6 7 8 9
Zeile 1: 0 1 5 9 3 7 4 8 2 6
Zeile 2: 0 1 7 6 9 8 3 2 5 4
Zeile 3: 0 1 8 4 6 2 9 5 7 3
Zeile 4: 0 1 2 3 4 5 6 7 8 9
Von rechts nach links:
Ziffer 8 wird 2 aus Transformationszeile 1
Ziffer 4 wird 9 aus Zeile 2
Ziffer 9 wird 3 aus Zeile 3
Ziffer 6 wird 6 aus Zeile 4
Ziffer 1 wird 1 aus Zeile 1
Ziffer 7 wird 2 aus Zeile 2
Ziffer 4 wird 6 aus Zeile 3
Ziffer 8 wird 8 aus Zeile 4
Ziffer 2 wird 5 aus Zeile 1
___
Summe 42
===
Die Einerstelle wird vom Wert 10 subtrahiert. Das Ergebnis
ist die Prüfziffer, in unserem Beispiel also 10 – 2 =
Prüfziffer 8, die Kontonummer lautet somit 2847169488.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_27.py
- Öffentliche API:
  - @register("27") def validate_method_27(blz: str, account: str) -> bool
  - @register_generator("27") def generate_account_method_27(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_27.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.