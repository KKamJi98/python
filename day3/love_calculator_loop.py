print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
name = lower_name1 + lower_name2
true_score = 0
love_score = 0
for i in name:
  if i == 't' or i == 'r' or i == 'u' or i == 'e':
    true_score += 1
for i in name:
  if i == 'l' or i == 'o' or i == 'v' or i == 'e':
    love_score += 1

total_score = int((str(true_score) + str(love_score)))
if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {true_score}{love_score}.")