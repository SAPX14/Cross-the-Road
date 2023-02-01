import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

t = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(t.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    # Detecting collision
    for car in car_manager.all_cars:
        if car.distance(t) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting if turtle reached the other side
    if t.is_at_finish_line():
        t.goto_start()
        car_manager.level_up()
        scoreboard.level_increment()

screen.exitonclick()