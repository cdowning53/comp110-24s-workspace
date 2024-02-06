"""Number Guessing Game"""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        #something to help us exit
        correct = True
    if guess > SECRET:
        print("Too high. Guess again")
    if guess < SECRET:
        print ("Too low! Guess again")