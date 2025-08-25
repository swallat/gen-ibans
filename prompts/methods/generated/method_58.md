# Implementierung Bundesbank Prüfziffermethode: 58

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 58") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 0, 0, 0, 0
Die Kontonummer (mindestens 6-stellig) ist durch linksbündige
Nullenauffüllung 10-stellig darzustellen. Danach ist die 10. Stelle
die Prüfziffer. Die Stellen 5 bis 9 werden von rechts nach links
mit den Ziffern 2, 3, 4, 5, 6 multipliziert. Die restliche
Berechnung und die Ergebnisse entsprechen dem Verfahren 02.
Beispiel:
Stellennr.: 1 2 3 4 5 6 7 8 9 P
Kontonr.: 1 8 0 0 2 9 3 3 7 7
Wichtung: 0 0 0 0 6 5 4 3 2
0 +0 +0 +0 +12 +45 +12 +9 +14 =92
92: 11 = 8, Rest 4 11-4=7 P= 7
Ergibt die Division einen Rest von 0, so ist die Prüfziffer = 0. Bei
einem Rest von 1 ist die Kontonummer falsch.
Testkontonummern:
1800881120, 9200654108, 1015222224, 3703169668
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_58.py
- Öffentliche API:
  - @register("58") def validate_method_58(blz: str, account: str) -> bool
  - @register_generator("58") def generate_account_method_58(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_58.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
