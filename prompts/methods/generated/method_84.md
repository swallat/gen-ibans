# Implementierung Bundesbank Prüfziffermethode: 84

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 84") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist durch linksbündige Nullenauffüllung
immer 10-stellig darzustellen. Die 10. Stelle ist per Definition
die Prüfziffer.
Es ist zu beachten, dass nur die Stellen 5 bis 9 in das
Prüfzifferberechnungsverfahren einbezogen werden.
Methode A
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06.
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer X X X X K K K K K P
Gewichtung 6 5 4 3 2
Testkontonummern richtig: 240699, 350982, 461059
Testkontonummern falsch: 240965, 350980, 461053
Führt die Berechnung nach Methode A zu einem Prüfzifferfehler,
ist die Berechnung nach Methode B vorzunehmen.
Methode B
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06. Dabei ist zu beachten, dass als Divisor 7 zu
verwenden ist.
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer X X X X K K K K K P
Gewichtung 6 5 4 3 2
Testkontonummern richtig: 240692, 350985, 461052
Testkontonummern falsch: 240965, 350980, 461053
Ergibt auch die Berechnung der Prüfziffer nach Methode B
einen Prüfzifferfehler, ist eine weitere Berechnung mit der
Methode C vorzunehmen.
Methode C
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen dem
Verfahren 06.
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer X X X X K K K K K P
Gewichtung 2 1 2 1 2
Testkontonummern richtig: 240961, 350984, 461054
Testkontonummern falsch: 240965, 350980, 461053
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung gemäß der Ausnahme in Methode 51 mit den
gleichen Ergebnissen und Testkontonummern.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_84.py
- Öffentliche API:
  - @register("84") def validate_method_84(blz: str, account: str) -> bool
  - @register_generator("84") def generate_account_method_84(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_84.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
