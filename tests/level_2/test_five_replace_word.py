from functions.level_2.five_replace_word import replace_word
import pytest

def test__replace_word__success_replacement():
    test_text = "Good morning kids ! Welcome to school !"
    test_replace_from = "kids"
    test_replace_to = "fellows"

    word_replacement = replace_word(
        text = test_text,
        replace_from = test_replace_from,
        replace_to = test_replace_to
    )
    
    expected_result = "Good morning fellows ! Welcome to school !"

    assert word_replacement == expected_result


def test__replace_word__not_str_replace_from():
    test_text = "Good morning kids ! Welcome to school !"
    test_replace_from = 000
    test_replace_to = "fellows"

    with pytest.raises(AttributeError):
        replace_word(
            text = test_text,
            replace_from = test_replace_from,
            replace_to = test_replace_to
        )


def test__replace_word__not_str_replace_to():
    test_text = "Good morning kids ! Welcome to school !"
    test_replace_from = "kids"
    test_replace_to = None

    with pytest.raises(TypeError):
        replace_word(
            text = test_text,
            replace_from = test_replace_from,
            replace_to = test_replace_to
        )


if __name__ == "__main__":
    func_test = replace_word(
        text = "Good morning kids ! Welcom to school !",
        replace_from = "kids",
        replace_to = "fellows"
    )
    print(func_test)