from functions.level_2.three_first import first, NOT_SET
import pytest


def test__first__items_not_empty_int():
    test_items = [1, 2, 3]
    default_value = 42

    first_result = first(
        items=test_items,
        default=default_value
    )

    assert first_result == 1


def test__first__items_not_empty_str():
    test_items = ['string', 2, 3]
    default_value = 42

    first_result = first(
        items=test_items,
        default=default_value
    )

    assert first_result == 'string'


def test__first__items_empty_returns_default_int():
    test_items = []
    default_value = 42

    first_result = first(
        items=test_items,
        default=default_value
    )

    assert first_result == 42


def test__first__items_empty_returns_default_str():
    test_items = []
    default_value = '451'

    first_result = first(
        items=test_items,
        default=default_value
    )

    assert first_result == '451'


def test__first__no_items_no_default():
    test_items = []

    with pytest.raises(AttributeError):
        first(items=test_items)


if __name__ == "__main__":
    # Function run test
    func_result = first(
        items=['f']
    )
    print(f"Function result: {func_result}")