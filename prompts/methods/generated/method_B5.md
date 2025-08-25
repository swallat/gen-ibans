# Implementierung Bundesbank Prüfziffermethode: B5

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode B5") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist einschließlich der Prüfziffer 10-stellig,
ggf. ist die Kontonummer für die Prüfzifferberechnung durch
linksbündige Auffüllung mit Nullen 10-stellig darzustellen.
Variante 1:
Modulus 10, Gewichtung 7, 3, 1 ,7 , 3, 1, 7, 3, 1
Die Gewichtung entspricht der Methode (Kennzeichen) 05.
Die Berechnung entspricht der Methode (Kennzeichen) 01.
Führt die Berechnung nach der Variante 1 zu einem
Prüfzifferfehler, so sind Kontonummern, die an der 1. Stelle
von links der 10-stelligen Kontonummer den Wert 8 oder 9
beinhalten, falsch. Alle anderen Kontonummern sind nach der
Variante 2 zu prüfen.
Testkontonummern (richtig): 0159006955, 2000123451,
1151043216, 9000939033
Testkontonummern (falsch): 7414398260, 8347251693,
1151043211, 2345678901,
5678901234, 9000293707
Variante 2:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Gewichtung und Berechnung erfolgen nach der Methode
(Kennzeichen) 00.
Testkontonummern (richtig): 0123456782, 0130098767,
1045000252
Testkontonummern (falsch): 0159004165, 0023456787,
0056789018, 3045000333
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_B5.py
- Öffentliche API:
  - @register("B5") def validate_method_B5(blz: str, account: str) -> bool
  - @register_generator("B5") def generate_account_method_B5(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_B5.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
