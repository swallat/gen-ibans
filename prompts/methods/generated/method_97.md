# Implementierung Bundesbank Prüfziffermethode: 97

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 97") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11:
Die Kontonummer (5, 6, 7, 8, 9 o. 10-stellig) ist durch
linksbündige Nullenauffüllung 10-stellig darzustellen. Danach
ist die 10. Stelle die Prüfziffer.
Die Kontonummer ist unter Weglassung der Prüfziffer
(= Wert X) durch 11 zu teilen. Das Ergebnis der Division ist
ohne die Nachkomma-Stellen mit 11 zu multiplizieren. Das
Produkt ist vom 'Wert X' zu subtrahieren.
Ist das Ergebnis < 10, so entspricht das Ergebnis der
Prüfziffer.
Ist das Ergebnis = 10, so ist die Prüfziffer = 0
Beispiel: 2 4 0 1 0 0 1 9 (8-stellige Kontonummer)
1) 2 401 001 : 11 = 218 272,81
2) 218 272 x 11 = 2 400 992
3) 2 401 001 - 2 400 992 = 9
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_97.py
- Öffentliche API:
  - @register("97") def validate_method_97(blz: str, account: str) -> bool
  - @register_generator("97") def generate_account_method_97(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_97.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
