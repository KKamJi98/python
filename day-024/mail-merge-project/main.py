# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

NAME_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "Input/Names/invited_names.txt"
)
LETTER_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "Input/Letters/starting_letter.txt"
)
OUTPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), "Output/ReadyToSend/")


with open(LETTER_FILE_PATH, "r") as file:
    letter = file.read()

with open(NAME_FILE_PATH, "r") as file:
    names = file.readlines()

    for name in names:
        name = name.strip()
        temp_letter = letter.replace("[name]", name)

        with open(f"{OUTPUT_FILE_PATH}letter_for_{name}.docx", "w") as file:
            file.write(temp_letter)
