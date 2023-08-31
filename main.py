from turtle import Turtle, Screen
from snake import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)


game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)








screen.exitonclick()