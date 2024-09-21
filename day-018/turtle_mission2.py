import turtle as t

my_turtle = t.Turtle()
my_turtle.shape("classic")

def draw_dotted_line_ver1() -> None:
    for _ in range(15):
        my_turtle.color("black")
        my_turtle.forward(10)
        my_turtle.color("white")
        my_turtle.forward(10)
    my_turtle.color("black")

def draw_dotted_line_ver2() -> None:
    for _ in range(15):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()

draw_dotted_line_ver2()

screen = t.Screen()
screen.exitonclick()