from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x_cor=random.randint(-200,200)
        y_cor=random.randint(-200,200)
        self.goto(x_cor,y_cor)
        
