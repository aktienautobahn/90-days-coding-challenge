from turtle import Turtle, color

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
GAME_OVER_FONT = ('Courier', 40, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 00
        self.color('white')
        self.penup()
        self.goto(-340,-260)
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score}', font=FONT, align=ALIGNMENT)       
        
    def update_score(self, score):
        self.score += score
        self.refresh()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"You won! Your score is {self.score}", align=ALIGNMENT, font=GAME_OVER_FONT)


 