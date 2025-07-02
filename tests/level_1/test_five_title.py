import pytest
from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title,expected_result",
    [
        ("Final_version", "Copy of Final_version"),
        ("Copy of Final_version", "Copy of Final_version (2)"),
        ("Copy of Final_version (2)", "Copy of Final_version (3)"),
        ("Final_version (2)", "Copy of Final_version (2)"),
        ("Final_version (3)", "Copy of Final_version (3)")
    ]
)
def test__change_copy_item__returns_input_title_with_word_copy_prefix_and_copy_count_postfix(
    title, expected_result
):
    assert change_copy_item(title) == expected_result
