from turtle import Turtle
from random import randint, choice
UPPER_WALL = 280
LOWER_WALL = -280

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.invert_x = choice([-7,-8,-9,-10,7,8,9,10])
        self.invert_y = choice([-7,-8,-9,-10,7,8,9,10])
        print("ball initialized")

    def move(self):
        self.bounce_wall()
        new_x = self.xcor() + self.invert_x
        new_y = self.ycor() + self.invert_y
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
    #detect collision on wall
        if self.ycor() > UPPER_WALL or self.ycor() < LOWER_WALL:
            self.invert_y *= -1

    
    def bounce_paddle(self, paddle):
            #detect collision with a paddle
        for paddle_segment in paddle.segments:
            if self.distance(paddle_segment) < 20 and self.xcor() < 385 and self.xcor() > -390:
                self.invert_x *= -1 


        