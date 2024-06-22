from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0
        self.draw_middle()
        self.goto(0, 180)
        self.update_scoreboard()
    def draw_middle(self):
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f'{self.p2_score}', align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(f'{self.p1_score}', align=ALIGN, font=FONT)
        self.draw_middle()

    def increase_score(self, player):
        if player == 1:
            self.p1_score += 1
        else:
            self.p2_score += 1
        self.clear()
        self.update_scoreboard()

    def p2_score(self):
        self.p2_score += 1
        self.clear()
        self.update_scoreboard()