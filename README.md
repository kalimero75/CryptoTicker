Crypto Price Tracker
Ein Python-basiertes Tool zur Überwachung von Kryptowährungspreisen in Echtzeit, das mit der CCXT-Bibliothek arbeitet. Es bietet eine intuitive Möglichkeit, Preisdaten, Tageshöchst- und -tiefststände sowie die Volatilität ausgewählter Kryptowährungen anzuzeigen. Das Tool eignet sich hervorragend für Trader und Entwickler, die Marktbewegungen live verfolgen möchten.

Funktionen
Echtzeit-Preisüberwachung: Verfolge die aktuellen Preise deiner ausgewählten Kryptowährungen in Euro, mit kontinuierlichen Updates.

Unterstützung für mehrere Kryptowährungen: Gib mehrere Symbole (z. B. BTC, ETH, LTC) ein, um Preise und andere Daten gleichzeitig zu verfolgen.

Berechnung der Volatilität: Das Tool berechnet die tägliche Volatilität (%) basierend auf dem Tageshoch und -tief.

Datenanzeige in EUR: Alle Preisdaten werden automatisch von USD in EUR umgerechnet, basierend auf dem aktuellen USD/EUR-Wechselkurs.

Farblich kodierte Preisänderungen:

Grün: Der Preis ist gestiegen.
Rot: Der Preis ist gefallen.
Robuste Fehlerbehandlung: Das Tool enthält eine Retry-Logik, um vorübergehende Netzwerkprobleme zu handhaben, sowie aussagekräftige Fehlermeldungen und Logging.

Einfache Bedienung: Durch eine Eingabeaufforderung kannst du leicht die Symbole der Kryptowährungen auswählen, die du überwachen möchtest.

Möglichkeiten
Live-Preis-Tracking für Trading-Strategien: Überwache in Echtzeit Preisbewegungen und Volatilität, um fundierte Trading-Entscheidungen zu treffen.

Anpassbare Symbolauswahl: Wähle flexibel die Kryptowährungen aus, die für dich relevant sind.

Marktanalysen und Reporting: Die tägliche Volatilitätsanzeige eignet sich hervorragend zur Analyse der Marktstabilität.

Erweiterbar: Dank der Verwendung von ccxt kannst du das Tool leicht an andere Börsen oder Funktionen anpassen, wie z. B. historische Daten oder Orderbuch-Informationen.

Verwendung
Voraussetzungen
Python 3.7 oder höher
Installierte Abhängigkeiten (ccxt und tabulate)

pip install ccxt tabulate


python crypticker.py
Gib die gewünschten Kryptowährungen ein, getrennt durch Kommas (z. B. BTC,ETH,LTC).


BTC/USDT: 27500.23 EUR | Volatilität: 2.34% | Tageshoch: 28000.00 EUR | Tagestief: 27000.00 EUR
ETH/USDT: 1800.12 EUR | Volatilität: 1.89% | Tageshoch: 1850.00 EUR | Tagestief: 1750.00 EUR
Abbrechen des Tools
Drücke Strg+C, um das Tool zu stoppen.

Zukünftige Verbesserungen
Unterstützung für mehr Währungspaare (z. B. BTC/EUR direkt).
Visualisierung der Preisdaten (z. B. mit Diagrammen).
Integration zusätzlicher Börsen und Märkte.
Alarmfunktion bei Erreichen bestimmter Preisniveaus.
