from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=750,height=650)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)


screen.listen()
my_snake = Snake("white")
snake_food = Food()
snake_score = Scoreboard()


screen.onkey(key="Up",fun=my_snake.go_up)
screen.onkey(key="Down",fun=my_snake.go_down)
screen.onkey(key="Left",fun=my_snake.go_left)
screen.onkey(key="Right",fun=my_snake.go_right)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.09)
    my_snake.move()

    if my_snake.tim_instances[0].distance(snake_food)<18:
        print("yummy!")
        snake_score.score += 1
        snake_food.refresh()
        my_snake.extend()
        snake_score.write_this()

    if my_snake.tim_instances[0].xcor()>360 or my_snake.tim_instances[0].xcor()< -360 or my_snake.tim_instances[0].ycor()>285 or my_snake.tim_instances[0].ycor()< -285:
        # is_game_on = False
        # snake_score.gameover()
        my_snake.reset()
        snake_score.new_score() 

    for segment in my_snake.tim_instances[1:]:

        if my_snake.tim_instances[0].distance(segment)<8:
            is_game_on = False
            snake_score.game_over()


screen.exitonclick()

