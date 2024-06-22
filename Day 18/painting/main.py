###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as tr
###############################################
################ IMPORTED CODE ################
###############################################
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_colors.append(color.rgb)

###########################################
################ VARIABLES ################
###########################################

t = tr.Turtle() # Initiate boi
t.shape('circle') # Make it a BBC (Big beautiful circle)
tr.colormode(255) # RGB
t.speed(-20) # FAST AF BOI (STILL SLOW AF)



screen = tr.Screen() # Initiate screen
screen.title("T THE BIG BOI") # Let 'em know
screen.bgcolor("#FFFDD0") # Creamy
screen.setworldcoordinates(1, 1, screen.window_width() - 1, screen.window_height() - 1) # Just works (tm)

###########################################
################ FUNCTIONS ################
###########################################
def random_color():
    """Generate random rgb from given image"""
    number=random.randint(0,len(rgb_colors)-1)
    r = rgb_colors[number][0]
    g = rgb_colors[number][1]
    b = rgb_colors[number][2]
    return (r,g,b)
def draw_dots(width,height,size):
    """Draw dots in given dimensions"""
    t.penup()  # We no need no lines
    t.hideturtle()
    current_height = 0
    for _ in range(int((height) / size)):
        t.goto(0, current_height)
        for _ in range(int((width) / size) + 1):
            t.dot(int(size / 2), random.choice(rgb_colors))
            t.forward(size)
        if _ is not int((height) / size):
            current_height += size




draw_dots(screen.window_width(), screen.window_height(), 35) #Pump that screen full


tr.done()
