import pytest
from questions.utils import (
    fetch_all_symbols,
    fetch_top5_symbols_with_specific_quote_asset,
)


@pytest.mark.parametrize(
    "test_quote_asset",
    ["BTC", "USDT"],
)
def test_fetch_all_symbols(test_quote_asset):
    result = fetch_all_symbols(quote_asset=test_quote_asset)
    assert type(result) == list
    assert result[0][-len(test_quote_asset) :] == test_quote_asset  # noqa


def test_fetch_top5_symbols_with_specific_quote_asset():
    result = fetch_top5_symbols_with_specific_quote_asset("USDT", "count")
    assert type(result[0]) == str
    assert len(result) == 5
