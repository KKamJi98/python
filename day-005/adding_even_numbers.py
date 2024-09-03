target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_sum = 0
for ele in range(2, target + 1, 2):
    even_sum += ele

print(even_sum)
