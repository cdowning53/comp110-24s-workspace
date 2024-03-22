"""Test my garden functions."""

__author__ = "730482646"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_edge() -> None:
    """Tests add_by_kind with an edge case."""
    plants_by_kind = {}
    plant_kind = "flowers"
    plant = "roses"
    add_by_kind(plants_by_kind, plant_kind, plant)
    assert plant_kind in plants_by_kind
    assert plants_by_kind[plant_kind] == ["roses"]


def test_add_by_kind_use() -> None:
    """Tests add_by_kind with a use case."""
    plants_by_kind = {"flowers": ["marigolds", "tulips"]}
    plant_kind = "flowers"
    plant = "roses"
    add_by_kind(plants_by_kind, plant_kind, plant)
    assert "roses" in plants_by_kind[plant_kind]


def test_add_by_date_edge() -> None:
    """Tests add_by_date with an edge case."""
    plants_by_date = {}
    month = "April"
    plant = "elderberry"
    add_by_date(plants_by_date, month, plant)
    assert month in plants_by_date
    assert plants_by_date[month] == ["elderberry"]


def test_add_by_date_use() -> None:
    """Tests add_by_date with a use case."""
    plants_by_date = {"May": ["elderberry"], "June": ["zinnias"]}
    month = "April"
    plant = "daisy"
    add_by_date(plants_by_date, month, plant)
    assert "daisy" in plants_by_date[month]


def test_lookup_by_kind_and_date_edge() -> None:
    """Tests lookup_by_kind_and_date with an edge case."""
    plants_by_kind = {}
    plants_by_date = {}
    plant_kind = "vegetables"
    month = "June"
    plant_statement = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert plant_statement == "No vegetables to plant in June."


def test_lookup_by_kind_and_date_use() -> None:
    """Tests lookup_by_kind_and_date with a use case."""
    plants_by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date = {"April": ["marigold"], "June": ["carrots"]}
    plant_kind = "flowers"
    month = "April"
    plant_statement = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert plant_statement == "flowers to plant in April: ['marigold']"