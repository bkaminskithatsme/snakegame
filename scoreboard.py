from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(align="center", arg=f"Score: {self.score}")

    def losing_state(self):
        self.write(align="center", arg=f"Score: {self.score} GAME OVER!")
