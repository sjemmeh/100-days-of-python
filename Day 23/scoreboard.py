from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.goto(-210, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.level}', align=ALIGN, font=FONT)
    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGN, font=FONT)
