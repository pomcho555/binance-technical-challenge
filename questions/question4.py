import configparser

from binance.spot import Spot as Client

from questions.question2 import fetch_top5_trades_symbols_with_specific_quote_asset

Config = configparser.ConfigParser()
Config.read("config.ini")

client = Client(base_url=Config.get("API", "BaseUrl"))


def get_spread_each_symbols(symbols: list) -> dict:
    """Get the price spread for each of the symbols from Q2.

    Args:
        symbols (list): target symbols you want to calculate spread.
            e.g. ['LUNAUSDT', 'BTCUSDT', ... ]

    Returns:
        dict: the key value pair of symbol and spread.
            e.g. {'BTCUSDT': 0.00999999999839929, ... }
    """
    result = client.ticker_24hr(symbols=symbols)
    spreads = {}
    for s in result:
        spreads[s["symbol"]] = abs(float(s["bidPrice"]) - float(s["askPrice"]))

    return spreads


def get_q4_result():
    # Fetch q2 result
    question2_symbols = fetch_top5_trades_symbols_with_specific_quote_asset()
    get_spread_each_symbols(question2_symbols)


def print_answer():
    print("====Q4 ANSWER====")
    print(get_q4_result())
