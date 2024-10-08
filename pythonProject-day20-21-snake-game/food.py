
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        x_cor=random.randint(-280, 280)
        y_cor=random.randint(-280, 280)
        self.goto(x_cor,y_cor)

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
