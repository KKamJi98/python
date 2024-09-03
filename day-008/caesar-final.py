from modules.art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_amount, direction):
    result_text = ""

    for letter in text:
        if not letter.isalpha():
            result_text += letter
            continue
        letter_index = alphabet.index(letter)
        if direction == "encode":
            shifted_letter_index = letter_index + shift_amount
            if shifted_letter_index >= len(alphabet):
                shifted_letter_index = shifted_letter_index - len(alphabet)
        elif direction == "decode":
            shifted_letter_index = letter_index - shift_amount
            if shifted_letter_index < 0:
                shifted_letter_index = len(alphabet) + shifted_letter_index
        else:
            print("Wrong Input")
            return
        result_text += alphabet[shifted_letter_index]

    print(f"The {direction}d text is => {result_text}")


print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet) - 1:
        shift = shift % len(alphabet)

    caesar(text, shift, direction)

    again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if again != "yes":
        print("Good Bye!")
        break
