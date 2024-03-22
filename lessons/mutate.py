"""Mutating functions."""

__author__ = "730482646"

number_list: list[int] = [1, 2, 3]


def manual_append(number_list: list[int], value: int) -> None:
    """Manually appends function."""
    number_list.append(value)


manual_append(number_list, 2)
print(number_list)

number_list2: list[int] = [1, 2, 3]


def double(number_list2: list[int]) -> None:
    """Doubles function."""
    counter: int = 0
    while len(number_list2) > counter:
        number_list2[counter] *= 2
        counter += 1


double(number_list2)
print(number_list2)
