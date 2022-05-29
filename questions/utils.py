"""
This file collect some common function across by many modules.
"""
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
        list: list of symbols. e.g. ['LUNAUSDT', 'GMTUSDT', 'USTUSDT', 'BTCUSDT']
    """
    exchange_info = client.exchange_info()
    if not quote_asset:
        return [i["symbol"] for i in exchange_info["symbols"]]
    all_symbols = []
    for s in exchange_info["symbols"]:
        if s["symbol"][-len(quote_asset) :] == quote_asset:  # noqa
            all_symbols.append(s["symbol"])
    return all_symbols


def fetch_top5_symbols_with_specific_quote_asset(
    quote_asset: str, specific_field: str
) -> list:
    """Fetch top5 symbols with specific quote asset ordered by a specific field.

    Args:
        quote_asset (str): Specify a quote asset such as BTC.
        specific_field (str): Specify a field such as volume and count.
            You can use a field from below response:
            https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

    Returns:
        list: top 5 higher symbols with a specific field such as volume.
        e.g. ['SKLBTC', 'XLMBTC', 'CKBBTC', 'HIGHBTC', 'KLAYBTC']
    """
    target_symbols = fetch_all_symbols(quote_asset=quote_asset)

    # TODO: Write exception handler
    result = client.ticker_24hr(symbols=target_symbols)
    if specific_field not in result[0].keys():
        raise Exception("A specific_field is not valid! Use a valid field.")

    volumes = {s["symbol"]: s[specific_field] for s in result}
    sorted_volumes = sorted(volumes.items(), key=lambda x: x[1], reverse=True)
    return [s[0] for s in sorted_volumes[:5]]
