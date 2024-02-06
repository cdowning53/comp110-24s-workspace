"""EX02 - One Shot Battleship - Battleship adding more details."""

__author__ = 730482646

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_a_row: int = int(input("Guess a row: "))
while guess_a_row < 1 or guess_a_row > 4:
    guess_a_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_a_column: int = int(input("Guess a column: "))
while guess_a_column < 1 or guess_a_column > 4:
    guess_a_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

row: int = 1
result: str = ""

while row <= grid_size:
    column: int = 1
    while column <= grid_size:
        if guess_a_column == column and guess_a_row == row:
            if guess_a_column == secret_column and guess_a_row == secret_row:
                result += RED_BOX
            else:
                result += WHITE_BOX
        else:
            result += BLUE_BOX
        column += 1
    result += "\n"
    row += 1
print(result)
    
if guess_a_row == secret_row and guess_a_column == secret_column:
    print("Hit!")

elif guess_a_row != secret_row and guess_a_column != secret_column:
    print("Miss!")

elif guess_a_row == secret_row and guess_a_column != secret_column:
    print("Close! Correct row, wrong column.")

elif guess_a_row != secret_row and guess_a_column == secret_column:
    print("Close! Correct column, wrong row.")