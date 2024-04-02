"""EX 04 - List Utility Functions."""
__author__ = "730461078"


def all(num: list[int], interger: int) -> bool:
    """Finding out if all the integers in a list are the same as the target number."""
    if not num:  
        return False
    num_idx: int = 0  
    while num_idx <= (len(num) - 1): 
        if num[num_idx] != interger:   
            return False
        num_idx += 1  
    return True  


def max(input: list[int]) -> int:
    """Determining the highest number within a number list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    num_idx: int = 0 
    high_input: int = input[0]
    while num_idx < (len(input)):
        if input[num_idx] > high_input:
            high_input = input[num_idx]
        num_idx += 1
    return high_input


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checking if the lists are a match."""
    if len(list1) != len(list2): 
        return False
    idx: int = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]: 
            return False
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Extending the function."""
    list1 += list2