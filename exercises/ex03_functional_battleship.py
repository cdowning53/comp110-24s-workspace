"""Functional Battleship."""

__author__ = "730482646"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid: int, specification: str) -> int:
    """Player guesses the location of the row and column."""
    assert specification == "row" or specification == "column"
    if specification == "row":
        guess_a_row: int = int(input("Guess a row: "))
        while guess_a_row < 1 or guess_a_row > grid:
            guess_a_row = int(input(f"The grid is only {grid} by {grid}. Try again: "))
        return guess_a_row
    else:
        guess_a_column: int = int(input("Guess a column: "))
        while guess_a_column < 1 or guess_a_column > grid:
            guess_a_column = int(input(f"The grid is only {grid} by {grid}. Try again: "))
        return guess_a_column


def print_grid(grid: int, guess_a_row: int, guess_a_column: int, answer: bool) -> None:
    """Battleship grid is printed using emoji codes."""
    result: str = ""
    if answer:
        result = RED_BOX
    else:
        result = WHITE_BOX
    row_count: int = 1
    while row_count <= grid:
        row_answer: str = ""
        column_count: int = 1
        if guess_a_row == row_count:
            while column_count <= grid:
                if guess_a_column == column_count:
                    row_answer += result
                else:
                    row_answer += BLUE_BOX
                column_count += 1
        else:
            while column_count <= grid:
                row_answer += BLUE_BOX
                column_count += 1
        print(row_answer)
        row_count += 1


def correct_guess(correct_row: int, correct_column: int, guess_a_row: int, guess_a_column: int) -> bool:
    """If the player's guess is correct or not."""
    if guess_a_row == correct_row and guess_a_column == correct_column:
        return True
    else:
        return False


def main(grid: int, correct_row: int, correct_column: int) -> None:
    """Main functions, gives player 5 guesses."""
    turn: int = 1
    win: bool = False
    while turn <= 5 and not win:
        print(f"=== Turn {turn}/5 ===")
        guess_a_row: int = input_guess(grid, "row")
        guess_a_column: int = input_guess(grid, "column")
        correct: bool = correct_guess(correct_row, correct_column, guess_a_row, guess_a_column)
        print_grid(grid, guess_a_row, guess_a_column, correct)
        if correct:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            win = True
        else:
            print("Miss!")
            turn += 1
    if turn > 5 and not win:
        print("X/5 - Better luck next time!")
        # exit()


if __name__ == "__main__":
    grid: int = random.randint(3, 5)
    main(grid, random.randint(1, grid), random.randint(1, grid))