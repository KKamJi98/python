from modules.art import logo
from modules.read_file import read_file
from modules.user import get_user_input
import pandas as pd
import random
from pandas import DataFrame
import os
import platform

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
print(logo)

df: DataFrame = read_file(relative_path="./data/data.csv")

score = 0
keep_going = True
while keep_going:
    if len(df) == 0:
        print("You Win!! All Clear")
        break

    if score == 0:
        select_elements: DataFrame = df.sample(n=2)
        # df.drop(df[df["name"] == select_elements.iloc[1]["name"]].index, inplace=True)
        name_left: str = select_elements.iloc[1]["name"]
        followers_left: int = int(select_elements.iloc[1]["followers"])
    else:
        select_elements: DataFrame = df.sample(n=1)

    name_right: str = select_elements.iloc[0]["name"]
    followers_right: int = int(select_elements.iloc[0]["followers"])
    # df.drop(df[df["name"] == select_elements.iloc[0]["name"]].index, inplace=True)
    df.drop(df[df["name"].isin([name_left, name_right])].index, inplace=True)

    user_select = get_user_input(name_left, name_right)

    if user_select == "left" and followers_left > followers_right:
        print("Correct!")
        score += 1
    elif user_select == "right" and followers_left < followers_right:
        print("Correct!")
        score += 1
    elif followers_left == followers_right:
        print("Draw!")
    else:
        print("Incorrect!")
        keep_going = False
        print("Game Over")
        score -= 1
    
    print(f"Left: {name_left} with {followers_left} followers")
    print(f"Right: {name_right} with {followers_right} followers")
    
    if keep_going:
        print(f"Current score: {score}")
        continue_game = (
            input("Do you want to continue? Type 'yes' to continue or 'no' to stop:")
            .strip()
            .lower()
        )
        if continue_game == "no":
            keep_going = False
            print("Game End")
        else:
            clear()


print(f"Your Score: {score}")
