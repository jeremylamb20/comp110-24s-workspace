"""Dictionary Test."""

__author__ = "730461078"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_word() -> None:
    """Test the basic function of invert by reversing the orders of 2 sets of words."""
    original_dict: dict[str, str] = {"bean": "lima", "pepper": "red"}
    inverted_dict: dict[str, str] = invert(original_dict)
    assert inverted_dict == {'lima': 'bean', 'red': 'pepper'}


def test_invert_num_letter() -> None:
    """Test the basic function of invert using numbers and words."""
    original_dict: dict[str, str] = {'5': 'vanilla', '3': 'coffee', '8': 'chocolate'}
    inverted_dict: dict[str, str] = invert(original_dict)
    assert inverted_dict == {'vanilla': '5', 'coffee': '3', 'chocolate': '8'}


def test_invert_key_error() -> None:
    """Test to make sure KeyError is raised in response to duplicates."""
    with pytest.raises(KeyError):
        repeat_dict = {'vanilla': '4', 'coffee': '4'}
        invert(repeat_dict)


def test_favorite_color_peers() -> None:
    """Test basic function of favorite_color using friends' favorites."""
    friends: dict[str, str] = {'Jon': 'blue', 'Greg': 'red', 'Duy': 'green', 'Chris': 'blue'}
    assert favorite_color(friends) == 'blue'


def test_favorite_color_coworkers() -> None:
    """Test basic function of favorite_color using coworkers' favorites."""
    coworkers: dict[str, str] = {'James': 'red', 'Vlad': 'orange', 'Angie': 'orange', 'Greg': 'blue'}
    assert favorite_color(coworkers) == 'orange'


def test_favorite_color_tie() -> None:
    """Edge test for favorite_color for tie functionality."""
    tie: dict[str, str] = {'Vlad': 'green', 'George': 'red', 'Khalil': 'red', 'Hiram': 'green'}
    assert favorite_color(tie) == 'green'


def test_count_colors() -> None:
    """Test basic use of count by finding amount each color shows up in favorite colors."""
    colors_from_friends_coworkers_and_tie: list[str] = ['blue', 'red', 'yellow', 'blue', 'red', 'brown', 'brown', 'blue', 'yellow', 'red', 'red', 'yellow']
    assert count(colors_from_friends_coworkers_and_tie) == {'blue': 3, 'red': 4, 'yellow': 3, 'brown': 2}


def test_count_excrescence() -> None:
    """Test basic use of count by finding amount each letter in the word excrescence."""
    excrescence_by_letter: list[str] = ['e', 'x', 'v', 'r', 'e', 's', 'v', 'e', 'n', 'v']
    assert count(excrescence_by_letter) == {'e': 3, 'x': 1, 'v': 3, 'r': 1, 's': 1, 'n': 1}


def test_count_single_letter() -> None:
    """Test edge use of count by finding amount single letter."""
    single_letter: list[str] = {'a'}
    assert count(single_letter) == {'a': 1}


def test_alphabetizer_grocery() -> None:
    """Test basic use of aphabetizer using grocery list."""
    groceries: list[str] = ['bread', 'chips', 'snacks', 'bacon', 'sausage', 'chicken', 'bananas', 'soda', 'butter', 'cookies']
    assert alphabetizer(groceries) == {'b': ['bread', 'bacon', 'bananas', 'butter'], 'c': ['chips', 'chicken', 'cookies'], 's': ['snacks', 'sausage', 'soda']}


def test_alphabetizer_animals() -> None:
    """Test basic use of aphabetizer using animals."""
    animals: list[str] = ['deer', 'alligator', 'eagle', 'armadillo', 'ant', 'dolphin', 'elephant', 'dog', 'duck']
    assert alphabetizer(animals) == {'d': ['deer', 'dolphin', 'dog', 'duck'], 'a': ['alligator', 'armadillo', 'ant'], 'e': ['eagle', 'elephant']}


def test_alphabetizer_characters() -> None:
    """Test edge use of aphabetizer with special characters."""
    special_characters: list[str] = ['!dog', '~dog', 'dog', '~duck', '!duck', 'duck', 'deer', '!deer', '~deer', '!dolphin']
    assert alphabetizer(special_characters) == {'!': ['!dog', '!duck', '!deer'], '$': ['~dog', '~duck', '~deer'], 'd': ['dog', 'duck', 'deer']}

def test_update_attendance() -> None:
    original_attendance: dict = {}
    new_attendance: dict[str, list[str]] = new_attendance()
    assert new_attendance == {'Monday': ['...nna', 'Anna']} == {'Monday': '...ay': ['Anna']}

def test_update_attendance_add_to_existing() -> None:
    """Test basic use of update_attendance by adding names of friends who were present for each night."""
    movie_week: dict = {'Monday': ['Jon', 'Laura', 'Greg', 'Ben'], 'Wednesday': ['Leo', 'Laura']}
    attendance_log: dict[str, list[str]] = update_attendance(movie_week, 'Wednesday', 'Zoe')
    assert attendance_log == {'Monday': ['Jon', 'Laura', 'Greg', 'Ben'], 'Wednesday': ['Leo', 'Laura', 'Zoe']}


def test_update_attendance_add_day() -> None:
    """Test basic use of update_attendance by adding new day and attendee to log."""
    movie_week_updated: dict = {'Monday': ['Jon', 'Laura', 'Greg', 'Ben'], 'Wednesday': ['Leo', 'Laura', 'Zoe']}
    attendance_log_2: dict[str, list[str]] = update_attendance(movie_week_updated, 'Friday', 'Greg')
    assert attendance_log_2 == {'Monday': ['Jon', 'Laura', 'Greg', 'Ben'], 'Wednesday': ['Leo', 'Laura', 'Zoe'], 'Friday': ['Greg']}


def test_update_attendance_empty_num_multiple() -> None:
    """Test edge use for empty initial list, student number instead of names, and adding multiple student numbers in single line of code."""
    empty_log: dict = {}
    add_day_and_student_no: dict[str, list[str]] = update_attendance(empty_log, 'Monday', ['323', '737', '180', '999'])
    assert add_day_and_student_no == {'Monday': [['323', '737', '180', '999']]}