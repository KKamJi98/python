# easy: 10회
# hard: 5회
# medium: 8회
from modules.art import logo
from modules.clear import clear

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

difficulty_levels = {"easy": 10, "medium": 8, "hard": 5}

while True:
    difficulty = input(
        "Choose a difficulty. Type 'easy' or 'medium' or 'hard': "
    ).lower()
    if difficulty in difficulty_levels:
        lives = difficulty_levels[difficulty]
        break
    else:
        print("Invalid input. Please type 'easy' or 'medium' or 'hard'.")


import random

correct_number = random.randint(1, 100)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))

    if guess_number == correct_number:
        print(f"You got it! The answer was {correct_number}")
        break
    else:
        lives -= 1
        if guess_number < correct_number:
            print("Too Low")
        else:
            print("Too High")

    if lives == 0:
        print(
            f"You've run out of guesses, you lose. The correct number was {correct_number}."
        )
