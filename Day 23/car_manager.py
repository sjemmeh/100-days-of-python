from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager():
    def __init__(self):
        self.spawned_cars = []
        self.current_tick = 0
        self.ticks_required = random.randint(1, 20)
        self.car_speed = STARTING_MOVE_DISTANCE
    def car_logic(self):
        for car in self.spawned_cars:
            if car.xcor() <= -320: # When out of bounds
                self.remove_car(car)
        self.create_car()
        self.move_cars()


    def create_car(self):
        """Creates a car in a random tick between 1 and 20"""
        if self.current_tick == self.ticks_required:
            self.current_tick = 0
            new_car = Turtle(shape='square')
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-200, 200))
            self.spawned_cars.append(new_car)
            print(f'New car created: {new_car}')
        else:
            self.current_tick += 1

    def remove_car(self, id):
        """Removes a car from spawned cars to avoid memory flood"""
        self.spawned_cars.remove(id)
    def increase_speed(self, level):
        self.car_speed += STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT)
    def move_cars(self):
        for car in self.spawned_cars:
            car.forward(self.car_speed)
