import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.speed("fastest")
my_turtle.pensize(3)
t.colormode(255)


def change_color() -> None:
    R: int = random.randint(0, 255)
    G: int = random.randint(0, 255)
    B: int = random.randint(0, 255)
    my_turtle.color(R, G, B)


for i in range(0, 360, 5):
    my_turtle.setheading(i)
    my_turtle.circle(100)
    change_color()


screen = t.Screen()
screen.setup(width=680, height=680)
screen.exitonclick()
