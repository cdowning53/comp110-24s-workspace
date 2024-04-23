"""Putting recursion into code."""

__author__ = "730482646"


def f(n: int, k: int) -> int:
    """Recursive definition."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)