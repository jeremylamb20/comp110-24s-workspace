"""EX01 - Simple Battleship!!"""
	 
__author__ = "730461078"

#Prompting for Player 1 Input
while True:
    player1_input = int(input("Pick a secret boat location between 1 and 4: "))
    if player1_input < 1:
        print("Error! {} too low!".format(player1_input))
    elif player1_input > 4:
        print("Error! {} too high!".format(player1_input))
    else:
        break

#Prompting for Player 2 Input
while True:
    player2_input = int(input("Pick a secret boat location between 1 and 4: "))
    if player2_input < 1:
        print("Error! {} too low!".format(player2_input))
    elif player2_input > 4:
        print("Error! {} too high!".format(player2_input))
    else:
        break

#Copied named constants from assignment page
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#Checking Player 1's guess
player1_guess = int(input("Guess a number between 1 and 4: "))
if player1_guess == player2_input:
    print("Correct! You hit the ship")
else:
    print("Incorrect! You missed the ship.")

#Checking Player 1's guess and building the emoji string
result = RED_BOX if player1_guess == player2_input else WHITE_BOX
emoji_string2 = ""
for Y in range(1, 5):
    if Y == player1_guess:
        emoji_string2 += result
    else:
        emoji_string2 += BLUE_BOX

print(emoji_string2)

#Checking Player 2's guess
player2_guess = int(input("Guess a number between 1 and 4: "))
if player2_guess == player1_input:
    print("Correct! You hit the ship")
else:
    print("Incorrect! You missed the ship.")

#Checking Player 2's guess and building the emoji string
result = RED_BOX if player2_guess == player1_input else WHITE_BOX
emoji_string1 = ""
for X in range(1, 5):
    if X == player2_guess:
        emoji_string1 += result
    else:
        emoji_string1 += BLUE_BOX

print(emoji_string1)