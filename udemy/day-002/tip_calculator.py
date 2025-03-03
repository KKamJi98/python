# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_amount = total_bill + (total_bill * (tip_percentage / 100))
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print(f"Each person shuld pay: ${round(total_amount / number_of_people, 2)}")

total_amount = "{:.2f}".format(total_amount / number_of_people)
print(f"Each person shuld pay: ${total_amount}")
