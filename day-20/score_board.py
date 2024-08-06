from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 00
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.refresh()
        
        
    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score}', font=FONT, align=ALIGNMENT)
    
    def add_score(self):
        self.score += 1
        self.refresh()#
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)