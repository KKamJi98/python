from turtle import Turtle, Screen


def move_forward() -> None:
    my_turtle.forward(50)


def move_back() -> None:
    my_turtle.back(50)


def rotate_clockwise() -> None:
    current_heading = my_turtle.heading()
    new_heading = current_heading - 10
    my_turtle.setheading(new_heading)


def rotate_counterclockwise() -> None:
    current_heading = my_turtle.heading()
    new_heading = current_heading + 10
    my_turtle.setheading(new_heading)


def clear() -> None:
    my_turtle.home()
    my_turtle.clear()


my_turtle = Turtle()

screen = Screen()

screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeypress(key="a", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
