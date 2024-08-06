from turtle import Turtle, Screen
from random import randint

pen = Turtle()
screen = Screen()
screen.colormode(255)
pen.speed(0)

#function for random color pick
def change_color():
    return (randint(0,255),randint(0,255),randint(0,255))

#drawing function
def hirst_dot():
    pen.pencolor(change_color())
    pen.dot(20,change_color())
    pen.forward(40)

#change initiate postion to x-500
pen.penup()
pen.setposition((-400,0))   
pen.hideturtle()

#main loop
for x in range(5):
    for x in range(10):
        hirst_dot()
    pen.setheading(90)
    hirst_dot()
    pen.setheading(180)
    for x in range(10):
        hirst_dot()
    pen.setheading(90)
    hirst_dot()
    pen.setheading(0)

screen.exitonclick()