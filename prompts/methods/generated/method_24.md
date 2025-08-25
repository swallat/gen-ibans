# Implementierung Bundesbank Prüfziffermethode: 24

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 24") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 1, 2, 3, 1, 2, 3, 1, 2, 3
Die für die Berechnung relevanten Stellen der Kontonummer
befinden sich - von links nach rechts gelesen - in den Stellen
1 - 9; die Prüfziffer in Stelle 10. Die Kontonummer ist
rechtsbündig zu interpretieren und ggf. mit Nullen aufzufüllen.
Die einzelnen Ziffern der Kontonummer sind, beginnend mit
der ersten Ziffer ungleich 0, von links nach rechts bis
einschließlich Stelle 9 mit den o. g. Gewichtungsfaktoren zu
multiplizieren. Zum jeweiligen Produkt ist der zugehörige
Gewichtungsfaktor zu addieren (zum ersten Produkt +1, zum
zweiten +2, zum dritten +3, zum Vierten +1 usw.). Das
jeweilige Ergebnis ist durch 11 zu dividieren (5 : 11 = 0 Rest
5). Die sich aus der Division ergebenden Reste sind zu
summieren. Die letzte Ziffer dieser Summe ist die Prüfziffer.
Ausnahmen:
1) Eine ggf. in Stelle 1 vorhandene Ziffer 3, 4, 5 oder 6 wird
als 0 gewertet. Der o. g. Prüfalgorithmus greift erst ab der
ersten Stelle ungleich 0.
2) Eine ggf. in Stelle 1 vorhandene Ziffer 9 wird als 0
gewertet und führt dazu, dass auch die beiden
nachfolgenden Ziffern in den Stellen 2 und 3 der
Kontonummer als 0 gewertet werden müssen. Der o. g.
Prüfalgorithmus greift in diesem Fall also erst ab Stelle 4
der 10stelligen Kontonummer. Die Stelle 4 ist ungleich 0.
Beispiele:
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 1 3 8 3 0 1
Ktonr.
umgesetzt:
0 0 0 0 1 3 8 3 0
Gewichtung: 1 2 3 1 2
1 6 24 3 0
Gewich- 1 2 3 1 2
tungsfaktor 2+8+27+4+2 = 21
11 1 = Prüfziffer
R5
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 1 3 0 6 1 1 8 6 0 5
Gewichtung: 1 2 3 1 2 3 1 2 3
1 6 0 6 2 3 8 12 0
Gewich- 1 2 3 1 2 3 1 2 3
tungsfaktor 2+8+3+7+4+6+9+14+3 = 45
11 5 = Prüfziffer
R3
Stellennr.: 1 2 3 4 5 6 7 8 9 10
24 Kontonr.: 3 3 0 7 1 1 8 6 0 8
Ktonr.
umgesetzt:
0 3 0 7 1 1 8 6 0
Gewichtung: 1 2 3 1 2 3 1 2
3 0 21 1 2 24 6 0
Gewich- 1 2 3 1 2 3 1 2
tungsfaktor 4+2+24+2+4+27+7+2 = 28
11 11 8 = Prüfziffer
R2 R5
Stellennr.: 1 2 3 4 5 6 7 8 9 10
Kontonr.: 9 3 0 7 1 1 8 6 0 3
Ktonr.
umgesetzt:
0 0 0 7 1 1 8 6 0
Gewichtung: 1 2 3 1 2 3
7 2 3 8 12 0
Gewich- 1 2 3 1 2 3
tungsfaktor 8+4+6+9+14+3 = 33
11 3 = Prüfziffer
R3
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_24.py
- Öffentliche API:
  - @register("24") def validate_method_24(blz: str, account: str) -> bool
  - @register_generator("24") def generate_account_method_24(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_24.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.