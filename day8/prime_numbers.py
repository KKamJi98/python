# Write your code below this line 👇
def prime_checker(number):
    prime_numbers = [True for _ in range(number+1)]
    prime_numbers[1] = False
    prime_numbers[0] = False
    for current in range(2, len(prime_numbers)):
        if prime_numbers[current] == False:
            continue
        for idx in range(2, number+1):
            if current*idx > number:
                break
            else:
                prime_numbers[current * idx] = False
                
    if prime_numbers[number] == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)