"""Using three unit tests to check each dictionary function."""

__author__ = "730482646"

import pytest
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_edge_case() -> None:
    """Tests the invert function with an edge case."""
    with pytest.raises(KeyError):
        dictionary_list = {"hey": "hello", "hi": "hello"}
        invert(dictionary_list)


def test_invert_use_case_one() -> None:
    """Tests the invert function with the first use case."""
    dictionary_list: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(dictionary_list) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_two() -> None:
    """Tests the invert function with the second use case which is more complex."""
    dictionary_list: dict[str, str] = {"first": "one", "second": "two", "third": "three"}
    assert invert(dictionary_list) == {"one": "first", "two": "second", "three": "third"}


def test_favorite_color_edge_case() -> None:
    """Tests the favorite color function with an edge case."""
    color_dict = {"Nio": "black", "Priscilla": "green", "Malo": "blue"}
    assert favorite_color(color_dict) == ""


def test_favorite_color_use_case_one() -> None:
    """Tests the favorite color function with a use case."""
    color_dict = {"Nio": "black", "Priscilla": "black", "Malo": "blue"}
    assert favorite_color(color_dict) == "black"


def test_favorite_color_use_case_two() -> None:
    """Tests the favorite color function with another use case."""
    color_dict = {"Connor": "black", "Katie": "pink", "Nathan": "blue", "Rhea": "pink"}
    assert favorite_color(color_dict) == "pink"


def test_count_edge_case() -> None:
    """Tests the count function with an edge case."""
    value_list = []
    assert count(value_list) == {}


def test_count_use_case_one() -> None:
    """Tests the count function with a use case involving just numbers."""
    value_list = ["1", "2", "3", "1", "2", "3"]
    assert count(value_list) == {"1": 2, "2": 2, "3": 2}


def test_count_use_case_two() -> None:
    """Tests the count function with another use case involving words."""
    value_list = ["soccer", "tennis", "soccer", "soccer"]
    assert count(value_list) == {"soccer": 3, "tennis": 1}


def test_alphabetizer_edge_case() -> None:
    """Tests the alphabetizer function with an edge case."""
    word_list = []
    assert alphabetizer(word_list) == {}


def test_alphabetizer_use_case_one() -> None:
    """Tests the alphabetizer function with a use case involving one word for different letters."""
    word_list = ["farewell", "goodbye", "hello"]
    assert alphabetizer(word_list) == {"f": ["farewell"], "g": ["goodbye"], "h": ["hello"]}


def test_alphabetizer_use_case_two() -> None:
    """Tests the alphabetizer function with a use case involving multiple words belonging to different letters."""
    word_list = ["aries", "aquarius", "sagittarius", "scorpio"]
    assert alphabetizer(word_list) == {"a": ["aries", "aquarius"], "s": ["sagittarius", "scorpio"]}


def test_update_attendance_edge_case() -> None:
    """Tests the update attendance function with an edge case."""
    student_attendance = {}
    day = "Monday"
    name = "Jane"
    update_attendance(student_attendance, day, name)
    assert student_attendance == {"Monday": ["Jane"]}


def test_update_attendance_use_case_one() -> None:
    """Tests the update attendance function with a use case."""
    student_attendance = {"Monday": ["Connor", "Jane"]}
    day = "Monday"
    name = "Aya"
    update_attendance(student_attendance, day, name)
    assert student_attendance == {"Monday": ["Connor", "Jane", "Aya"]}


def test_update_attendance_use_case_two() -> None:
    """Tests the update attendance function with another use case."""
    student_attendance = {"Monday": ["Aya", "Jane"], "Tuesday": ["Jane"], "Wednesday": ["Aya"]}
    day = "Thursday"
    name = "Connor"
    update_attendance(student_attendance, day, name)
    assert student_attendance == {"Monday": ["Aya", "Jane"], "Tuesday": ["Jane"], "Wednesday": ["Aya"], "Thursday": ["Connor"]}