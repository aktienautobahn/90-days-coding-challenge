from this import d
from turtle import Screen, Turtle
import random

tim = Turtle()

tim.shape('turtle')
tim_color = ["medium aquamarine", "DarkOrchid","IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def change_angle(corner):
    for _ in range(corner):
        tim.forward(50)
        tim.right(360/corner)


for number in range(4,11):
    tim.color(random.choice(tim_color))
    change_angle(number)
    


screen = Screen()
screen.exitonclick()