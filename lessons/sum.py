"""Summing the elements of a list using different loops."""

__author__ = "730461078"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of all elements in the input list using a while loop.
    
    Args:
    vals (list[float]): A list of floats to sum up.
    
    Returns:
    float: The sum of all elements in the input list.
    """
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of all elements in the input list using a for loop.
    
    Args:
    vals (list[float]): A list of floats to sum up.
    
    Returns:
    float: The sum of all elements in the input list.
    """
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of all elements in the input list using a for loop with range().
    
    Args:
    vals (list[float]): A list of floats to sum up.
    
    Returns:
    float: The sum of all elements in the input list.
    """
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total