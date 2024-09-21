from turtle import Turtle, Screen
import time

def animate_square():
    # 거북이 객체 생성
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("medium blue")

    # 정사각형 그리기
    for _ in range(8):
        timmy_the_turtle.forward(100)
        time.sleep(0.5)
        timmy_the_turtle.right(90)
        
def three_animate_square():
    tim = Turtle()
    tom = Turtle()
    tam = Turtle()
    
    tim.color("red")
    tom.color("green")
    tam.color("blue")

    tim.forward(150)
    tom.forward(200)
    tam.forward(250)        
        
# 스크린 객체 생성 및 창 크기 설정
screen = Screen()
screen.setup(width=680, height=680)

animate_square()
three_animate_square()
# 창 클릭 시 종료
screen.exitonclick()
