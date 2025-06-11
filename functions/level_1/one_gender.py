def genderalize(verb_male: str, verb_female: str, gender: str) -> str:
    """Returns the verb based on the specified gender."""
    return verb_male if gender == "male" else verb_female


if __name__ == '__main__':
    print(genderalize("He codes tests.", "She codes tests.", "male"))