from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize(
        verb_male="He codes tests.", verb_female="She codes tests.", gender="male"
        ) == "He codes tests."
    assert genderalize(
        verb_male="He codes tests.", verb_female="She codes tests.", gender="female"
        ) == "She codes tests."
    assert genderalize(
        verb_male="He codes tests.", verb_female="She codes tests.", gender="she"
    ) == "She codes tests."