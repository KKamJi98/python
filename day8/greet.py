# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


greet()


def greet_with_name(name):  # name => Parameter
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("KKamJi")  # "KKamJi" => Argument


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(location="Korea", name="Tae-hyung")
