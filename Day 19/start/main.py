from turtle import Turtle, Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

jos = Turtle()
screen = Screen()


def move_forward():
    """Moves Jos forward 10 pixels"""
    jos.forward(10)


def move_backward():
    """Moves Jos backward 10 pixels"""
    jos.backward(10)


def move_left():
    """Moves Jos left 15 degrees"""
    jos.left(15)


def move_right():
    """Moves Jos right 15 degrees"""
    jos.right(15)


def reset():
    """Resets the screen"""
    screen.resetscreen()


screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.listen()

screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
