from turtle import Screen, Turtle
import turtle

from pyrsistent import s
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

#setting up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")    
screen.tracer(0)
#drawing dashed line
pen = Turtle()
pen.color("white")
pen.width(5)
pen.penup()
pen.goto(0,280)
pen.setheading(270)
end = False
while end == False:
    if pen.ycor() > -280:

        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(20)
    else:
        end = True
        pen.hideturtle()

#defining objects
score_left = ScoreBoard('left')
score_right = ScoreBoard('right')
paddle_left = Paddle('left')
paddle_right = Paddle('right')
ball = Ball()
#defining keys

screen.listen()
screen.onkey(paddle_right.paddle_move_up, "Up")
screen.onkey(paddle_right.paddle_move_down, "Down")
screen.onkey(paddle_left.paddle_move_up, "w")
screen.onkey(paddle_left.paddle_move_down, "s")

#main logic
game_is_on = True

while game_is_on:

    screen.update()  
    time.sleep(0.05)
    ball.move()
    #bounce on right / left puddle colision
    ball.bounce_paddle(paddle_left)
    ball.bounce_paddle(paddle_right)
    #check and update score
    
    if ball.xcor() < -400:
        score_right.update_score()
        ball.hideturtle()
        ball = Ball()
    elif ball.xcor() > 400:
        score_left.update_score()
        ball.hideturtle()
        ball = Ball()
    
 


screen.exitonclick()