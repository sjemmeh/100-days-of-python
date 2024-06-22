import random
import turtle as t



timmy = t.Turtle()
timmy.shape("circle")
timmy.shapesize(1)
t.colormode(255)
timmy.pensize(1)
timmy.speed("fastest")

screen = t.Screen()
screen.title("TIMMY THE BIG BOI")
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_figure(sides):
#     for _ in range(sides):
#         timmy.color(random.choice(colors))
#         timmy.forward(100)
#         timmy.right((360/sides))
#
#
# for shape in range(3,6):
#     draw_figure(shape)
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def create_spirograph(gapsize):
    for _ in range(int(360 / gapsize)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(gapsize)

create_spirograph(5)

screen.exitonclick()
