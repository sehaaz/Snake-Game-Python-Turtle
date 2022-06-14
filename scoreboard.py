from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 285)
        self.write(f"Score = {self.score}", False, "center", font=("Verdana", 7, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(f"Score = {self.score}", False, "center", font=("Verdana", 7, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", False, "center", font=("Verdana", 15, "normal"))