import random

names = input("Give me everybody's names, separated by a comma. ").split(", ")
num_of_people = len(names)
target_name = names[random.randint(0, num_of_people - 1)]
print(f"{target_name} is going to buy the meal today!")
