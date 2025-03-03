from data.coffee_information import menu
from modules.command import turn_off, resource_report, order_coffee


def process_input(user_input: str) -> None:
    """사용자 입력을 처리하는 함수"""
    if user_input in menu:
        inserted_coin = insert_coin()
        if inserted_coin >= menu[user_input]["cost"]:
            change = inserted_coin - menu[user_input]["cost"]
            print(f"Here is ${change:.2f} in change.")
            order_coffee(user_input)
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_input == "off":
        turn_off()
    elif user_input == "report":
        resource_report()
    else:
        print("Invalid input")


def insert_coin() -> float:
    """코인을 삽입하는 함수"""
    print("Please insert coins.")
    try:
        quarters: int = int(input("How many quarters?(0.25$): "))
        dimes: int = int(input("How many dimes?(0.10$): "))
        nickles: int = int(input("How many nickles?(0.05$): "))
        pennies: int = int(input("How many pennies?(0.01$): "))
    except ValueError:
        print("Invalid input, please enter a number.")
        return 0.0  # 에러 시 0.0 반환

    total: float = (
        (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    )

    # 총 금액을 유저에게 출력
    print(f"Total inserted: ${total:.2f}")

    return total
