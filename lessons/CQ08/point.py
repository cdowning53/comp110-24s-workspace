"""Taking a point and changing it via mutating and non-mutating methods."""

from __future__ import annotations

__author__ = "730482646"


class Point:
    """Creating a class to represent a point which will then be modified by the other functions."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor that assigns the two inputs as the initial values."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates a Point through updating it via multiplying it by the factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Returns point through a non-mutative method."""
        new_point_x = self.x * factor
        new_point_y = self.y * factor
        return Point(new_point_x, new_point_y)