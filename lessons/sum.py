"""Summing the elements of a list using different loops."""

__author__ = "730482646"

vals: list[float] = [1.1, 0.9, 1.0]


def w_sum(vals: list[float]) -> float:
    """Basic sum in a while loop."""
    starting_value = 0.0
    index = 0
    while index < len(vals):
        starting_value += vals[index]
        index += 1
    return starting_value


def f_sum(vals: list[float]) -> float:
    """Using in loops to find the sum."""
    starting_value = 0.0
    for elem in vals:
        starting_value += elem
    return starting_value


def f_range_sum(vals: list[float]) -> float:
    """Using range to find the sum."""
    starting_value = 0.0
    for elem in range(0, len(vals)):
        starting_value += vals[elem]
    return starting_value