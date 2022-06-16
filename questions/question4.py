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
    results = [client.depth(symbol=s, limit=1) for s in symbols]
    spreads = {}
    for s, r in zip(symbols, results):

        try:
            spreads[s] = abs(float(r["bids"][0][0]) - float(r["asks"][0][0]))
        except IndexError:
            # Sometimes, there is no response from depth API.
            # USTUSDT {'lastUpdateId': 63603045, 'bids': [], 'asks': []}
            spreads[s] = 0.0
    return spreads


def get_q4_result():
    # Fetch q2 result
    question2_symbols = fetch_top5_trades_symbols_with_specific_quote_asset()
    return get_spread_each_symbols(question2_symbols)


def print_answer():
    print("====Q4 ANSWER====")
    print(get_q4_result())
