# Implementierung Bundesbank Prüfziffermethode: B6

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B6") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Variante 1:
Modulus 11, Gewichtung 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,3
Kontonummern, die an der 1. Stelle der 10-stelligen Kontonummer
den Wert 1-9 oder an den Stellen 1–5 die Werte
02691-02699 beinhalten, sind nach der Methode 20 zu
prüfen. Alle anderen Kontonummern sind nach der Variante 2
zu prüfen.
Testkontonummer (richtig): 9110000000, 0269876545
Testkontonummer (falsch): 9111000000, 0269456780
Variante 2:
Modulus 11, Gewichtung 2, 4, 8, 5, 10, 9, 7, 3, 6, 1, 2, 4
Die Berechnung erfolgt nach der Methode 53.
Testkontonummer (richtig) mit BLZ 80053782: 487310018
Testkontonummer (falsch) mit BLZ 80053762: 467310018
Testkontonummer (falsch) mit BLZ 80053772: 477310018
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B6.py
- Öffentliche API:
  - @register("B6") def validate_method_B6(blz: str, account: str) -> bool
  - @register_generator("B6") def generate_account_method_B6(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B6.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
