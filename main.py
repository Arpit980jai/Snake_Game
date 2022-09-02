import turtle
from turtle import Screen
from snake import Snake
from Food import Food
import time
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#detect the collision


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extendSegments()
        scoreboard.increase_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scoreboard.game_over()
        game_is_on=False

    for segment in snake.segments:
        if snake.head==segment:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()