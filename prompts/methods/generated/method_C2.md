# Implementierung Bundesbank Prüfziffermethode: C2

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C2") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Die 10. Stelle der Kontonummer ist die Prüfziffer.
Variante 1:
Modulus 10, Gewichtung 3, 1, 3, 1, 3, 1, 3, 1, 3
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 22. Führt die Berechnung nach Variante 1 zu einem
Prüfzifferfehler, so ist nach Variante 2 zu prüfen.
Testkontonummern (richtig): 2394871426, 4218461950,
7352569148
Testkontonummern (falsch): 5127485166, 8738142564,
0328705282, 9024675131,
0076543216, 3456789012,
9024675138, 7352569145
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00. Führt die Berechnung nach Variante 2 zu einem
Prüfzifferfehler, so ist nach Variante 3 zu prüfen.
Testkontonummern (richtig): 5127485166, 8738142564
Testkontonummern (falsch): 0328705282, 9024675131,
0076543216, 3456789012,
9024675138, 7352569145
Variante 3:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2, 3, 4
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 04.
Testkontonummern (richtig): 0076543216, 3456789012,
9024675138
Testkontonummern (falsch): 0328705282, 7352569145,
9024675131
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C2.py
- Öffentliche API:
  - @register("C2") def validate_method_C2(blz: str, account: str) -> bool
  - @register_generator("C2") def generate_account_method_C2(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C2.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
