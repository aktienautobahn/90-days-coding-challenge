from turtle import Turtle
MOVING_DISTANCE = 40
UP = 90
DOWN = 270
RIGHT_X = 380
LEFT_X = -380

class Paddle:
    def __init__(self, side):
        self.segments = []
        if side == "right":
            self.create_puddle(RIGHT_X)
        elif side == "left":
            self.create_puddle(LEFT_X)
        #self.head = self.segments[0]
        #self.head.setheading(UP)
        #self.tail = self.segments[-1]
        #self.tail.setheading(DOWN)    
    
    
    def create_puddle(self, x):
        
        y=20
        for n_segment in range(3):
            n_segment = Turtle(shape="square")
            n_segment.color("white")
            n_segment.penup()
            n_segment.goto(x=x, y=y)        
            y -= 20
            self.segments.append(n_segment)
    
    def paddle_move_up(self):
        #following other segments
        
        for segment in self.segments:
            segment.setheading(UP)
            segment.forward(40)
        
        
    def paddle_move_down(self):
                #following other segments
        for segment in self.segments:
            segment.setheading(DOWN)
            segment.forward(40)