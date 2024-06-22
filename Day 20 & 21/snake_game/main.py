from turtle import Screen
from snake import Snake
from display import Display
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
display = Display()

snake = Snake()
food = Food()
score = Scoreboard()

# Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Setup
game_is_on = True
while game_is_on:
    display.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.move()
        score.increase_score()
        snake.extend()
    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.restart()
        snake.restart()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.restart()
            snake.restart()


display.closeBehaviour()
