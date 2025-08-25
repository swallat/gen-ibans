# Implementierung Bundesbank Prüfziffermethode: 68

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 68") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Kontonummern sind 6- bis 10-stellig und enthalten keine
führenden Nullen. Die erste Stelle von rechts ist die Prüfziffer.
Die Berechnung erfolgt wie bei Verfahren 00, hierbei sind jedoch
folgende Besonderheiten zu beachten:
Bei 10-stelligen Kontonummern erfolgt die Berechnung für die 2.
bis 7. Stelle. Stelle 7 muss eine »9« sein.
Stellennr.: A 9 8 7 6 5 4 3 2 1 (A = 10)
Kontonr.: 8 8 8 9 6 5 4 3 2 P
Gewichtung: 1 2 1 2 1 2
9 + 3 + 5 + 8 + 3 + 4 = 32
(Q)
(Q = Quersumme)
Die Einerstelle der Summe wird vom Wert 10 subtrahiert
(10 - 2 = 8).
Die Prüfziffer ist in diesem Fall die 8 und die vollständige
Kontonummer lautet: 8 8 8 9 6 5 4 3 2 8
6- bis 9-stellige Kontonummern sind in zwei Varianten prüfbar.
Variante 1: voll prüfbar
Kontonr.: 9 8 7 6 5 4 3 2 P
Gewichtung: 1 2 1 2 1 2 1 2
9 + 7 + 7 + 3 + 5 + 8 + 3 + 4 = 46
(Q) (Q)
(Q = Quersumme)
Die Einerstelle der Summe wird vom Wert 10 subtrahiert
(10 - 6 = 4).
Die Prüfziffer ist in diesem Fall die 4 und die vollständige
Kontonummer lautet: 9 8 7 6 5 4 3 2 4
Ergibt die Berechnung nach Variante 1 einen Prüfzifferfehler,
muss Variante 2 zu einer korrekten Prüfziffer führen.
Variante 2: Stellen 7 und 8 werden nicht geprüft.
Kontonr.: 9 8 7 6 5 4 3 2 P
Gewichtung: 1 2 1 2 1 2
9 + 3 + 5 + 8 + 3 + 4 = 32
(Q)
(Q = Quersumme)
Die Einerstelle der Summe wird vom Wert 10 subtrahiert
(10 - 2 = 8).
Die Prüfziffer ist in diesem Fall die 8 und die vollständige
Kontonummer lautet: 9 8 7 6 5 4 3 2 8
9-stellige Kontonummern im Nummernbereich 400 000 000 bis
499 999 999 sind nicht prüfbar, da diese Nummern keine
Prüfziffer enthalten.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_68.py
- Öffentliche API:
  - @register("68") def validate_method_68(blz: str, account: str) -> bool
  - @register_generator("68") def generate_account_method_68(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_68.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.