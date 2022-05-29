from questions.question2 import fetch_top5_trades_symbols_with_specific_quote_asset


def test_fetch_top5_trades_symbols_with_specific_quote_asset():
    result = fetch_top5_trades_symbols_with_specific_quote_asset()
    print(result)
    assert type(result[0]) == str
    assert len(result) == 5
