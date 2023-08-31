# Snakegame Copycat by Ben Kaminski
# Uses Turtle Py Lib


from snake import *
from food import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)


game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.15)
    #food touch
    if snake.snake[0].distance(food) < 15:
        print("yum")
        score.score += 1
        score.clear()
        score.update_score()
        snake.grow()
        snake.grow()
        snake.grow()
        food.new_food()

    #wall touch
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        score.clear()
        score.losing_state()
        game_on = False

    #body touch
    for seg in snake.snake[1:]:
        if snake.snake[0].distance(seg) < 10:
            game_on = False
            score.clear()
            score.losing_state()









screen.exitonclick()