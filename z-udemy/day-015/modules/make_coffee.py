from data.coffee_information import menu, resources


def can_make(coffee_type: str) -> bool:
    """
    남은 resources를 사용해 커피를 만들 수 있는지 확인
    """
    # 메뉴 이름에 해당하는 음료의 ingredients만 가져옴
    customer_menu_ingredients = menu[coffee_type]["ingredients"]

    for ingredient in customer_menu_ingredients:
        # resources에 해당 재료가 부족한지 확인
        if customer_menu_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def make_coffee(coffee_type: str) -> None:
    """
    resources를 사용해 커피를 만들기
    """
    resources["money"] += menu[coffee_type]["cost"]

    customer_menu_ingredients = menu[coffee_type]["ingredients"]

    for ingredient in customer_menu_ingredients:
        resources[ingredient] -= customer_menu_ingredients[ingredient]
