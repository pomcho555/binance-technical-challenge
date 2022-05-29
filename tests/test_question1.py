from questions.question1 import fetch_top5_volume_symbols_with_specific_quote_asset


def test_fetch_top5_volume_symbols_with_specific_quote_asset():
    assert len(fetch_top5_volume_symbols_with_specific_quote_asset()) == 5
