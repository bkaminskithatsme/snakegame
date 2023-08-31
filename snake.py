from turtle import Turtle, Screen
import time
MOVE_DISTANCE = 20


class Snake:

    snake = []

    def __init__(self):
        for seg in range(3):
            new_segment = Turtle()
            new_segment.pu()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(x=0 - 20 * seg, y=0)
            self.snake.append(new_segment)
            print(self.snake)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
