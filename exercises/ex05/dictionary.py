"""Practicing utilizing different dictionary functions."""

__author__ = "730482646"


def invert(dictionary_list: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary of keys/values inputted in a list."""
    inverted_dict: dict[str, str] = dict()
    switch_list: list[str] = list()
    for words in dictionary_list:
        if dictionary_list[words] in switch_list:
            raise KeyError("Repeat values aren't permitted!!!")
        else:
            switch_list.append(dictionary_list[words])
    for words in dictionary_list:
        inverted_dict[dictionary_list[words]] = words
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """From a dictionary of people's favorite colors, outputs the most popular."""
    color: str
    list_info: dict[str, int] = dict()
    popular_color: int = 0
    for colors in color_dict:
        if color_dict[colors] in list_info:
            list_info[color_dict[colors]] += 1
        else: 
            list_info[color_dict[colors]] = 1
    for elem in list_info:
        if list_info[elem] > popular_color:
            popular_color = list_info[elem]
            color = elem
    return color


def count(value_list: list[str]) -> dict[str, int]:
    """Counts the amount of times a value is in a inputted list."""
    value_dict: dict[str, int] = dict()
    for value in value_list:
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
    return value_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Organizes words in a list based off of the first letter of it's spelling."""
    letter_dict: dict[str, list[str]] = dict()
    for elem in word_list:
        letter = elem[0].lower()
        if letter in letter_dict:
            letter_dict[letter].append(elem)
        else:
            letter_dict[letter] = [elem]
    return letter_dict


def update_attendance(student_attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Checks if a student was present on different days."""
    if day in student_attendance:
        student_attendance[day].append(name)
    else:
        student_attendance[day] = [name]