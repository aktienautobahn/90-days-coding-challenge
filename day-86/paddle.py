from turtle import Turtle

MOVING_DISTANCE = 50
RIGHT = 0
LEFT = 180
START_POSITION_X = 50
START_POSITION_Y = -280

class Paddle:
    def __init__(self):
        self.segments = []
        self.create_puddle(x=START_POSITION_X, y=START_POSITION_Y)
    
    
    def create_puddle(self, x, y):
        for n_segment in range(7): # range(7) -> 7 segments of paddle
            n_segment = Turtle(shape="square")
            n_segment.color("white")
            n_segment.penup()
            n_segment.goto(x=x, y=y)        
            x -= 20
            self.segments.append(n_segment)
    
    def paddle_move_left(self):
        #following other segments
        for segment in self.segments:
            segment.setheading(LEFT)
            segment.forward(MOVING_DISTANCE)
        
    def paddle_move_right(self):
        #following other segments
        for segment in self.segments:
            segment.setheading(RIGHT)
            segment.forward(MOVING_DISTANCE)