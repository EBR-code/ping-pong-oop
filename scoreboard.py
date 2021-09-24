from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"AWTS GEGE", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

