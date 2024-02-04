"""EX02 - One Shot Battleship."""
__author__ = "730461078"

# Part 1: Establishing a Secret and Prompting for a Guess
grid_size = 4
secret_row = 3
secret_column = 2

# Prompt the user to guess a row and column
while True:
    guess_row = int(input("Guess a row: "))
    if guess_row < 1 or guess_row > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        continue
    else:
        break

while True:
    guess_column = int(input("Guess a column: "))
    if guess_column < 1 or guess_column > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        continue
    else:
        break

# Box colors
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Check the user's guess and construct the visual representation of the grid
row_count = 1
while row_count <= grid_size:
    column_count = 1
    row_string = ""
    while column_count <= grid_size:
        if guess_row == row_count:
            if guess_column == column_count:

                # Construct the result box (red or white) based on guess
                if guess_row == secret_row and guess_column == secret_column:
                    row_string += RED_BOX  # Red box = hit
                else:
                    row_string += WHITE_BOX  # White box = miss
            else:
                row_string += BLUE_BOX  # Blue box for all other guess options
        else:
            row_string += BLUE_BOX  # Blue box for other guess options
        column_count += 1
    print(row_string)
    row_count += 1

# Output of result
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")