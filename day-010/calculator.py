from modules.clear import clear
from modules.art import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    choice = "y"
    while choice == "y":
        for operation in operations:
            print(operation)
        operation = input("What is the operation?: ")
        num2 = float(input("What is the next number?: "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:"
        ).lower()
        if choice == "n":
            clear()
            calculator()
        num1 = result

    print("Calculator is off.")


calculator()
