# Implementierung Bundesbank Prüfziffermethode: 50

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 50") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die für die Berechnung relevante Grundnummer befindet sich in
den Stellen 1 bis 6, die Prüfziffer in Stelle 7 (von links nach
rechts gezählt). Die Stellen 1 bis 6 werden mit den Ziffern 7, 6, 5,
4, 3, 2 multipliziert. Die restliche Berechnung und Ergebnisse
entsprechen dem Verfahren 06. Die dreistellige Unternummer
(Stellen 8 bis 10) darf nicht in das Prüfzifferberechnungsverfahren
einbezogen werden. Ist die Unternummer »000«, so
kommt es vor, dass diese nicht angegeben ist. Ergibt die erste
Berechnung einen Prüfzifferfehler, wird empfohlen, die
Prüfzifferberechnung ein zweites Mal durchzuführen und dabei
die »gedachte« Unternummer 000 an die Stellen 8 bis 10 zu
setzen und die vorhandene Kontonummer vorher um drei Stellen
nach links zu verschieben.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x P x x x
Gewichtung: 7 6 5 4 3 2
Testkontonummern: 4000005001, 4444442001
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_50.py
- Öffentliche API:
  - @register("50") def validate_method_50(blz: str, account: str) -> bool
  - @register_generator("50") def generate_account_method_50(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_50.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
