from turtle import Screen
import turtle
from score_board import ScoreBoard
from snake_class import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#declaring objects
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#main logic
game_is_on = True

while game_is_on:
    screen.update()  
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        snake.add_segment()
        score_board.add_score()
        food.refresh()
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over() 
    #detect collistion with it's tail
    #if head collides with any segments of the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15: 

            #trigger game over
            game_is_on = False
            score_board.game_over()


screen.exitonclick()