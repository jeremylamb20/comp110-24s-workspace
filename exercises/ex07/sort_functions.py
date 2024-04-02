"""Functions that implement sorting algorithms."""

__author__ = "730461078"

def insertion_sort(x: list[int]) -> None:  
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)):  
        current: int = x[i]  
        j: int = i - 1  
        while j >= 0 and current < x[j]:
            x[j + 1] = x[j] 
            j -= 1  
        x[j + 1] = current 
    return None
def selection_sort(x: list[int]) -> None:  
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0 
    for idx in range(0,len(x)):  
        min: int = idx  
        for j in range(idx + 1, len(x)):
            if x[j] < x[min]:
                min = j
        if min != idx:
            x[idx], x[min] = x[min], x[idx]
        idx +=1
    return None