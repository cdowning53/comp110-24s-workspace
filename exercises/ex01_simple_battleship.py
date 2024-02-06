"""EX01 - Simple Battleship - A cute step toward battleship."""

__author__ = "730482646"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

pick_a_number: int = int(input("Pick a secret boat location between 1 and 4: "))
if pick_a_number > 4: 
    print("Error! " + str(pick_a_number) + " too high!")
    exit()
if pick_a_number < 1:
    print("Error! " + str(pick_a_number) + " too low!")
    exit()

guess_a_number = int(input("Guess a number between 1 and 4: "))
if guess_a_number > 4:
    print("Error! " + str(guess_a_number) + " too high!")
    exit()
if guess_a_number < 1:
    print("Error! " + str(guess_a_number) + " too low!")
    exit()

battleship: str = ""
guess_emoji: str = ""
if guess_a_number == pick_a_number:
    guess_emoji = RED_BOX
else:
    guess_emoji = WHITE_BOX
if guess_a_number == 1:
    battleship = guess_emoji + BLUE_BOX + BLUE_BOX + BLUE_BOX

if guess_a_number == 2:
    battleship = BLUE_BOX + guess_emoji + BLUE_BOX + BLUE_BOX

if guess_a_number == 3:
    battleship = BLUE_BOX + BLUE_BOX + guess_emoji + BLUE_BOX

if guess_a_number == 4:
    battleship = BLUE_BOX + BLUE_BOX + BLUE_BOX + guess_emoji
print(battleship)
if guess_a_number == pick_a_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")