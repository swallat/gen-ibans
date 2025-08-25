# Implementierung Bundesbank Prüfziffermethode: A1

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode A1") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 0, 0
Die Kontonummern sind 8- oder 10-stellig. Kontonummern
(ohne führende Nullen gezählt) mit 9 oder weniger als 8
Stellen sind falsch. 8-stellige Kontonummern sind für die
Prüfzifferberechnung durch linksbündige Auffüllung mit Nullen
10-stellig darzustellen. Die Berechnung erfolgt wie beim
Verfahren 00.
Beispiel:
Kontonr.: 0 0 1 0 0 3 0 9 9 7
Gewichtung: 0 0 2 1 2 1 2 1 2 P
Produkte: 0 0 2 0 0 3 0 9 18
Quersummen:0+ 0+ 2+ 0+ 0+ 3+ 0+ 9+ 9= 23
10-3 = 7 = P
Testkontonummern (richtig): 0010030005, 0010030997,
1010030054
Testkontonummern (falsch): 0110030005, 0010030998,
0000030005
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_A1.py
- Öffentliche API:
  - @register("A1") def validate_method_A1(blz: str, account: str) -> bool
  - @register_generator("A1") def generate_account_method_A1(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_A1.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
