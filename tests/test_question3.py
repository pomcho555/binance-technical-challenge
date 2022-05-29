from questions.question3 import get_total_notional_value_top_200_transaction


def test_get_total_notional_value_top_200_transaction():
    result = get_total_notional_value_top_200_transaction()
    print(result)
    assert len(result) == 5
    one_sample = result[list(result.keys())[0]]
    assert one_sample["total"] == one_sample["bids"] + one_sample["asks"]
