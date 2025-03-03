# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    area = height * width
    num_cans = ceil(area / cover)
    print(f"You'll need {num_cans} cans of paint.")
    return num_cans


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
