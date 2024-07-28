from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake= Snake()
food= Food()
score= ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detecting collision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect collison with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()> 280 or snake.head.ycor ()<-280:
        score.reset_score()
        snake.reset()


    #detest collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance (segment)< 10:
            score.reset_score()
            snake.reset()





screen.exitonclick()