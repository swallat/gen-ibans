# Implementierung Bundesbank Prüfziffermethode: 96

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 96") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Variante 1
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 8, 9, 1
Die Prüfziffernrechnung ist nach Kennzeichen 19
durchzuführen.
Führt die Berechnung nach Variante 1 zu einem
Prüfzifferfehler, so ist die Berechnung nach Variante 2
vorzunehmen.
Gültige Kontonummern (Darstellung 10-stellig, einschl.
Prüfziffer): 0000254100, 9421000009
Variante 2
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Prüfziffernrechnung ist nach Kennzeichen 00
durchzuführen.
Gültige Kontonummern (Darstellung 10-stellig, einschl.
Prüfziffer): 0000000208, 0101115152, 0301204301
Variante 3
Führen die Berechnungen nach Variante 1 und 2 zu
Prüfzifferfehlern, so ist zu prüfen, ob die Kontonummer
zwischen 0001300000 und 0099399999 liegt.
Trifft dies zu, so gilt die Prüfziffer als richtig; trifft dies nicht zu,
so ist die Prüfziffer falsch.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_96.py
- Öffentliche API:
  - @register("96") def validate_method_96(blz: str, account: str) -> bool
  - @register_generator("96") def generate_account_method_96(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_96.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.