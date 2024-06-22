from turtle import Turtle, Screen
from tkinter import messagebox
import random

# Define objects
is_race_on = False
screen = Screen()

# Setup screen
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

setting_bet = True
while setting_bet:
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:").lower()
    if user_bet in colors:
        setting_bet = False

# Setup turtles
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for turtle_index in range(0,len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                messagebox.showinfo("You win!", "You win! The winning turtle was " + str(winner) + "!")
            else:
                messagebox.showinfo("You Lose!", "You Lose! The winning turtle was " + str(winner) + "!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

