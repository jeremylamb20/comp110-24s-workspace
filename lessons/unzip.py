"""Splitting a dictionary into two lists."""

__author__ = "730461078"


def get_keys(input_dictionary: dict[str, int]) -> list[str]:
    """Return a list of all the keys in the input dictionary.
    
    Args:
    input_dict (dict[str, int]): A dictionary with string keys and integer values.
    
    Returns:
    list[str]: A list containing all the keys from the input dictionary.
    """
    return list(input_dictionary.keys())


def get_values(input_dictionary: dict[str, int]) -> list[int]:
    """Return a list of all the values in the input dictionary.
    
    Args:
    input_dict (dict[str, int]): A dictionary with string keys and integer values.
    
    Returns:
    list[int]: A list containing all the values from the input dictionary.
    """
    return list(input_dictionary.values())