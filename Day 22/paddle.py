from turtle import Turtle
SHAPE = "square"
COLOR = "WHITE"

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(x_position, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def go_up(self):
        if self.ycor() != 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
    def go_down(self):
        if self.ycor() != -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)