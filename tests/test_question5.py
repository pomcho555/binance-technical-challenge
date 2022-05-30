from collections import defaultdict

from questions.question5 import print_spread_each_symbol


def test_print_spread_each_symbol():
    previous_spreads = defaultdict()
    result = print_spread_each_symbol()
    # print(result)
    for s in result:
        assert len(result) == 5
        assert type(result[s]["spread"]) == float
        assert result[s]["delta"] == result[s]["spread"]
        previous_spreads[s] = result[s]["spread"]

    result2 = print_spread_each_symbol()
    # Check delta correctness.
    for s in result2:
        assert result2[s]["delta"] == abs(previous_spreads[s] - result2[s]["spread"])
