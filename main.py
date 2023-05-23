import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creates the player, scoreboard, and cars
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Screen listing and keys
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
default_speed = 0.1

while game_is_on:

    time.sleep(scoreboard.player_speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            scoreboard.game_over()
            game_is_on = False
    # detect if player goes to the next level
    if player.ycor() > 300:
        player.player_reset()
        scoreboard.player_score()

screen.exitonclick()
