from turtle import Turtle
from random import choice, randint

from validators import card_number

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.segments = []
        self.create_car()
        
    def create_car(self):
        x=STARTING_POSITION-randint(1,60)*10
        y=randint(-25,25)*10
        color = choice(COLORS)

        for _ in range(2):
            self.segments.append(Turtle(shape="square"))
            self.segments[_].color(color)
            self.segments[_].penup()
            self.segments[_].setheading(180)
            self.segments[_].goto(x=x,y=y)
            x += 20

    def move(self):
        for segment in self.segments:
            segment.forward(self.move_distance)
            
    def reset_position(self):
        x=STARTING_POSITION
        y=randint(-13,13)*10
        if self.segments[0].xcor() < -300:
            for segment in self.segments:
                segment.goto(x = x, y = y )
                x += 20
        
    def speed_update(self):
        self.move_distance += MOVE_INCREMENT
#how oft one car starts
