# Implementierung Bundesbank Prüfziffermethode: E0

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode E0") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Stellen der Kontonummer sind von rechts nach links mit
den Ziffern 2, 1, 2, 1, 2 usw. zu multiplizieren. Die jeweiligen
Produkte werden addiert, nachdem jeweils aus den
zweistelligen Produkten die Quersumme gebildet wurde
(z. B. Produkt 18 = Quersumme 9) plus den Wert 7. Nach
der Addition bleiben außer der Einerstelle alle anderen
Stellen unberücksichtigt. Die Einerstelle wird von dem Wert
10 subtrahiert. Das Ergebnis ist die Prüfziffer (10. Stelle der
Kontonummer). Ergibt sich nach der Subtraktion der
Rest 10, ist die Prüfziffer 0.
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 1 2 3 4 5 6 8 0 1 3
Gewichtung 2 1 2 1 2 1 2 1 2 P
Produkt 2 2 6 4 10 6 16 0 2
Quersumme 2 2 6 4 1 6 7 0 2
Summe = 30 + 7 = 37
10 – 7 (Einerstelle) = 3 = Prüfziffer
Testkontonummern (richtig):1234568013, 1534568010,
2610015, 8741013011
Testkontonummern (falsch):1234769013, 2710014,
9741015011
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_E0.py
- Öffentliche API:
  - @register("E0") def validate_method_E0(blz: str, account: str) -> bool
  - @register_generator("E0") def generate_account_method_E0(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_E0.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
