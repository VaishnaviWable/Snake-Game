from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.sc=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.sc}   Highscore:{self.high_score}",font=("Verdana",15, "normal"),align="center")
        
    def increase_score(self):
        self.sc+=1
        self.update_score()
    
    def reset(self):
        if self.sc>self.high_score:
            self.high_score=self.sc
        self.sc=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     # self.penup()
    #     # self.hideturtle()
    #     # self.color("white")
    #     self.write("GAME OVER !!",font=("Verdana",16, "normal"),align="center")
    
    

    
       
            