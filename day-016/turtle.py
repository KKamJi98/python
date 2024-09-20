import turtle

# https://docs.python.org/ko/3/library/turtle.html
import modules.another_module

print(modules.another_module.another_variable)

timmy = turtle.Turtle()  # turtle 객체 생성
timmy.shape("turtle")
timmy.color("coral")


my_screen = turtle.Screen()  # screen 객체 생성
print(my_screen.canvheight)
for _ in range(100):
    timmy.forward(1)
my_screen.exitonclick()  # Exit 버튼을 클릭하기 전까지 종료 X
