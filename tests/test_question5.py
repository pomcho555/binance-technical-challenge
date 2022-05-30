from collections import defaultdict

from questions.question5 import print_spread_each_symbol


def test_print_spread_each_symbol():
    test_symbols = ["LUNAUSDT", "BTCUSDT", "GMTUSDT", "BELUSDT", "USTUSDT"]
    previous_spreads = defaultdict()
    result = print_spread_each_symbol(test_symbols)
    for s in result:
        assert len(result) == 5
        assert type(result[s]["spread"]) == float
        previous_spreads[s] = result[s]["spread"]

    result2 = print_spread_each_symbol(test_symbols)
    # Check delta correctness.
    for s in result2:
        assert result2[s]["delta"] == abs(previous_spreads[s] - result2[s]["spread"])
