from turtle import Turtle, Screen

kkamji = Turtle()
screen = Screen()


def move_forwards():
    kkamji.forward(10)


screen.listen()
screen.onkey(
    key="space", fun=move_forwards
)  # space 이벤트 발생 시 move_forwards 함수 실행
screen.exitonclick()
