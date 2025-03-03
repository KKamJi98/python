import random


def is_correct(input_display):
    for letter in input_display:
        if letter == "_":
            return False
    return True


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

display = ["_" for _ in range(len(chosen_word))]

while not is_correct(display):
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    print(display)

print("You Win!")
