import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,expected_result",
    [
        ("He codes tests.", "She codes tests.", "male", "He codes tests."),
        ("He codes tests.", "She codes tests.", "female", "She codes tests."),
        ("He codes tests.", "She codes tests.", "she", "She codes tests."),
        ("He codes tests.", "She codes tests.", "he", "She codes tests."),
    ]
)
def test__genderalize__returns_correct_verb_according_to_specified_gender(
    verb_male, verb_female, gender, expected_result
):
    assert genderalize(verb_male, verb_female, gender) == expected_result
