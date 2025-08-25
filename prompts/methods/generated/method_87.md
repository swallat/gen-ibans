# Implementierung Bundesbank Prüfziffermethode: 87

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 87") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Kontonummer ist durch linksbündige Nullenauffüllung 10-
stellig darzustellen. Der zur Prüfzifferberechnung
heranzuziehende Teil befindet sich bei der Methode A und D
in den Stellen 4 bis 9 der Kontonummer und bei den
Methoden B und C in Stellen 5 - 9, die Prüfziffer in Stelle 10
der Kontonummer. Ergibt die erste Berechnung der Prüfziffer
nach der Methode A einen Prüfzifferfehler, so sind weitere
Berechnungen mit den anderen Methoden vorzunehmen.
Ausnahme:
Ist nach linksbündiger Auffüllung mit Nullen auf 10 Stellen die
3. Stelle der Kontonummer = 9 (Sachkonten), so erfolgt die
Berechnung gemäß der Ausnahme in Methode 51 mit den
gleichen Ergebnissen und Testkontonummern.
Methode A:
Für die Berechnung werden folgende Felder verwendet:
i = Hilfsvariable (Laufvariable)
C2 = Hilfsvariable (Kennung, ob gerade oder ungerade
Stelle bearbeitet wird)
D2 = Hilfsvariable
A5 = Hilfsvariable (Summenfeld), kann negativ
werden
P = Hilfsvariable (zur Zwischenspeicherung der
Prüfziffer)
KONTO = 10-stelliges Kontonummernfeld mit KONTO
(i) = in Bearbeitung befindliche Stelle; der
Wert an jeder Stelle kann zweistellig werden
TAB1; TAB2 = Tabellen mit Prüfziffern:
Tabelle TAB1 Tabelle TAB2
Stelle Inhalt Stelle Inhalt
0 0 0 7
1 4 1 1
2 3 2 5
3 2 3 9
4 6 4 8
i : = 4;
DO WHILE KONTO (i) = 0
i : = i + 1;
END;
C2 : = i mod 2;
D2 : = 0;
A5 : = 0;
DO WHILE i < 10
CASE KONTO (i) OF
0:
KONTO (i) : = 5;
1:
KONTO (i) : = 6;
5:
KONTO (i) : = 10;
6:
KONTO (i) : = 1;
END;
IF C2 = D2 THEN
BEGIN
IF KONTO (i) > 5 THEN
BEGIN
IF C2 = 0 AND D2 = 0 THEN
BEGIN
C2 : = 1;
D2 : = 1;
A5 : = A5 + 6 - (KONTO (i) - 6);
END ELSE
BEGIN
C2 : = 0;
D2 : = 0;
A5 : = A5 + KONTO (i);
END
END ELSE
BEGIN
IF C2 = 0 AND D2 = 0 THEN
BEGIN
C2 : = 1;
A5 : = A5 + KONTO (i);
END ELSE
BEGIN
C2 : = 0
A5 : = A5 + KONTO (i);
END
END;
END ELSE
BEGIN
IF KONTO (i) > 5 THEN
BEGIN
IF C2 = 0 THEN
BEGIN
C2 : = 1;
D2 : = 0;
A5 : = A5 - 6 + (KONTO (i) - 6);
END ELSE
BEGIN
C2 : = 0;
D2 : = 1;
A5 : = A5 - KONTO (i);
END
END ELSE
BEGIN
IF C2 = 0 THEN
BEGIN
C2 : = 1;
A5 : = A5 - KONTO (i);
END ELSE
BEGIN
C2 := 0;
A5 := A5 - KONTO (i);
END
END;
END;
i := i + 1;
END
DO WHILE A5 < 0 OR A5 > 4
IF A5 > 4 THEN
BEGIN
A5 := A5 - 5;
END ELSE
BEGIN
A5 := A5 + 5;
END
END;
IF D2 = 0 THEN
BEGIN
P := TAB1 (A5);
END ELSE
BEGIN
P := TAB2 (A5);
END
IF P = KONTO (10) THEN
BEGIN
Prüfziffer OK;
END ELSE
BEGIN
IF KONTO (4) = 0 THEN
BEGIN
IF P > 4 THEN
BEGIN
P := P - 5;
END ELSE
BEGIN
P := P + 5;
END
IF P = KONTO (10) THEN
BEGIN
Prüfziffer OK;
END
END;
END,
Testkontonummern: 0000000406, 0000051768,
0010701590, 0010720185
Führt die Berechnung nach Methode A zu einem
Prüfzifferfehler, ist die Berechnung nach Methode B
vorzunehmen.
Methode B:
Modulus 11, Gewichtung 2, 3, 4, 5, 6
Die für die Berechnung relevanten Stellen werden von rechts
nach links mit den Ziffern 2, 3, 4, 5, 6 multipliziert. Die weitere
Berechnung und die möglichen Ergebnisse entsprechen dem
Verfahren 33.
Stellennr.: 1 2 3 4 5 6 7 8 9 A (A = 10)
Kontonr.: x x x x x x x x x P
Gewichtung: 6 5 4 3 2
Führt die Berechnung nach Methode B wiederum zu einem
Prüfzifferfehlen, ist eine weitere Berechnung nach Methode C
vorzunehmen.
Methode C:
Modulus 7, Gewichtung 2, 3, 4, 5, 6
Die Stellen 5 bis 9 der Kontonummer werden von rechts nach
links mit den Gewichten multipliziert. Die jeweiligen Produkte
werden addiert. Die Summe ist durch 7 zu dividieren. Der
verbleibende Rest wird vom Divisor (7) subtrahiert. Das
Ergebnis ist die Prüfziffer. Verbleibt nach der Division kein
Rest, ist die Prüfziffer = 0.
Testkontonummern Methode B und C:
0000100005, 0000393814,
0000950360, 3199500501
Führt die Berechnung nach Methode C wiederum zu einem
Prüfzifferfehler, ist eine weitere Berechnung nach Methode D
vorzunehmen.
Methode D:
Modulus 11, Gewichtung 2, 3, 4, 5, 6, 7
Die Stellen 4 bis 9 werden von rechts nach links mit den
Ziffern 2, 3, 4, 5, 6, 7 multipliziert. Die weitere Berechnung
und mögliche Ergebnisse entsprechen dem Verfahren 06.
Stelle-Nr. 1 2 3 4 5 6 7 8 9 A (A=10)
Konto-Nr. x x x K K K K K K P
Gewichtung 7 6 5 4 3 2
Testkontonummern (richtig): 0001975641, 0001988654
Testkontonummern (falsch): 0001924592
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_87.py
- Öffentliche API:
  - @register("87") def validate_method_87(blz: str, account: str) -> bool
  - @register_generator("87") def generate_account_method_87(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_87.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
