from questions.question4 import get_spread_each_symbols


def test_get_spread_each_symbols():
    result = get_spread_each_symbols()
    print(result)
    assert len(result) == 5
    assert type(result) == dict
