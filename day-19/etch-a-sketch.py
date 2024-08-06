
#TODO import all nessessary and build objects
#TODO write key functions

#import stuff
from re import X
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def forwards():
    pen.forward(20)

def backwards():
    pen.backward(20)
      
def counter_clockwise():
    pen.left(10)
    pen.forward(20)
    
def clockwise():
    pen.right(10)
    pen.forward(20)

def clear_drawing():
    pen.clear()
    pen.penup()
    pen.home()
    pen.down()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "c")
screen.listen()

screen.exitonclick()