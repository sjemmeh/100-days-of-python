import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# Setup player and cars
player = Player()
cars = CarManager()
score = Scoreboard()

# Player movement
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    cars.car_logic()
    time.sleep(0.1)
    screen.update()
    for car in cars.spawned_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        score.increase_score()
        cars.increase_speed(score.level)
        player.spawn()

screen.exitonclick()


