from turtle import Turtle
RIGHT = "right"
LEFT = "left"
ALIGNMENT = 'center'
FONT = ('Courier', 60, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self, side) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 00
        self.color('white')
        self.penup()
        
        if side == RIGHT:
            self.goto(70,240)
            self.refresh()
        elif side == LEFT:
            self.goto(-70,240)
            self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f'{self.score}', font=FONT, align=ALIGNMENT)       
        
    def update_score(self):
        self.score += 1
        self.refresh()
 