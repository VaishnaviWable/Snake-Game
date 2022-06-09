from logging import setLogRecordFactory
from turtle import Turtle

class playagain(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.choice=""

    def display(self):
        self.penup()
        # self.goto(0,-100)
        # self.color("white")
        self.choice=self.screen.textinput(title="Play or Stop",prompt="Would you like to play again?")
        # print(self.choice)
       

            
        
