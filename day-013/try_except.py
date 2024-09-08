try:
    age = int(input("How old are you?"))
except ValueError:
    print(
        "You have typed in a an invalid number. Please try again with a valid number."
    )
    age = int(input("How old are you?"))

if age > 18:
    print("You can drive!!!!")
else:
    print("You can't drive...")
