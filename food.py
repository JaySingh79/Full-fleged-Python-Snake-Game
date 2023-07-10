from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.speed(0)
        self.turtlesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-330,330)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
