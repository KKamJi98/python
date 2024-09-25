from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.print_score()
        self.hideturtle()
        
    def print_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))
        # self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 5, "bold"))

    def increase_score(self) -> None:
        self.score += 1
        self.print_score()