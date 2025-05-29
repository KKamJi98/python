"""
Generator Example - Demonstrating Python generators

This example shows how to create and use a simple generator function in Python.
The generator yields lines from a dialogue between Simpsons characters.
"""


def doh2():
    """
    A generator function that yields three lines of dialogue.
    
    Yields:
        str: Lines of dialogue from Simpsons characters
    """
    yield "Homer: D'oh!"
    yield "Lisa: A deer!"
    yield "Marge: A female deer!"


if __name__ == "__main__":
    # Iterate through the generator and print each yielded value
    for line in doh2():
        print(line)
        
    # Alternative way to use the generator
    print("\nAlternative way to use the generator:")
    g = doh2()
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("Generator exhausted")
