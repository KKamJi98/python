from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20x20 => 10x10
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self) -> None:
        random_x: int = random.randint(-280, 280)
        random_y: int = random.randint(-280, 280)
        self.goto(random_x, random_y)