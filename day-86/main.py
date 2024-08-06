#--------------------------- IMPORT LIBRARIES & MODULES ----------------------------#
from turtle import Screen
import time
import random
import gc #garbage collector

# import classes
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
from bricks import Bricks


#--------------------------- CONSTANTS ----------------------------#
COLORS = ['red', 'blue', 'green', 'orange']


#---------------------------- SETTING UP SCREEN ----------------------------#
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Breakout Game")    
screen.tracer(0)



#---------------------------- GENERATING OBJECTS ----------------------------#

#generate Paddle
paddle = Paddle()
#generate Ball
ball = Ball()

#generating bricks
bricks_list = []
start_pos_y = 280
for y in range(5):
    start_pos_x = - 390
    color = random.choice(COLORS)
    for _ in range(13):
        bricks_list.append(Bricks(x=start_pos_x, y=start_pos_y, color=color))
        start_pos_x += 60
    start_pos_y -= 20
#generate scoreboard
score_board = ScoreBoard()

#---------------------------- DEFINING KEYS ----------------------------#
screen.listen()
screen.onkey(paddle.paddle_move_left, "Left")
screen.onkey(paddle.paddle_move_right, "Right")

#---------------------------- SCREEN RENDER LOOP ----------------------------#
game_is_on = True

while game_is_on:
    
    screen.update()  
    time.sleep(0.02)
    
    ball.move()
    
    #bounce on puddle colision
    ball.bounce_paddle(paddle)
    
    #check collision with bricks
    for bricks in bricks_list:
        if ball.collision_check(bricks):
            for segment in bricks.segments:
                segment.reset()
                segment.clear()
                segment = 0
                gc.collect()
            bricks_list.remove(bricks)
            score_board.update_score(score=1)
            
    # check if any bricks left
    if len(bricks_list) == 0:
        score_board.game_over()
        game_is_on = False

    #check and update score
    if ball.ycor() < -300:
        score_board.update_score(score=-1)
        ball.hideturtle()
        ball = Ball()
    
 


screen.exitonclick()