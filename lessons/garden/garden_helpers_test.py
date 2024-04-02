"""Test my garden functions."""
__author__ = "730461078"


from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date

 
def test_add_by_kind_use_case() -> None:
    """Tests if the function will properly add a new plant and a new plant type to the list."""
    test: dict[str, list[str]] = {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots']}
    add_by_kind(test, "fruit", "watermelon")
    assert test == {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots'], 'fruit': ['watermelon']}


def test_add_by_kind_edge_case() -> None:
    """Tests if the function will add a new plant type if the new plant is empty."""
    test: dict[str, list[str]] = {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots']}
    add_by_kind(test, "fruit", "",)
    assert test == {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots'], 'fruit': ['']}


def test_add_by_date_use_case() -> None:
    """Tests if the function will add a new plant type to the already existing list for April."""
    test: dict[str, list[str]] = {'April': ['marigold'], 'June': ['carrots']}
    add_by_date(test, "April", "sunflower")
    assert test == {'April': ['marigold', 'sunflower'], 'June': ['carrots']}


def test_add_by_date_edge_case() -> None:
    """Tests if the function will add an empty new plant type to an already existing list for June."""
    test: dict[str, list[str]] = {'April': ['marigold'], 'June': ['carrots']}
    add_by_date(test, "June", "")
    assert test == {'April': ['marigold'], 'June': ['carrots', '']}


def test_lookup_by_kind_and_date_use_case() -> None:
    """Tests if the function will print out the right response for an input already in type and month."""
    test1: dict[str, list[str]] = {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots']}
    test2: dict[str, list[str]] = {'April': ['marigold'], 'June': ['carrots']}
    assert lookup_by_kind_and_date(test1, test2, "vegetable", "June") == "vegetables to plant in June: ['carrots']"


def test_lookup_by_kind_and_date_edge_case() -> None:
    """Tests if the function will still work with empty inputs for plant type and month."""
    test1: dict[str, list[str]] = {'flower': ['marigold', 'zinnia'], 'vegetable': ['carrots']}
    test2: dict[str, list[str]] = {'April': ['marigold'], 'June': ['carrots']}
    assert lookup_by_kind_and_date(test1, test2, "", "") == "No s to plant in "