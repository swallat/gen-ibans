# Implementierung Bundesbank Prüfziffermethode: C5

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode C5") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummern sind einschließlich der Prüfziffer 6- oder
8- bis 10-stellig, ggf. ist die Kontonummer für die Prüfzifferberechnung
durch linksbündige Auffüllung mit Nullen 10-
stellig darzustellen.
Die Berechnung der Prüfziffer und die möglichen Ergebnisse
richten sich nach dem jeweils bei der entsprechenden
Variante angegebenen Kontonummernkreis. Entspricht eine
Kontonummer keinem der vorgegebenen Kontonummernkreise
oder führt die Berechnung der Prüfziffer nach der
vorgegebenen Variante zu einem Prüfzifferfehler, so ist die
Kontonummer ungültig.
S = Ziffer der Kontonummer, die in die Prüfzifferberechnung
einbezogen wird
X = Weitere Ziffern der Kontonummer, die jedoch nicht in die
Prüfzifferberechnung mit einbezogen werden
P = Prüfziffer
Variante 1:
Modulus 10, Gewichtung 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 75.
 6-stellige Kontonummern; 5. Stelle = 1-8
Kontonummernkreis 0000100000 bis 0000899999
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
6-stellige
Konto-Nr.:
0 0 0 0 S
(1-8)
S S S S P
Testkontonummern (richtig): 0000301168, 0000302554
Testkontonummern (falsch): 0000302589, 0000507336
 9-stellige Kontonummern; 2. Stelle = 1-8
Kontonummernkreis 0100000000 bis 0899999999
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
9-stellige
Konto-Nr.:
0 S
(1-8)
S S S S P X X X
Testkontonummern (richtig): 0300020050, 0300566000
Testkontonummern (falsch): 0302555000, 0302589000
Variante 2:
Modulus 10, iterierte Transformation
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 29.
 10-stellige Kontonummern, 1. Stelle = 1, 4, 5, 6 oder 9
Kontonummernkreis 1000000000 bis 1999999999
Kontonummernkreis 4000000000 bis 6999999999
Kontonummernkreis 9000000000 bis 9999999999
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
10-stellige
Konto-Nr.:
S S S S S S S S S P
Testkontonummern (richtig): 1000061378, 1000061412,
4450164064, 4863476104,
5000000028, 5000000391,
6450008149, 6800001016,
9000100012, 9000210017
Testkontonummern (falsch): 1000061457, 1000061498
4864446015, 4865038012,
5000001028, 5000001075,
6450008150, 6542812818,
9000110012, 9000300310
Variante 3:
Modulus 10, Gewichtung 2, 1, 2, 1, 2, 1, 2, 1, 2
Die Berechnung und mögliche Ergebnisse entsprechen der
Methode 00.
 10-stellige Kontonummern, 1. Stelle = 3
Kontonummernkreis 3000000000 bis 3999999999
Stellen-Nr.: 1 2 3 4 5 6 7 8 9 10
10-stellige
Konto-Nr.:
S
(3)
S S S S S S S S P
Testkontonummern (richtig): 3060188103, 3070402023
Testkontonummern (falsch): 3081000783, 3081308871
Variante 4:
Für die folgenden Kontonummernkreise gilt die Methode 09
(keine Prüfzifferberechnung).
 8-stellige Kontonummern; 3. Stelle = 3, 4 oder 5
Kontonummernkreis 0030000000 bis 0059999999
 10-stellige Kontonummern; 1.+ 2. Stelle = 70 oder 85
Kontonummernkreis 7000000000 bis 7099999999
Kontonummernkreis 8500000000 bis 8599999999
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_C5.py
- Öffentliche API:
  - @register("C5") def validate_method_C5(blz: str, account: str) -> bool
  - @register_generator("C5") def generate_account_method_C5(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_C5.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
