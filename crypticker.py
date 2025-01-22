#!/bin/python3

import ccxt
import os
import time

def get_exchange():
    """Initialisiere die Binance-Börse mit ccxt."""
    try:
        exchange = ccxt.binance()
        return exchange
    except Exception as e:
        print(f"Fehler beim Initialisieren der Börse: {e}")
        exit()

def list_all_symbols(exchange):
    """Zeige alle verfügbaren Handelspaare auf Binance an."""
    try:
        markets = exchange.load_markets()
        symbols = list(markets.keys())
        return symbols
    except Exception as e:
        print(f"Fehler beim Abrufen der Symbole: {e}")
        return []

def filter_symbols_by_user_input(symbols, user_input):
    """Filtere Symbole basierend auf der Benutzereingabe (z.B. LTC, BTC)."""
    user_tokens = [token.strip().upper() for token in user_input.split(',')]
    filtered_symbols = [f"{token}/USDT" for token in user_tokens if f"{token}/USDT" in symbols]
    os.system(command="clear")
    return filtered_symbols

def fetch_ticker_data(exchange, symbol):
    """Hole die Ticker-Daten für ein bestimmtes Symbol (einschließlich Hoch und Tief des Tages)."""
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker
    except Exception as e:
        print(f"Fehler beim Abrufen der Ticker-Daten für {symbol}: {e}")
        return None

def calculate_volatility(high, low):
    """Berechne die Volatilität in Prozent basierend auf dem Tageshoch und Tagestief."""
    if high and low:
        volatility = (high - low) / low * 100  # Volatilität in %
        return volatility
    return None

def get_usd_to_eur_rate(exchange):
    """Hole den aktuellen USD/EUR-Wechselkurs."""
    try:
        ticker = exchange.fetch_ticker("EUR/USDT")
        usd_to_eur = 1 / ticker['last']  # Da EUR/USDT = wie viele USDT pro EUR
        return usd_to_eur
    except Exception as e:
        print(f"Fehler beim Abrufen des USD/EUR-Wechselkurses: {e}")
        return None

def display_prices(exchange, symbols):
    """Zeige die aktuellen Preise, Volatilität, Tageshoch und -tief in EUR für ausgewählte Symbole an."""
    try:
        usd_to_eur_rate = get_usd_to_eur_rate(exchange)
        if usd_to_eur_rate is None:
            print("Wechselkurs nicht verfügbar. Abbruch.")
            return
        
        # Initiale Ausgabe für jedes Symbol
        for symbol in symbols:
            print(f"{symbol}: Lade Daten...", end="\r")

        previous_prices = {symbol: None for symbol in symbols}

        while True:
            # Aktualisiere die Preise und Volatilität ohne Zeilenumbruch
            for symbol in symbols:
                ticker = fetch_ticker_data(exchange, symbol)
                if ticker:
                    high = ticker['high']
                    low = ticker['low']
                    volatility = calculate_volatility(high, low)
                    price_usd = ticker['last']
                    
                    if price_usd is not None:
                        # Berechne Preise in EUR und runde auf 2 Dezimalstellen für Berechnungen
                        price_eur = price_usd * usd_to_eur_rate  # Alle Dezimalstellen für die Anzeige
                        high_eur = high * usd_to_eur_rate if high else None
                        low_eur = low * usd_to_eur_rate if low else None

                        # Berechne die Preisveränderung auf Basis der ersten zwei Dezimalstellen
                        price_eur_rounded = round(price_eur, 2)  # Preis auf 2 Dezimalstellen für die Berechnung
                        previous_price_rounded = round(previous_prices[symbol], 2) if previous_prices[symbol] else None

                        # Berechne die Farbe: Grün, wenn der Preis steigt, Rot, wenn er fällt
                        color = "\033[32m" if previous_price_rounded is None or price_eur_rounded > previous_price_rounded else "\033[31m"
                        previous_prices[symbol] = price_eur

                        # Überschreibe die Zeile mit den neuen Daten und färbe den Text
                        print(f"\r{color}{symbol} >> {price_eur:.4f} EUR << Volatilität: {volatility:.2f}% | Tageshoch: {high_eur:.4f} EUR | Tagestief: {low_eur:.4f} EUR\033[0m", end="")
                        time.sleep(5)
                    else:
                        print(f"\r{symbol} Preis nicht verfügbar", end="")
                else:
                    print(f"\r{symbol}: Ticker-Daten nicht verfügbar", end="")
            time.sleep(0.1)  # Aktualisierung alle 1 Sekunde
    except KeyboardInterrupt:
        print("\nProgramm wurde abgebrochen. Bis zum nächsten Mal!")

if __name__ == "__main__":
    try:
        exchange = get_exchange()
        all_symbols = list_all_symbols(exchange)
        if all_symbols:
            print("Gib die gewünschten Coins ein (z.B. LTC,BTC,SOL):")
            user_input = input("Deine Auswahl: ")
            selected_symbols = filter_symbols_by_user_input(all_symbols, user_input)
            if selected_symbols:
                display_prices(exchange, selected_symbols)
            else:
                print("Keine passenden Symbole gefunden.")
        else:
            print("Keine Symbole verfügbar.")
    except KeyboardInterrupt:
        print("\nProgramm wurde abgebrochen. Bis zum nächsten Mal!")
