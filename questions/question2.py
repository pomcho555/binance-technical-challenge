from questions.utils import fetch_top5_symbols_with_specific_quote_asset


def fetch_top5_trades_symbols_with_specific_quote_asset() -> list:
    """Fetch top5 the highest number of trades symbols with specific quote asset.

    Returns:
        list: top 5 higher volume symbols.
        e.g. ['SKLBTC', 'XLMBTC', 'CKBBTC', 'HIGHBTC', 'KLAYBTC']
    """
    return fetch_top5_symbols_with_specific_quote_asset("USDT", "count")


def print_answer():
    print(fetch_top5_trades_symbols_with_specific_quote_asset())
