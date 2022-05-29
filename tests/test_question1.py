from questions.question1 import (
    fetch_all_symbols,
    fetch_top5_volume_symbols_with_specific_quote_asset,
)


def test_fetch_top5_volume_symbols_with_specific_quote_asset():
    assert len(fetch_top5_volume_symbols_with_specific_quote_asset("BTC")) == 5


def test_fetch_all_symbols():
    result = fetch_all_symbols(quote_asset="BTC")
    assert type(result) == list
    assert result[0][-3:] == "BTC"
