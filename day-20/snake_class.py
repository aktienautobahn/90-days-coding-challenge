#this is a snake class
from turtle import Turtle 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        x=0
        y=0
        for _ in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[_].color("white")
            self.segments[_].penup()
            self.segments[_].goto(x=x,y=y)
            x -= 20
    
    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        
    def move(self):
        for segment in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].setpos(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)
            
    
    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)
    
    def stop_game(self):
        self.game_is_on = False
        print(self.game_is_on)
        return self.game_is_on