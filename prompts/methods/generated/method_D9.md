# Implementierung Bundesbank Prüfziffermethode: D9

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D9") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Gewichtung und Berechnung erfolgen nach der Methode 00.
Führt die Berechnung nach Variante 1 zu einem Prüfzifferfehler,
so ist nach Variante 2 zu prüfen.
Testkontonummern (richtig): 1234567897, 0123456782
Testkontonummern (falsch): 9876543210, 1234567890,
6543217890, 0543216789
Variante 2:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 10
Gewichtung und Berechnung erfolgen nach der Methode 10.
Führt die Berechnung nach Variante 2 zu einem Prüfzifferfehler,
so ist nach Variante 3 zu prüfen.
Testkontonummern (richtig): 9876543210, 1234567890,
0123456789
Testkontonummern (falsch): 6543217890, 0543216789
Variante 3:
Modulus 10, Gewichtung 3, 9, 7, 1, 3, 9, 7, 1, 3
Gewichtung und Berechnung erfolgen nach der Methode 18.
Testkontonummern (richtig): 1100132044, 1100669030
Testkontonummern (falsch): 1100789043, 1100914032
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D9.py
- Öffentliche API:
  - @register("D9") def validate_method_D9(blz: str, account: str) -> bool
  - @register_generator("D9") def generate_account_method_D9(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D9.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
