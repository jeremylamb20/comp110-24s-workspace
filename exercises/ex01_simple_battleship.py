"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730461078"

# Pt 1: Player 1 input
secret_boat_location = int(input("Pick a secret boat location between 1 and 4: "))
if secret_boat_location < 1:
    print(f"Error! {secret_boat_location} too low!")
    exit()
elif secret_boat_location > 4:
    print(f"Error! {secret_boat_location} too high!")
    exit()

# Pt 2: Player 2 input
guess_number = int(input("Guess a number between 1 and 4: "))
if guess_number < 1:
    print(f"Error! {guess_number} too low!")
    exit()
elif guess_number > 4:
    print(f"Error! {guess_number} too high!")
    exit()

# Part 3: Checking if user input matches
if guess_number == secret_boat_location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

result = RED_BOX if guess_number == secret_boat_location else WHITE_BOX
emoji_string = ""
for i in range(1, 5):
    if i == guess_number:
        emoji_string += result
    else:
        emoji_string += BLUE_BOX
print(emoji_string)