from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, 'normal')
HIGHSCORE = "highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        self.goto(0, 250)
        self.update_scoreboard()
    def read_highscore(self):
        with open(HIGHSCORE, "r") as file:
            content = file.read()
        self.high_score = int(content)
    def write_highscore(self, score):
        with open(HIGHSCORE, 'w') as file:
            file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.read_highscore()
        self.write(f'Score: {self.score}, High Score: {self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def restart(self):
        if self.score > self.high_score:
            self.write_highscore(self.score)
        self.score = 0
        self.update_scoreboard()
