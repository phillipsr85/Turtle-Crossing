import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


FINISH_LINE_Y = 280
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -10
speed = STARTING_MOVE_DISTANCE


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
level = Scoreboard()
cars = CarManager()
car_list=[]

screen.listen()
screen.onkey(player.move,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(car_list) < 15:
        car_list= cars.create_car()

    cars.move(car_list,speed)


    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        level.update_level()
        speed += MOVE_INCREMENT

        ##car collision
    for car in car_list:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()