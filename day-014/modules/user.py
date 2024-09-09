def get_user_input(name_left: str, name_right: str) -> str:
    while True:
        user_select = input(f"{name_left} vs {name_right} Who has more followers? \nType 'left' or 'right': ").strip().lower()
        if user_select in ["left", "right"]:
            return user_select
        else:
            print("Wrong Answer... Type 'left' or 'right'")
