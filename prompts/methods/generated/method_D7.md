# Implementierung Bundesbank Prüfziffermethode: D7

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D7") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Die Stellen der Kontonummer sind von rechts nach links mit
den Ziffern 2, 1, 2, 1, 2, 1, 2, 1, 2 zu multiplizieren. Die
jeweiligen Produkte werden addiert, nachdem jeweils aus den
zweistelligen Produkten die Quersumme gebildet wurde (z. B.
Produkt 18 = Quersumme 9). Nach der Addition bleiben außer
der Einerstelle alle anderen Stellen unberücksichtigt; diese
Einerstelle ist die Prüfziffer (Ergebnis = 27 / Prüfziffer = 7).
Beispiel:
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 0 5 0 0 0 1 8 2 0 5
Gewichtung 2 1 2 1 2 1 2 1 2 P
Produkt 0 5 0 0 0 1 16 2 0
Quersumme 0 5 0 0 0 1 7 2 0
Summe = 15
Einerstelle = Prüfziffer = 5
Testkontonummern richtig: 0500018205, 0230103715,
0301000434, 0330035104,
0420001202, 0134637709,
0201005939, 0602006999
Testkontonummern falsch: 0501006102, 0231307867,
0301005331, 0330034104,
0420001302, 0135638809,
0202005939, 0601006977
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D7.py
- Öffentliche API:
  - @register("D7") def validate_method_D7(blz: str, account: str) -> bool
  - @register_generator("D7") def generate_account_method_D7(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D7.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
