from typing import Union


def add(n1, n2) -> Union[int, float]:
    return n1 + n2


def min(n1, n2) -> Union[int, float]:
    return n1 - n2


def calculator(n1, n2, func) -> Union[int, float]:
    return func(n1, n2)


result: int | float = calculator(4, 2, min)
print(result)
