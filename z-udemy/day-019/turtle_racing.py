from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles: list[Turtle] = []
y_positions: list[int] = [-70, -40, -10, 20, 50, 80]


for i in range(6):
    temp_turtle = Turtle()
    temp_turtle.color(colors[i])
    temp_turtle.shape("turtle")
    temp_turtle.penup()
    temp_turtle.goto(x=-230, y=y_positions[i])
    # temp_turtle.pendown()
    turtles.append(temp_turtle)

user_bet: str | None = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 170:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
