from random import randint
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=8.5, stretch_wid=8.5)
        self.color("blue")
        self.speed("fastest")
        random_x = randint(-200,200)
        random_y = randint(-200,200)
        self.goto(random_x, random_y)
