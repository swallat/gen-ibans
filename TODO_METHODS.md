# ToDo: Prüfziffer-Methoden (Deutsche Bundesbank) vollständig implementieren

Dieses Dokument dient als Arbeitsgrundlage für kommende Sessions zur vollständigen, korrekten Umsetzung der Prüfziffer-Berechnungsverfahren (Prüfziffermethoden) für deutsche Kontonummern gemäß Deutscher Bundesbank. Es beschreibt Vorgehen, Prioritäten, Teststrategie sowie den Zielzustand in diesem Repository.


## Quellen und Referenzen
- Offizielle Beschreibung der Prüfzifferberechnung (Bundesbank):
  https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/serviceangebot/pruefzifferberechnung/pruefzifferberechnung-fuer-kontonummern-626222
- Referenz-Implementierung (als Vorlage):
  https://github.com/baumerdev/ibantools-germany/tree/main/src/lib/methods


## Aktueller Stand im Projekt
- Paket `gen_ibans.methods` mit:
  - Registry/Dekorator `register(method_code)`
  - Generische Erzeugung `generate_valid_account(blz, rng, method_code)` mit Validator-basiertem Retry.
- Bereits implementierte Files (mit Unit-Tests):
  - method_00.py (akzeptiert 10-stellige Kontonummern – korrekt für „00“/kein Check)
  - method_01.py (Mod11 mit Gewichten [2..10], 11→0, 10→invalid)
  - method_02.py (Mod11 mit Gewichten [2,3,4,5,6,7,8,9,2], 11→0, 10→invalid)
  - method_03.py (Mod11 mit wiederholten Gewichten 2..7, 11→0, 10→invalid)
  - method_04.py (einfaches Mod10 über die ersten 9 Stellen)
  - method_05.py (Luhn/Mod10, letzte Stelle Prüfziffer)
  - method_06.py (Mod11 mit Gewichten [2..10], 11→0, 10→invalid)
  - method_07.py (Mod11 mit wiederholten Gewichten 2..7, 11→0, 10→invalid)
  - method_08.py (Mod11 mit Gewichten [2,3,4,5,6,7,8,9,2], 11→0, 10→invalid)
  - method_09.py (Mod11 mit wiederholten Gewichten 2..7)
  - method_10.py (einfaches Mod10 über die ersten 9 Stellen)
  - method_13.py (Luhn/Mod10, letzte Stelle Prüfziffer)
  - method_24.py (Mod11 mit Gewichten [2,3,4,5,6,7,8,9,2])
- `IBANGenerator` nutzt `BankInfo.method_code` und generiert Kontonummern über `gen_ibans.methods.generate_valid_account`.
- Vollständige methodenspezifische Detailtests existieren für 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 13 und 24; gesamte Test-Suite grün.


## Zielbild
- Alle von der Bundesbank definierten Verfahren (00, 01, …, inkl. Sonderfälle/Gruppenvarianten) sind korrekt implementiert.
- Pro Verfahren eine Datei `gen_ibans/methods/method_XX.py` nach Schema der Referenz.
- Jedes Verfahren bietet mindestens:
  - `@register("XX")`-dekorierte Funktion `validate_method_XX(blz: str, account: str) -> bool`
  - Optional: Hilfsfunktionen; wenn möglich (und effizient), eine dedizierte Generatorfunktion, ansonsten genügt der vorhandene Retry-Generator über den Validator.
- Begleitende Tests pro Verfahren (Unit- und Cross-Checks gegen Referenzdaten). 


## Struktur & Konventionen
- Dateiname: `method_<CODE>.py` (numerisch 00–99 und alphanumerisch A0–E9; bei numerischen Codes zweistellig mit führender Null).
- Öffentliche Signatur: `validate_method_XX(blz: str, account: str) -> bool`.
- Keine Seiteneffekte; nur pure Validierung. BLZ-bezogene Ausnahmen laut Verfahren berücksichtigen (z. B. andere Gewichtungen je Bankgruppe).
- Für Hilfsfunktionen (z. B. Modulo-10/11, iterierte Gewichtungen, Subkontomasken) intern im jeweiligen File implementieren oder in kleinen gemeinsamen Utils (nur wenn es mehrfach benutzt wird – aktuell vermeiden, bis klarer Bedarf besteht).


## Arbeits-Workflow pro Methode
1. Spezifikation lesen (Bundesbank-Dokument; ggf. Beispiele und Sonderfälle notieren).
2. Referenzcode (Repo oben) anschauen, aber nicht blind kopieren; Logik nachvollziehen und äquivalent implementieren.
3. Implementationsschritte:
   - Datei `gen_ibans/methods/method_XX.py` anlegen.
   - `@register("XX")` + `validate_method_XX(...)` implementieren.
   - Falls Verfahren mehrere Varianten (a/b/c) kennt, innerhalb derselben Datei kapseln und im Validator korrekt verzweigen (ggf. anhand BLZ, Kontonummer-Länge, Startziffern, etc.).
4. Tests erstellen:
   - Positiv-/Negativfälle: bekannte gültige/ungültige Kontonummern (sofern vorhanden) bzw. synthetische Fälle anhand der Spezifikation.
   - Property-Tests: Alle generierten Nummern müssen den Validator bestehen; leichte Mutationstests (z. B. letzte Stelle ändern) sollten meist fehlschlagen.
5. Lauf `pytest`, sicherstellen, dass bestehende Tests weiter grün sind.
6. Bei Bedarf Performance prüfen (Retry-Schleife bei seltenen Validen kann teuer werden). Für schwierige Verfahren ggf. direkten Erzeuger implementieren.


## Priorisierung (erste Iteration)
Empfehlung: Zuerst die am häufigsten auftretenden/verbreiteten „Standard“-Verfahren umsetzen. Aus der Referenz ergeben sich u. a. folgende Gruppen:
- Modulo-10/11-Verfahren mit festen Gewichtungen
- Verfahren mit Kontonummer-Segmenten (Stamm-/Unterkonto) 
- Verfahren mit Ausnahmeregeln abhängig von BLZ oder Kontonummer-Präfix

Startvorschlag (alphabetisch nach Code ist nicht sinnvoll – stattdessen nach Komplexität/Verbreitung):
1) 01, 02, 03, 04 (häufige Basismethoden Mod 10/11 mit Gewichtungen) – erledigt ✓ 
2) 06, 07, 08 (weitere Varianten mit Sonderregeln) – erledigt ✓
3) 09, 10, 11, 12, 13 (09, 10 und 13 sind bereits umgesetzt; 11/12 folgen)
4) 20er-Bereich (24 ist bereits umgesetzt; übrige 20er bei Bedarf anschließend)
5) Restliche Methoden inkl. Sonder-/Gruppenverfahren

Hinweis: Exakte Reihenfolge kann nach tatsächlicher BLZ-Verteilung in realen Bundesbankdaten feinjustiert werden.


## Teststrategie
- Unit-Tests pro Methode: `tests/methods/test_method_XX.py` (neu anlegen)
  - Mindestens 3–5 Positiv- und 3–5 Negativfälle pro Variante.
  - Edge-Cases: führende Nullen, Maximal-/Minimal-Längen laut Verfahren, Ausnahmetabellen.
- Integrations-Tests:
  - Über `IBANGenerator`: Für Banken mit bekannter Methode validieren, dass kontonummernbezogene Regeln eingehalten werden (Smoke-Tests, keine massiven Fixtures nötig).
- Cross-Check (optional): Gegen die Referenz-Implementierung (falls lizenzkonform möglich) oder anhand offizieller Testdatensätze (sofern verfügbar).


## Wichtige Edge Cases
- Kontonummern mit führenden Nullen.
- Verfahren, die unterschiedliche Pfade je Kontonummer-Länge/Teilsegment gehen.
- BLZ-spezifische Sonderfälle (Whitelist/Blacklist; verfahrensinterne Umleitungen).
- Verfahren, die bei „invalid“ in ein Fallbackverfahren wechseln (laut Spezifikation gibt es solche Hinweise bei einigen Methoden).
- Kontonummern, die formal 10-stellig formatierbar sind, aber intern weniger signifikante Stellen haben.


## Metriken & Qualitätssicherung
- Für jede fertiggestellte Methode: 
  - Tests grün, 
  - Code-Coverage für die jeweilige Datei >= 95%,
  - Kurzer Eintrag in CHANGELOG mit Referenz auf Verfahren.


## Geplante Dateien (Checkliste)
- [x] gen_ibans/methods/__init__.py (Registry, Generator via Retry)
- [x] gen_ibans/methods/method_00.py (kein Check)
- [x] gen_ibans/methods/method_01.py
- [x] gen_ibans/methods/method_02.py
- [x] gen_ibans/methods/method_03.py
- [x] gen_ibans/methods/method_04.py
- [x] gen_ibans/methods/method_05.py
- [x] gen_ibans/methods/method_06.py
- [x] gen_ibans/methods/method_07.py
- [x] gen_ibans/methods/method_08.py
- [x] gen_ibans/methods/method_09.py
- [x] gen_ibans/methods/method_10.py
- [ ] gen_ibans/methods/method_11.py
- [ ] gen_ibans/methods/method_12.py
- [x] gen_ibans/methods/method_13.py
- [ ] gen_ibans/methods/method_14.py
- [ ] gen_ibans/methods/method_15.py
- [ ] gen_ibans/methods/method_16.py
- [x] gen_ibans/methods/method_17.py
- [ ] gen_ibans/methods/method_18.py
- [ ] gen_ibans/methods/method_19.py
- [ ] gen_ibans/methods/method_20.py
- [ ] gen_ibans/methods/method_21.py
- [ ] gen_ibans/methods/method_22.py
- [ ] gen_ibans/methods/method_23.py
- [x] gen_ibans/methods/method_24.py
- [ ] gen_ibans/methods/method_25.py
- [ ] gen_ibans/methods/method_26.py
- [ ] gen_ibans/methods/method_27.py
- [ ] gen_ibans/methods/method_28.py
- [ ] gen_ibans/methods/method_29.py
- [ ] gen_ibans/methods/method_30.py
- [ ] gen_ibans/methods/method_31.py
- [ ] gen_ibans/methods/method_32.py
- [ ] gen_ibans/methods/method_33.py
- [ ] gen_ibans/methods/method_34.py
- [ ] gen_ibans/methods/method_35.py
- [ ] gen_ibans/methods/method_36.py
- [ ] gen_ibans/methods/method_37.py
- [ ] gen_ibans/methods/method_38.py
- [ ] gen_ibans/methods/method_39.py
- [ ] gen_ibans/methods/method_40.py
- [ ] gen_ibans/methods/method_41.py
- [ ] gen_ibans/methods/method_42.py
- [ ] gen_ibans/methods/method_43.py
- [ ] gen_ibans/methods/method_44.py
- [ ] gen_ibans/methods/method_45.py
- [ ] gen_ibans/methods/method_46.py
- [ ] gen_ibans/methods/method_47.py
- [ ] gen_ibans/methods/method_48.py
- [ ] gen_ibans/methods/method_49.py
- [ ] gen_ibans/methods/method_50.py
- [ ] gen_ibans/methods/method_51.py
- [ ] gen_ibans/methods/method_52.py
- [ ] gen_ibans/methods/method_53.py
- [ ] gen_ibans/methods/method_54.py
- [ ] gen_ibans/methods/method_55.py
- [ ] gen_ibans/methods/method_56.py
- [ ] gen_ibans/methods/method_57.py
- [ ] gen_ibans/methods/method_58.py
- [ ] gen_ibans/methods/method_59.py
- [ ] gen_ibans/methods/method_60.py
- [ ] gen_ibans/methods/method_61.py
- [ ] gen_ibans/methods/method_62.py
- [ ] gen_ibans/methods/method_63.py
- [ ] gen_ibans/methods/method_64.py
- [ ] gen_ibans/methods/method_65.py
- [ ] gen_ibans/methods/method_66.py
- [ ] gen_ibans/methods/method_67.py
- [ ] gen_ibans/methods/method_68.py
- [ ] gen_ibans/methods/method_69.py
- [ ] gen_ibans/methods/method_70.py
- [ ] gen_ibans/methods/method_71.py
- [ ] gen_ibans/methods/method_72.py
- [ ] gen_ibans/methods/method_73.py
- [ ] gen_ibans/methods/method_74.py
- [ ] gen_ibans/methods/method_75.py
- [ ] gen_ibans/methods/method_76.py
- [ ] gen_ibans/methods/method_77.py
- [ ] gen_ibans/methods/method_78.py
- [ ] gen_ibans/methods/method_79.py
- [ ] gen_ibans/methods/method_80.py
- [ ] gen_ibans/methods/method_81.py
- [ ] gen_ibans/methods/method_82.py
- [ ] gen_ibans/methods/method_83.py
- [ ] gen_ibans/methods/method_84.py
- [ ] gen_ibans/methods/method_85.py
- [ ] gen_ibans/methods/method_86.py
- [ ] gen_ibans/methods/method_87.py
- [ ] gen_ibans/methods/method_88.py
- [ ] gen_ibans/methods/method_89.py
- [ ] gen_ibans/methods/method_90.py
- [ ] gen_ibans/methods/method_91.py
- [ ] gen_ibans/methods/method_92.py
- [ ] gen_ibans/methods/method_93.py
- [ ] gen_ibans/methods/method_94.py
- [ ] gen_ibans/methods/method_95.py
- [ ] gen_ibans/methods/method_96.py
- [ ] gen_ibans/methods/method_97.py
- [ ] gen_ibans/methods/method_98.py
- [ ] gen_ibans/methods/method_99.py
- [ ] gen_ibans/methods/method_A0.py
- [ ] gen_ibans/methods/method_A1.py
- [ ] gen_ibans/methods/method_A2.py
- [ ] gen_ibans/methods/method_A3.py
- [ ] gen_ibans/methods/method_A4.py
- [ ] gen_ibans/methods/method_A5.py
- [ ] gen_ibans/methods/method_A6.py
- [ ] gen_ibans/methods/method_A7.py
- [ ] gen_ibans/methods/method_A8.py
- [ ] gen_ibans/methods/method_A9.py
- [ ] gen_ibans/methods/method_B0.py
- [ ] gen_ibans/methods/method_B1.py
- [ ] gen_ibans/methods/method_B2.py
- [ ] gen_ibans/methods/method_B3.py
- [ ] gen_ibans/methods/method_B4.py
- [ ] gen_ibans/methods/method_B5.py
- [ ] gen_ibans/methods/method_B6.py
- [ ] gen_ibans/methods/method_B7.py
- [ ] gen_ibans/methods/method_B8.py
- [ ] gen_ibans/methods/method_B9.py
- [ ] gen_ibans/methods/method_C0.py
- [ ] gen_ibans/methods/method_C1.py
- [ ] gen_ibans/methods/method_C2.py
- [ ] gen_ibans/methods/method_C3.py
- [ ] gen_ibans/methods/method_C4.py
- [ ] gen_ibans/methods/method_C5.py
- [ ] gen_ibans/methods/method_C6.py
- [ ] gen_ibans/methods/method_C7.py
- [ ] gen_ibans/methods/method_C8.py
- [ ] gen_ibans/methods/method_C9.py
- [ ] gen_ibans/methods/method_D0.py
- [ ] gen_ibans/methods/method_D1.py
- [ ] gen_ibans/methods/method_D2.py
- [ ] gen_ibans/methods/method_D3.py
- [ ] gen_ibans/methods/method_D4.py
- [ ] gen_ibans/methods/method_D5.py
- [ ] gen_ibans/methods/method_D6.py
- [ ] gen_ibans/methods/method_D7.py
- [ ] gen_ibans/methods/method_D8.py
- [ ] gen_ibans/methods/method_D9.py
- [ ] gen_ibans/methods/method_E0.py
- [ ] gen_ibans/methods/method_E1.py
- [ ] gen_ibans/methods/method_E2.py
- [ ] gen_ibans/methods/method_E3.py
- [ ] gen_ibans/methods/method_E4.py
- [ ] gen_ibans/methods/method_E5.py
- [ ] gen_ibans/methods/method_E6.py
- [ ] gen_ibans/methods/method_E7.py
- [ ] gen_ibans/methods/method_E8.py
- [ ] gen_ibans/methods/method_E9.py

Hinweis: Die Bundesbank definiert Methodencodes im Bereich 00–99 sowie zusätzlich alphanumerische Serien (A0–E9). Nicht alle Codes sind zwingend belegt oder aktuell im Einsatz; die Liste dient als vollständige Checkliste. Einige Verfahren sind Gruppen-/Variantenverfahren – bitte jeweils sauber dokumentieren.


## Beispiel: Schablone für eine Methode
Datei: `gen_ibans/methods/method_01.py`
```python
"""
Method 01: (Kurzbeschreibung laut Bundesbank)
- Rechenschritte …
- Gewichtungen …
- Sonderfälle …
Referenz: Link/Abschnitt
"""
from . import register

@register("01")
def validate_method_01(blz: str, account: str) -> bool:
    # 1) Vorbedingungen: Länge, nur Ziffern
    if len(account) != 10 or not account.isdigit():
        return False
    # 2) Rechenschritte je Spezifikation …
    # weights = [...]
    # sum_ = ...
    # check = ...
    # 3) Ergebnis zurückgeben
    return computed_check == expected
```


## CI & Regressionen
- Tests laufen via `pytest` und bestehender CI.
- Bei Änderungen an Parsern/CSV/XML bitte darauf achten, dass `method_code` korrekt eingelesen bleibt.


## Meilensteine
1) Basis-Familien (Mod10/Mod11 Standard) umgesetzt (>= 8 Verfahren) – Ziel: 1. Iteration.
2) Platzhalter (09, 13, 24) ersetzt – erreicht in 1. Iteration.
3) Verfahren mit Sonderwegen/BLZ-Abhängigkeiten – Ziel: 2. Iteration.
4) Vollständige Abdeckung und > 95% Test-Coverage pro `gen_ibans/methods/*` – Ziel: 3. Iteration.


## Offene Punkte / Notizen
- Prüfen, ob wir generische Utils (z. B. „mod11_weighted(sum, weights)“) zentralisieren wollen; zunächst pro Methode lokal halten, um versehentliche Verhaltenskopplung zu vermeiden.
- Falls echte Bundesbank-Beispieldaten vorliegen, Test-Fixtures daraus ableiten.
- Performance im Blick behalten: Falls ein Verfahren sehr geringe Trefferquote in der Retry-Erzeugung hat, einen zielgerichteten Generator ergänzen.
