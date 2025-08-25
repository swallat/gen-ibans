# Implementierung Bundesbank Prüfziffermethode: B0

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B0") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummern sind immer 10-stellig. Kontonummern
(ohne führende Nullen gezählt) mit 9 oder weniger Stellen
sind falsch. Kontonummern mit 8 an der ersten Stelle sind
ebenfalls falsch. Die weitere Verfahrensweise richtet sich
nach der 8. Stelle der Kontonummer:
Variante 1
Für Kontonummern mit einer 1, 2, 3, oder 6 an der 8. Stelle
gilt das Verfahren 09 (Keine Prüfzifferberechnung, alle
Kontonummern sind richtig).
Testkontonummern (richtig): 1197423162, 1000000606
Testkontonummern (falsch): 8137423260, 600000606,
51234309
Variante 2
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7, 2, 3, 4
(von rechts beginnend)
Für Kontonummern mit einer 0, 4, 5, 7, 8 oder 9 an der
8. Stelle erfolgen Gewichtung und Berechnung wie beim
Verfahren 06.
Beispiel:
Stelle: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 1 0 2 4 3 9 1 9 1 0
Gewichtung: 4 3 2 7 6 5 4 3 2 P
Produkt: 4+ 0+ 4+ 28+18+45+4+27+ 2 =132
132: 11 = 12, Rest 0 = P
Testkontonummern (richtig): 1000000406, 1035791538,
1126939724, 1197423460
Testkontonummern (falsch): 1000000405, 1035791539,
8035791532, 535791830,
51234901
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B0.py
- Öffentliche API:
  - @register("B0") def validate_method_B0(blz: str, account: str) -> bool
  - @register_generator("B0") def generate_account_method_B0(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B0.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
