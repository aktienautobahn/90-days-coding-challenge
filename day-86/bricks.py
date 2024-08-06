from turtle import Turtle


class Bricks:
    def __init__(self, x, y, color):
        self.segments = []
        self.x = x
        self.y = y
        self.color = color
        self.create_bricks()

    def __del__(self):
        pass
        
    def create_bricks(self):
        for n_segment in range(3):
            n_segment = Turtle(shape="square")
            n_segment.color(self.color)
            n_segment.penup()
            n_segment.goto(x=self.x, y=self.y)        
            self.x += 20
            self.segments.append(n_segment)
    

        