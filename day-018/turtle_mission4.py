# 무작위 행보 (degree 90)
# 선 두께 늘리기
# 터틀 움직이는 속도 더 빠르게

import random
import turtle as t

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.pensize(15)
my_turtle.speed(5)

def change_color() -> None:
    R: int = random.randint(0, 255)
    G: int = random.randint(0, 255)
    B: int = random.randint(0, 255)
    my_turtle.color(R, G, B)
    

direction = [0, 90, 180, 270]

while True:
    change_color()
    my_turtle.forward(50)
    # my_turtle.right(random.choice(direction))
    my_turtle.setheading(random.choice(direction))

# screen = t.Screen()
# screen.exitonclick()