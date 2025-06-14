from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    """Test for the base case"""
    assert change_copy_item("Final_version") == "Copy of Final_version"

def test_change_copy_item_with_copy():
    """Test when the title has a copy in it"""
    assert change_copy_item("Copy of Final_version") == "Copy of Final_version (2)"
