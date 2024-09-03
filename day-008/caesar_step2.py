# decrypt 함수 생성
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for ele in plain_text:
        ele_index = alphabet.index(ele)
        cipher_index = ele_index + shift_amount
        if cipher_index >= len(alphabet):
            cipher_index = cipher_index - len(alphabet)
        cipher_text += alphabet[cipher_index]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for ele in cipher_text:
        ele_index = alphabet.index(ele)
        plain_index = ele_index - shift_amount
        if plain_index < 0:
            plain_index = len(alphabet) + plain_index
        plain_text += alphabet[plain_index]
    print(f"The encoded text is {plain_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong input")
