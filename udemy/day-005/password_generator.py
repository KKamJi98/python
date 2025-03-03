# Password Generator Project
import random

letters = [
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
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# choice함수를 사용하면 가독성이 더 좋아짐
easy_password = ""
for i in range(0, nr_letters):
    easy_password += letters[random.randint(0, len(letters) - 1)]
for i in range(0, nr_symbols):
    easy_password += symbols[random.randint(0, len(symbols) - 1)]
for i in range(0, nr_numbers):
    easy_password += numbers[random.randint(0, len(numbers) - 1)]

print(f"easy password: {easy_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random.shuffle() 함수를 사용하면 더 쉬울 듯
hard_password = []
password_length = nr_letters + nr_symbols + nr_numbers
letter_count = 0
number_count = 0
symbol_count = 0
while len(hard_password) != password_length:
    random_num = random.randint(1, 3)
    # letter(1), symbol(2), number(3)
    if random_num == 1 and letter_count == nr_letters:
        continue
    elif random_num == 2 and symbol_count == nr_symbols:
        continue
    elif random_num == 3 and number_count == nr_numbers:
        continue

    if random_num == 1:
        hard_password.append(letters[random.randint(0, len(letters) - 1)])
    if random_num == 2:
        hard_password.append(symbols[random.randint(0, len(symbols) - 1)])
    if random_num == 3:
        hard_password.append(numbers[random.randint(0, len(numbers) - 1)])

print(f"hard password: {''.join(hard_password)}")
