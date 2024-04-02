"""EX03 - Functional Battleship."""
__author__ = "730461078"

# Part 1 - input_guess function
def input_guess(grid_size, row_or_col):
    """
    Prompts the user for a row or column guess.

    Args:
    grid_size (int): The size of the grid.
    row_or_col (str): A string specifying 'row' or 'column'.

    Returns:
    int: The user's row or column guess.
    """
    assert row_or_col == "row" or row_or_col == "column", "The second parameter must be 'row' or 'column'"

    guess = int(input(f"Guess a {row_or_col} (1-{grid_size}): "))
    while guess < 1 or guess > grid_size:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess

# Part 2 - print_grid function
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

def print_grid(grid_size, row_guess, col_guess, is_correct):
    """
    Prints a grid of colored boxes to represent the game board based on the user's guesses and correctness.

    Arguments:
    grid_size (int): The size of the grid.
    row_guess (int): The user's row guess.
    col_guess (int): The user's column guess.
    is_correct (bool): Indicates if the user's guess was correct.

    Returns:
    None
    """
    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            if i == row_guess and j == col_guess:
                if is_correct:
                    print(RED_BOX, end=" ")  # correct guess
                else:
                    print(WHITE_BOX, end=" ")  # incorrect guess
            else:
                print(BLUE_BOX, end=" ")  # empty cell
        print()  # Move to the next line for the next row
