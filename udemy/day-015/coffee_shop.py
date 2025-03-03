from modules.art import logo
from data.coffee_information import menu
from modules.order import process_input

print(logo)

menus = menu.keys()

print(f"{'Menu':<12}{'Price':>10}")  # 메뉴와 가격 헤더 출력 (폭 지정)
print("-" * 22)  # 구분선 출력

keep_going = True
while keep_going:
    for coffee_name, coffee_info in menu.items():
        print(f"{coffee_name.capitalize():<12} ${coffee_info['cost']:<8.2f}")  # 폭 지정

    # 사용자 입력 받기
    user_menu: str = (
        input(f"What would you like? ({'/'.join(menu.keys())}) : ").strip().lower()
    )
    if user_menu == "off":
        keep_going = False

    # 사용자 입력 처리
    process_input(user_menu)
