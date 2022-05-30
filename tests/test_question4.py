from questions.question4 import get_spread_each_symbols


def test_get_spread_each_symbols():
    test_symbols = ["LUNAUSDT", "BTCUSDT", "GMTUSDT", "BELUSDT", "USTUSDT"]
    result = get_spread_each_symbols(test_symbols)
    print(result)
    assert len(result) == 5
    assert type(result) == dict
