from turtle import Turtle
from random import choice
UPPER_WALL = 300
RIGHT_WALL = 380
LEFT_WALL = -380

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("white")

        #starting position
        self.goto(0, 180) 
        self.showturtle()
        #initial movement direction is random
        self.invert_x = choice([-7,-8,-9,-10,7,8,9,10])
        self.invert_y = choice([-8])
        print("ball initialized")

    def move(self):
        """
        move method
        """
        self.bounce_wall()
        new_x = self.xcor() + self.invert_x
        new_y = self.ycor() + self.invert_y
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        """
        checks collision with walls on screen
        """
        if self.xcor() > RIGHT_WALL or self.xcor() < LEFT_WALL:
            self.invert_x *= -1
        elif self.ycor() > UPPER_WALL:
            self.invert_y *= -1

    
    def bounce_paddle(self, paddle):
        """
        checks collision with paddle objects on screen
        """
        for paddle_segment in paddle.segments:
            if self.distance(paddle_segment) < 35 and self.xcor() < 380 and self.xcor() > -380:
                self.invert_y *= -1 


    def collision_check(self, bricks):
        """
        checks collision with bricks objects on screen
        """
        for brick in bricks.segments:
            if self.distance(brick) < 30:
                self.invert_y *= -1 
                return True