# 정삼각형 ~ 정십각형까지 그리기

import turtle as t
import random

# 색상 랜덤 변경
def change_color() -> None:
    R: int = random.randint(0, 255)
    G: int = random.randint(0, 255)
    B: int = random.randint(0, 255)
    my_turtle.color(R, G, B)
    
def draw_diagram(num) -> None:
    change_color()
    degree: float = 360 / num
    
    for _ in range(num):
        my_turtle.forward(100)
        my_turtle.right(degree)

t.colormode(255)
my_turtle = t.Turtle()
for i in range(3, 11):
    draw_diagram(i)

screen = t.Screen()
screen.exitonclick()