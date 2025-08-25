# Implementierung Bundesbank Prüfziffermethode: 52

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 52") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Modulus 11, Gewichtung 2, 4, 8, 5, 10, 9, 7, 3, 6, 1, 2, 4
Zur Berechnung der Prüfziffer muss zunächst aus der
angegebenen Bankleitzahl und der angegebenen
achtstelligen Kontonummer die zugehörige Kontonummer
des ESER-Altsystems (maximal 12-stellig) ermittelt werden.
Die einzelnen Stellen dieser Alt-Kontonummer sind von
rechts nach links mit den Ziffern 2, 4, 8, 5, 10, 9, 7, 3, 6, 1, 2,
4 zu multiplizieren. Dabei ist für die Prüfziffer, die sich immer
an der 6. Stelle von links der Alt-Kontonummer befindet, 0 zu
setzen. Die jeweiligen Produkte werden addiert und die
Summe durch 11 dividiert. Zum Divisionsrest (ggf. auch 0) ist
das Gewicht oder ein Vielfaches des Gewichtes über der
Prüfziffer zu addieren. Die Summe wird durch 11 dividiert; der
Divisionsrest muss 10 lauten. Die Prüfziffer ist der
verwendete Faktor des Gewichtes. Kann bei der Division kein
Rest 10 erreicht werden, ist die Konto-Nr. nicht verwendbar.
Bildung der Konto-Nr. des ESER-Altsystems aus
angegebener Bankleitzahl und Konto-Nr.:
BLZ Konto-Nr.
XXX5XXXX XPXXXXXX (P = Prüfziffer)
Kontonummer des Altsystems:
XXXX-XP-XXXXX (XXXX = variable Länge, da
evtl. vorlaufende Nullen eliminiert
werden)
Beispiel:
BLZ Konto-Nr.
13051172 4P001500
Konto-Nr. Altsystem (Multiplikation mit Gewichten)
1 1 7 2 - 4 P - 1 5 0 0
* * * * * * * * * *
1 6 3 7 9 1 0 5 8 4 2
= 1 + 6 + 21 + 14 + 36 + 0 + 5 + 40 + 0 + 0 =123
123 : 11 = 11 Rest 2
2 + 0 x 10 = 2 : 11 = 0 Rest 2 (10 = Gewicht
2 + 1 x 10 = 12 : 11 = 1 Rest 1 über der Prüf-
2 + 2 x 10 = 22 : 11 = 2 Rest 0 ziffer)
2 + 3 x 10 = 32 : 11 = 2 Rest 10
Die Prüfziffer lautet 3.
Bei 10-stelligen, mit 9 beginnenden Kontonummern ist die
Prüfziffer nach Verfahren 20 zu berechnen.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_52.py
- Öffentliche API:
  - @register("52") def validate_method_52(blz: str, account: str) -> bool
  - @register_generator("52") def generate_account_method_52(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_52.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
