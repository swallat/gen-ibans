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
- Bereits vorhandene Files:
  - method_00.py (akzeptiert 10-stellige Kontonummern – korrekt für „00“/kein Check)
  - method_09.py (Platzhalter)
  - method_13.py (Platzhalter)
  - method_24.py (Platzhalter)
- `IBANGenerator` nutzt `BankInfo.method_code` und generiert Kontonummern über `gen_ibans.methods.generate_valid_account`.
- Tests der bestehenden Codebasis laufen grün (Stand dieser Session); methodenspezifische Detailtests fehlen noch (geplant).


## Zielbild
- Alle von der Bundesbank definierten Verfahren (00, 01, …, inkl. Sonderfälle/Gruppenvarianten) sind korrekt implementiert.
- Pro Verfahren eine Datei `gen_ibans/methods/method_XX.py` nach Schema der Referenz.
- Jedes Verfahren bietet mindestens:
  - `@register("XX")`-dekorierte Funktion `validate_method_XX(blz: str, account: str) -> bool`
  - Optional: Hilfsfunktionen; wenn möglich (und effizient), eine dedizierte Generatorfunktion, ansonsten genügt der vorhandene Retry-Generator über den Validator.
- Begleitende Tests pro Verfahren (Unit- und Cross-Checks gegen Referenzdaten). 


## Struktur & Konventionen
- Dateiname: `method_XX.py` (zweistellig, führende Null).
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
1) 01, 02, 03, 04 (häufige Basismethoden Mod 10/11 mit Gewichtungen) 
2) 06, 07, 08 (weitere Varianten mit Sonderregeln)
3) 09, 10, 11, 12, 13 (hier: 09/13 sind bereits Platzhalter – ersetzen!)
4) 20er-Bereich (u. a. 24 bereits als Platzhalter – ersetzen)
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
- [ ] gen_ibans/methods/method_01.py
- [ ] gen_ibans/methods/method_02.py
- [ ] gen_ibans/methods/method_03.py
- [ ] gen_ibans/methods/method_04.py
- [ ] gen_ibans/methods/method_05.py
- [ ] gen_ibans/methods/method_06.py
- [ ] gen_ibans/methods/method_07.py
- [ ] gen_ibans/methods/method_08.py
- [ ] gen_ibans/methods/method_09.py (Platzhalter ersetzen)
- [ ] gen_ibans/methods/method_10.py
- [ ] gen_ibans/methods/method_11.py
- [ ] gen_ibans/methods/method_12.py
- [ ] gen_ibans/methods/method_13.py (Platzhalter ersetzen)
- [ ] gen_ibans/methods/method_14.py
- [ ] gen_ibans/methods/method_15.py
- [ ] gen_ibans/methods/method_16.py
- [ ] gen_ibans/methods/method_17.py
- [ ] gen_ibans/methods/method_18.py
- [ ] gen_ibans/methods/method_19.py
- [ ] gen_ibans/methods/method_20.py
- [ ] gen_ibans/methods/method_21.py
- [ ] gen_ibans/methods/method_22.py
- [ ] gen_ibans/methods/method_23.py
- [ ] gen_ibans/methods/method_24.py (Platzhalter ersetzen)
- [ ] … (weitere Codes gemäß Bundesbank-Liste)

Hinweis: Die vollständige Methodenliste bitte aus der Bundesbank-Seite übernehmen und hier ergänzen. Einige Verfahren sind Gruppe/X-Varianten – jeweils sauber dokumentieren.


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
2) Platzhalter (09, 13, 24) ersetzen – Ziel: 1. Iteration.
3) Verfahren mit Sonderwegen/BLZ-Abhängigkeiten – Ziel: 2. Iteration.
4) Vollständige Abdeckung und > 95% Test-Coverage pro `gen_ibans/methods/*` – Ziel: 3. Iteration.


## Offene Punkte / Notizen
- Prüfen, ob wir generische Utils (z. B. „mod11_weighted(sum, weights)“) zentralisieren wollen; zunächst pro Methode lokal halten, um versehentliche Verhaltenskopplung zu vermeiden.
- Falls echte Bundesbank-Beispieldaten vorliegen, Test-Fixtures daraus ableiten.
- Performance im Blick behalten: Falls ein Verfahren sehr geringe Trefferquote in der Retry-Erzeugung hat, einen zielgerichteten Generator ergänzen.
