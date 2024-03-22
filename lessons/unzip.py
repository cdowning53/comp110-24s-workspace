"""Splitting a dictionary into two lists."""

__author__ = "730482646"


def get_keys(test_dict: dict[str, int]) -> list[str]:
    """Returns the strings of the dictionary."""
    word_list: list[str] = []
    for words in test_dict:
        word_list.append(words)
    return word_list


def get_values(test_dict: dict[str, int]) -> list[int]:
    """Returns the values of the dictionary."""
    number_list: list[int] = []
    for number in test_dict:
        number_list.append(test_dict[number])
    return number_list    