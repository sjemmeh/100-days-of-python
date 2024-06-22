from display import Display
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
display = Display()

player1 = Paddle(350)
player2 = Paddle(-350)
score = Scoreboard()
ball = Ball()

screen.listen()



# Player 1
screen.onkeypress(player1.go_up, "Up")
screen.onkeypress(player1.go_down, "Down")

#Player 2
screen.onkeypress(player2.go_up, "w")
screen.onkeypress(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    display.update()
    ball.move()

    # Detect bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collisions
    if (ball.distance(player1) < 50 and ball.xcor() > 325) or (ball.distance(player2) < 50 and ball.xcor() < -325):
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() < -380:
        score.increase_score(1)
        ball.reset_position()
    elif ball.xcor() > 380:
        score.increase_score(2)
        ball.reset_position()



display.closeBehaviour()
