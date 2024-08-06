from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)

def change_color():
    return (randint(0,255),randint(0,255),randint(0,255))

def circle_func(angle):
    tim.pencolor(change_color())
    tim.circle(100)
    tim.setheading(angle)

for x in range(0,361,5):
    circle_func(x)

screen.exitonclick()