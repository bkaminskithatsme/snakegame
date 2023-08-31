from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("coral")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
