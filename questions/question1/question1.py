import configparser

from binance.spot import Spot as Client

Config = configparser.ConfigParser()
Config.read("config.ini")

client = Client(base_url=Config.get("API", "BaseUrl"))


def fetch_all_symbols(quote_asset: str = None) -> list:
    """fetch all symbols filtered by specific quote asset

    Args:
        quote_asset (str, optional): Specify a quote asset such as BTC. Defaults to None.

    Returns:
        list: list of symbols. e.g. ['DREPBUSD', 'AKROBUSD', 'PUNDIXBUSD']
    """
    exchange_info = client.exchange_info()
    if not quote_asset:
        return [i["symbol"] for i in exchange_info["symbols"]]
    all_symbols = []
    for s in exchange_info["symbols"]:
        if s["symbol"][-3:] == quote_asset:
            all_symbols.append(s["symbol"])
    return all_symbols


def fetch_top5_volume_symbols_with_specific_quote_asset(quote_asset: str) -> list:
    """Fetch exchange info by specific quote asset

    Args:
        quote_asset (str): Specify a quote asset such as BTC.

    Returns:
        list: top 5 higher volume symbols.
        e.g. ['SKLBTC', 'XLMBTC', 'CKBBTC', 'HIGHBTC', 'KLAYBTC']
    """
    target_symbols = fetch_all_symbols(quote_asset=quote_asset)

    # TODO: Write exception handler
    result = client.ticker_24hr(symbols=target_symbols)
    volumes = {s["symbol"]: s["volume"] for s in result}
    sorted_volumes = sorted(volumes.items(), key=lambda x: x[1], reverse=True)
    return [s[0] for s in sorted_volumes[:5]]


def print_answer():
    print(fetch_top5_volume_symbols_with_specific_quote_asset("BTC"))
