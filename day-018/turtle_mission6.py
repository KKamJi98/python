import colorgram
import turtle as t
import random

colors = colorgram.extract("./image.jpg", 30)

colors_rgb_list = []

for color in colors:
    rgb = color.rgb
    colors_rgb_list.append((rgb[0], rgb[1], rgb[2]))
# print(colors_rgb_list)
"""
[(248, 247, 240), (239, 250, 245), (251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20), 
(215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), (234, 165, 197), (121, 187, 159), (203, 31, 130), 
(12, 186, 212), (10, 46, 25), (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]
"""
t.colormode(255)
my_turtle = t.Turtle()
my_turtle.penup()  # 터틀 동선 안 남도록
my_turtle.hideturtle()  # 터틀 안보이게 (화살표)
my_turtle.speed("fastest")
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(colors_rgb_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()
