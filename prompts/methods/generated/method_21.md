# Implementierung Bundesbank Prüfziffermethode: 21

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 21") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2 (modifiziert)
Die Berechnung erfolgt wie bei Verfahren 00. Nach der
Addition der Produkte werden neben der Einerstelle jedoch
alle Stellen berücksichtigt, indem solange Quersummen
gebildet werden, bis ein einstelliger Wert verbleibt. Die
Differenz zwischen diesem Wert und dem Wert 10 ist die
Prüfziffer.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_21.py
- Öffentliche API:
  - @register("21") def validate_method_21(blz: str, account: str) -> bool
  - @register_generator("21") def generate_account_method_21(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_21.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.