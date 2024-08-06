from turtle import Screen, Turtle
from random import choice

tim = Turtle()
screen = Screen()
screen.colormode(255)

direction = [0,90,180,270]
tim.speed(0)

def random_color():
    return (choice(range(256)),choice(range(256)), choice(range(256)))

def random_walk():
    tim.forward(30)
    tim.setheading(choice(direction))
    tim.pencolor(random_color())
    tim.pensize(choice(range(5,10)))

for x in range(200):
    random_walk()

screen.exitonclick()