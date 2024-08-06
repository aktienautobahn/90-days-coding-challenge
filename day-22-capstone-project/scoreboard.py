from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 270)
        self.write(f"Level {self.level}", font=FONT)
    
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", font=FONT) 

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)