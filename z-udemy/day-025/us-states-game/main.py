import turtle
import os
import pandas

PATH = os.path.dirname(__file__)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{PATH}/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv(f"{PATH}/50_states.csv")

num_of_state = len(data)
num_of_correct = 0

states_dict = data.set_index("state")[["x", "y"]].to_dict(orient="index")
print(states_dict)

while num_of_correct != num_of_state:
    answer_state = screen.textinput(
        title=f"{num_of_correct}/{num_of_state} States Correct",
        prompt="What's another state's name?",
    )
    if answer_state == None:
        continue
    elif answer_state == "Exit":
        break
    else:
        answer_state = answer_state.title()
    if answer_state in states_dict:
        num_of_correct += 1
        temp_turtle = turtle.Turtle()
        temp_turtle.penup()
        temp_turtle.hideturtle()
        temp_turtle.goto(states_dict[answer_state]["x"], states_dict[answer_state]["y"])
        temp_turtle.write(answer_state.title())
        del states_dict[answer_state]

missed_data = states_dict.keys()
print(missed_data)
series_data = pandas.Series(list((states_dict.keys())))
series_data.to_csv(PATH + "/state_to_learn.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) # 클릭 이벤트 리스너
# turtle.mainloop() # 자동으로 스크린이 꺼지지 않도록

# screen.exitonclick()
