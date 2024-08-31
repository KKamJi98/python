# Step 2

import random
import modules.hangman_art as hangman_art
import modules.hangman_words as hangman_words
from modules.hangman_modules import clear
from modules.hangman_modules import is_correct

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")
input("Press Enter")
display = ["_" for _ in range(word_length)]

while True:
    guess = input("Guess a letter: ").lower()
    clear()
    letter_in_word = False

    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
            letter_in_word = True

    if letter_in_word == False:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        print("Correct!")

    print(" ".join(display))
    # print(f"lives: {lives}")
    print(hangman_art.stages[lives])

    if is_correct(display):
        print("You Win!")
        break
    elif lives == 0:
        print("You Lose...")
        break
