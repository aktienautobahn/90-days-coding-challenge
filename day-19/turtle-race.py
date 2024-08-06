#import stuff
from turtle import Turtle, Screen
from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')

#create object and initialize variables
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color from\n{', '.join(colors)}: ").lower()
turtles = []
y_pos = 100
#create turtle objects and put in the starter positions
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=y_pos)
    y_pos -= 50

#race loop
race_continue = True
while race_continue:
    for i in turtles:
        i.forward(randint(1,10))
        if i.position()[0] > 230:
            race_continue = False
            winner = i.color()[0]
            break

#print results and define if the user is winner
print(f"The winner is: {winner}")
if user_bet == winner:
    print("You won!")
else:
    print("You lost, better luck next time!")

#click for finishing
screen.exitonclick()