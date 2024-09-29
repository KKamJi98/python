import pandas
import os

PATH = os.path.join(os.path.dirname(__file__), "nato_phonetic_alphabet.csv")

data = pandas.read_csv(PATH)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
