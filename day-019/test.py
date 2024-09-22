from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

# 이동 상태를 나타내는 플래그 변수들
move_forward_flag = False
move_back_flag = False
rotate_clockwise_flag = False
rotate_counterclockwise_flag = False


# 거북이를 주기적으로 움직이는 함수
def move():
    if move_forward_flag:
        my_turtle.forward(5)
    if move_back_flag:
        my_turtle.backward(5)
    if rotate_clockwise_flag:
        my_turtle.right(5)
    if rotate_counterclockwise_flag:
        my_turtle.left(5)
    screen.ontimer(move, 100)  # 100밀리초마다 move 함수 호출


# 키 눌림 및 뗌 이벤트에 대한 처리 함수들
def start_move_forward():
    global move_forward_flag
    move_forward_flag = True


def stop_move_forward():
    global move_forward_flag
    move_forward_flag = False


def start_move_back():
    global move_back_flag
    move_back_flag = True


def stop_move_back():
    global move_back_flag
    move_back_flag = False


def start_rotate_clockwise():
    global rotate_clockwise_flag
    rotate_clockwise_flag = True


def stop_rotate_clockwise():
    global rotate_clockwise_flag
    rotate_clockwise_flag = False


def start_rotate_counterclockwise():
    global rotate_counterclockwise_flag
    rotate_counterclockwise_flag = True


def stop_rotate_counterclockwise():
    global rotate_counterclockwise_flag
    rotate_counterclockwise_flag = False


def clear():
    my_turtle.home()
    my_turtle.clear()


screen.listen()

# 키 눌림 이벤트 바인딩
screen.onkeypress(start_move_forward, "w")
screen.onkeyrelease(stop_move_forward, "w")
screen.onkeypress(start_move_back, "s")
screen.onkeyrelease(stop_move_back, "s")
screen.onkeypress(start_rotate_clockwise, "d")
screen.onkeyrelease(stop_rotate_clockwise, "d")
screen.onkeypress(start_rotate_counterclockwise, "a")
screen.onkeyrelease(stop_rotate_counterclockwise, "a")
screen.onkey(clear, "c")

move()  # 주기적인 움직임 시작

screen.exitonclick()
