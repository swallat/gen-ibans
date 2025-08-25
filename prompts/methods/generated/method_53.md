# Implementierung Bundesbank Prüfziffermethode: 53

Kontext:
- Diese Vorlage dient dazu, die Implementierung und/oder Validierung der Prüfzifferberechnungsmethode ("Methode 53") gemäß der Spezifikation der Deutschen Bundesbank zu erstellen oder zu prüfen.
- Spezifikation (einfügen/anhängen):

```Text
Die Berechnung entspricht dem Verfahren 52, jedoch für
neunstellige Kontonummern.
Bildung der Kontonummern des ESER-Altsystems aus
angegebener Bankleitzahl und angegebener neunstelliger
Kontonummer:
BLZ Konto-Nr.
XXX5XXXX XTPXXXXXX (P = Prüfziffer, T)
Kontonummer des ESER-Altsystems:
XXTX-XP-XXXXXX (XXXXXX = variable Länge, da
evtl. vorlaufende Nullen
eliminiert werden)
Beispiel:
BLZ Konto-Nr.
16052072 38P432256
Konto-Nr. Altsystem (Multiplikation mit Gewichten)
2 0 8 2 - 3 P 4 3 2 2 5 6
* * * * * * * * * * * *
4 2 1 6 3 7 9 10 5 8 4 2
8 + 0 + 8 + 12
+
9 + 0 + 36
+
30
+
10
+
16
+
20 + 12
=
161
161 : 11 = 14 Rest 7
7 + 0 x 7 = 7; 7 : 11 = 0 Rest 7 (Faktor 7: Gewicht
über der
Prüfziffer)
7 + 1 x 7 = 14; 14 : 11 = 1 Rest 3
7 + 2 x 7 = 21; 21 : 11 = 1 Rest 10
Die Prüfziffer lautet 2.
Bei 10-stelligen, mit 9 beginnenden Kontonummern ist die
Prüfziffer nach Verfahren 20 zu berechnen.
```

Vorgaben:
- Programmiersprache: Python 3.11+
- Zielmodul/Datei: gen_ibans/methods/method_53.py
- Öffentliche API:
  - @register("53") def validate_method_53(blz: str, account: str) -> bool
  - @register_generator("53") def generate_account_method_53(blz: str, rng: random.Random) -> str
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
- Vollständiger Python-Codeausschnitt für method_53.py mit Validator und Generator.
- Kurzer Begründungstext, wie die Berechnung aus der Spezifikation abgeleitet wurde.
Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README.
Alle Tests sollten nicht via Kommandozeile, sondern via pytest ausgeführt werden.
