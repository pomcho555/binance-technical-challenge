import configparser

from binance.spot import Spot as Client

from questions.question1 import fetch_top5_volume_symbols_with_specific_quote_asset

Config = configparser.ConfigParser()
Config.read("config.ini")

client = Client(base_url=Config.get("API", "BaseUrl"))


def get_total_notional_value_top_200_transaction() -> dict:
    """_summary_

    Returns:
        dict: Total notional values each symbols
            e.g. 'IRISBTC': {'total': 30.95195399, 'bids': 1.24807078, 'asks': 29.70388321}, ...}
    """
    # Fetch q1 result
    question1_symbols = fetch_top5_volume_symbols_with_specific_quote_asset()
    # Calculate total notional value each order book
    notional_values = {}
    for s in question1_symbols:
        result = client.depth(symbol=s, limit=200)
        bid_total = 0
        # TODO: Fix time complexity is O(n*:2)!
        for bid in result["bids"]:
            bid_total += float(bid[0]) * float(bid[1])
        ask_total = 0
        for ask in result["asks"]:
            ask_total += float(ask[0]) * float(ask[1])
        notional_values[s] = {
            "total": bid_total + ask_total,
            "bids": bid_total,
            "asks": ask_total,
        }
    return notional_values


def print_answer():
    print("Q3 ANSWER:")
    print(get_total_notional_value_top_200_transaction())
