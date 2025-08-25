# Implementierung Bundesbank Prüfziffermethode: 65

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 65") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2
Die Kontonummer ist zehnstellig.
Darstellung der Kontonummer:
G G G S S S S P K U
G = Geschäftsstellennummer
S = Stammnummer
P = Prüfziffer
K = Kontenartziffer
U = Unterkontonummer
Die Berechnung erfolgt wie bei Verfahren 00 über
Geschäftsstellennummer und Stammnummer mit der
Gewichtung 2, 1, 2, 1, 2, 1, 2.
Stellen: G G G S S S S P K U
Kontonr.: 1 2 3 4 5 6 7 0 0
Gewichtung: 2 1 2 1 2 1 2
2 + 2 + 6 + 4 + 1 + 6 + 5 = 26
(Q) (Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert (10 - 6 = 4).
Die Prüfziffer ist in diesem Fall die 4 und die vollständige
Kontonummer lautet: 1 2 3 4 5 6 7 4 0 0
Ausnahme:
Ist die Kontenartziffer (neunte Stelle der Kontonummer) eine 9,
so werden die neunte und zehnte Stelle der Kontonummer in
die Prüfzifferermittlung einbezogen.
Die Berechnung erfolgt dann über Geschäftsstellennummer,
Stammnummer, Kontenartziffer und Unterkontonummer mit der
Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2.
Stellen: G G G S S S S P K U
Kontonr.: 1 2 3 4 5 6 7 9 0
Gewichtung: 2 1 2 1 2 1 2 1 2
2 + 2 + 6 + 4 + 1 + 6 + 5 + 9 + 0 = 35
(Q) (Q)
(Q = Quersumme)
Die Einerstelle wird vom Wert 10 subtrahiert (10 - 5 = 5).
Die Prüfziffer ist in diesem Fall die 5 und die vollständige
Kontonummer lautet: 1 2 3 4 5 6 7 5 9 0
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_65.py
- Öffentliche API:
  - @register("65") def validate_method_65(blz: str, account: str) -> bool
  - @register_generator("65") def generate_account_method_65(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_65.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
