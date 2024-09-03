# encrypt 함수 생성
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
    print(cipher_text)


encrypt(text, shift)
