import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

choice = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_choice = int(input())
if user_choice >= 3 or user_choice < 0:
    print("Wrong input")
    exit()
print(choice[user_choice])

print("Computer chose:")
computer_choice = random.randint(0, 2)
print(choice[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
