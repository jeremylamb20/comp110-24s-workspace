"""Mutating functions."""

__author__ = "730461078"


def manual_append(lst: list[int], num: int) -> None:
    """Appends the integer num to the end of the input list lst.
    
    Parameters:
    lst (list[int]): Input list
    num (int): Integer to be appended

    Returns:
    None
    """
    lst.append(num)


def double(lst: list[int]) -> None:
    """Multiplies every element within input list by 2 using a while loop.
    
    Parameters:
    lst (list[int]): Input list

    Returns:
    None
    """
    i = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1
