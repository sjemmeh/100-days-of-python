
from turtle import Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND = "black"
SCREEN_TITLE = "Snek"

screen = Screen()
class Display():
    def __init__(self):
        self.setupScreen()

    def setupScreen(self):
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor(SCREEN_BACKGROUND)
        screen.title(SCREEN_TITLE)
        screen.tracer(0)

    def update(self):
        screen.update()
    def closeBehaviour(self):
        screen.exitonclick()