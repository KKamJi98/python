# Step 2

import random


def is_correct(input_display):
    for letter in input_display:
        if letter == "_":
            return False
    return True


stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = ["_" for _ in range(word_length)]

while True:
    guess = input("Guess a letter: ").lower()
    letter_in_word = False
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
            letter_in_word = True
    if letter_in_word == False:
        lives -= 1
    print(" ".join(display))
    print(f"lives: {lives}")
    print(stages[lives])

    if is_correct(display):
        print("You Win!")
        break
    elif lives == 0:
        print("You Lose...")
        break
