"""EX03 - Functional Battleship."""

__author__ = "730461078"

import random

BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


# part 1 ~ input guess
def input_guess(grid_size: int, row_col: str) -> int:
    """Guessing row and column."""
    assert row_col == "row" or row_col == "column", "Must be 'row' or 'column'."
    while True:
        guess_input = input(f"Guess a {row_col}: ")
        valid_guess_input = False
        guess_number = 1
        while guess_number <= grid_size:
            if guess_input == str(guess_number):
                valid_guess_input = True
                break
            guess_number += 1

        if valid_guess_input:
            return int(guess_input)

        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")


# part 2 ~ print grid
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Determining grid size."""
    row = 1
    while row <= grid_size:
        row_str = ""
        column = 1
        while column <= grid_size:
            if row == row_guess and column == column_guess:
                row_str += RED_BOX if correct else WHITE_BOX
            else:
                row_str += BLUE_BOX
            column += 1
        print(row_str)
        row += 1


# part 3 ~ correct guess
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Inputting the correct guess."""
    return row_guess == secret_row and column_guess == secret_column


# part 4 ~ main function
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Starting the main game itself."""
    turn_num = 5
    turns_used = 0
    correct = False

    while turns_used < turn_num and not correct:
        print(f"=== Turn {turns_used + 1}/{turn_num} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, row_guess, column_guess)

        print_grid(grid_size, row_guess, column_guess, correct)

        if correct:
            print(f"Hit! You won in {turns_used + 1}/{turn_num} turns!")
        else:
            print("Miss!")
            turns_used += 1

    if not correct:
        print(f"X/{turn_num} - Better luck next time!")


if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))