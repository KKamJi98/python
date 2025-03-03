from turtle import Turtle
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "data.txt")
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open(FILE_PATH, mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self) -> None:
        self.clear()
        self.write(
            f"Score: {self.score} \tHigh Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )
        # self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 5, "bold"))

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open(FILE_PATH, mode="w") as file:
            file.write(str(self.high_score))

    def increase_score(self) -> None:
        self.score += 1
        self.update_score()
