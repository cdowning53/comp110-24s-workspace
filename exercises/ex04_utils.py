"""Using Utility functions for lists."""

__author__ = "730482646"

number_list = list[int]
number = int


def all(number_list: list[int], number: int) -> bool:
    """Checks to see if all numbers inside the list match the typed number."""
    if len(number_list) == 0:
        return False
    
    for elem in number_list:
        if elem != number:
            return False
    return True


def max(input: list[int]) -> int:
    """Provides the maximum number out of the entire list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    
    max_value = input[0]
    for number in input:
        if number > max_value:
            max_value = number
    return max_value


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if the two inputted lists are equal to one another."""
    if len(list_one) != len(list_two):
        return False
    
    for i in range(len(list_one)):
        if list_one[i] != list_two[i]:
            return False
    return True


def extend(list_a: list[int], list_b: list[int]) -> None:
    """Extends the lists to be combined."""
    for elem in list_b:
        list_a.append(elem)
