import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
#car = CarManager()

#create car pool
car_pool = []
for _ in range(15):
    car_pool.append(CarManager())
print(car_pool)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_pool:
        car.move()
        car.reset_position()
        #detect collision with a car
        for segment in car.segments:
            if player.distance(segment) < 20:
                game_is_on = False
                score.game_over()

    
    if player.finish():
        score.update_score()
        player.reset_position()
        for car in car_pool:
            car.speed_update()
    
    #game_is_on = False
screen.exitonclick()