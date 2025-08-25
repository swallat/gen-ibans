# Implementierung Bundesbank Prüfziffermethode: D8

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode D8") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Die Berechnung der Prüfziffer und die möglichen Ergebnisse
richten sich nach dem jeweils bei der entsprechenden
Variante angegebenen Kontonummernkreis. Entspricht eine
Kontonummer keinem der vorgegebenen Kontonummernkreise
oder führt die Berechnung der Prüfziffer nach der
Variante 1 zu einem Prüfzifferfehler, so ist die Kontonummer
ungültig.
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Für Kontonummern aus dem Kontonummernkreis
1000000000 bis 9999999999 entsprechen die Berechnung
und mögliche Ergebnisse der Methode 00.
Beispiel:
Kontonummer: 6899999954
Stellen 1 – 9: 689999995
Stelle-Nr. 1 2 3 4 5 6 7 8 9 10
Kontonummer 6 8 9 9 9 9 9 9 5 4
Gewichtung 2 1 2 1 2 1 2 1 2 P
Produkt 12 8 18 9 18 9 18 9 10
Quersumme 3 8 9 9 9 9 9 9 1
Summe = 66
10 – 6 (Einerstelle) = 4 = Prüfziffer
Testkontonummern (richtig): 1403414848, 6800000439,
6899999954
Testkontonummern (falsch): 3012084101, 1062813622,
0000260986
Variante 2:
Für den Kontonummernkreis 0010000000 bis 0099999999 gilt
die Methode 09 (keine Prüfzifferberechnung, alle Kontonummern
sind als richtig zu werten).
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_D8.py
- Öffentliche API:
  - @register("D8") def validate_method_D8(blz: str, account: str) -> bool
  - @register_generator("D8") def generate_account_method_D8(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_D8.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
