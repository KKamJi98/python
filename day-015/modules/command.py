from data.coffee_information import menu, resources
from modules.make_coffee import can_make, make_coffee


def resource_report() -> None:
    """
    현재 커피 머신의 자원 상태를 출력하는 함수.
    물, 우유, 커피, 그리고 수익을 각각 출력합니다.
    """
    print(f"Water:\t{resources['water']}ml")
    print(f"Milk:\t{resources['milk']}ml")
    print(f"coffee:\t{resources['coffee']}g")
    print(f"Money:\t${resources['money']}")


def turn_off() -> None:
    """
    커피 머신을 종료하는 함수.
    """
    print("Turning off")


def order_coffee(coffee_type: str) -> None:
    """
    사용자가 선택한 커피를 주문하는 함수.
    먼저 커피를 만들 수 있는지(can_make) 확인하고, 가능하면 커피를 만듭니다(make_coffee).
    """
    if can_make(coffee_type):
        make_coffee(coffee_type)
    print(f"Here is your {coffee_type} 😊😊. Enjoy!")
