# Implementierung Bundesbank Prüfziffermethode: 69

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 69") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Für den Kontonummernkreis 9 300 000 000 bis 9 399 999 999 ist
keine Prüfzifferberechnung möglich = Kennzeichen 09.
Für den Kontonummernkreis 9 700 000 000 bis 9 799 999 999 ist
die Prüfzifferberechnung nach Variante 2 vorzunehmen:
Für alle anderen Kontonummern ist die Prüfziffer nach
Variante 1 zu ermitteln. Ergab die Berechnung nach Variante 1
einen Prüfzifferfehler, ist die Prüfziffer nach Variante 2 zu
ermitteln.
Variante 1
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8
Die Berechnung erfolgt wie bei Verfahren 28.
Variante 2
Die Position der einzelnen Ziffern von rechts nach links innerhalb
der Kontonummer gibt die Zeile 1 bis 4 der Transformationstabelle
an. Aus ihr sind die Übersetzungswerte zu summieren.
Die Einerstelle wird von 10 subtrahiert und stellt die
Prüfziffer dar.
Beispiel:
Kontonr.: 9 7 2 1 1 3 4 8 6 P
Gewichtung: 1 4 3 2 1 4 3 2 1
(P = Prüfziffer)
(Transf.-Zeile)
Transformationstabelle:
Ziffer : 0 1 2 3 4 5 6 7 8 9
Zeile 1 : 0 1 5 9 3 7 4 8 2 6
Zeile 2 : 0 1 7 6 9 8 3 2 5 4
Zeile 3 : 0 1 8 4 6 2 9 5 7 3
Zeile 4 : 0 1 2 3 4 5 6 7 8 9
Von rechts nach links:
Ziffer 6 wird 4 aus Transformationszeile 1
Ziffer 8 wird 5 aus Zeile 2
Ziffer 4 wird 6 aus Zeile 3
Ziffer 3 wird 3 aus Zeile 4
Ziffer 1 wird 1 aus Zeile 1
Ziffer 1 wird 1 aus Zeile 2
Ziffer 2 wird 8 aus Zeile 3
Ziffer 7 wird 7 aus Zeile 4
Ziffer 9 wird 6 aus Zeile 1
__
Summe 41
==
Die Einerstelle wird vom Wert 10 subtrahiert. Das Ergebnis ist
die Prüfziffer, in unserem Beispiel also 10 - 1 = Prüfziffer 9, die
Kontonummer lautet: 9 7 2 1 1 3 4 8 6 9.
Testkontonummern:
1234567900 (Variante 1)
1234567006 (Variante 2)
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_69.py
- Öffentliche API:
  - @register("69") def validate_method_69(blz: str, account: str) -> bool
  - @register_generator("69") def generate_account_method_69(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_69.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.