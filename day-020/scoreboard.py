from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        # self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 5, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.update_score()
