from turtle import Turtle

coordinates = [(0, 0), (-20, 0), (-40, 0)]
U=90
D=270
L=180
R=0

class Snake(Turtle):

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    

    def create_snake(self):
        # append 3 squares
        for positions in coordinates:
            self.add_segment(positions)
           
            
    def add_segment(self,positions):
        tur = Turtle("square")
        tur.color("white")
        tur.penup()
        self.snake.append(tur)
        tur.goto(positions)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        # game_on=True
        # # find x and y coordinates of 3 segments and move them to segmentposition-1 position
        # # i.e 3 segment on 2 position and so on
        for seg_num in range(len(self.snake)-1, 0, -1):
            x_cor = self.snake[seg_num-1].xcor()
            y_cor = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x_cor, y_cor)
        self.head.forward(20)

   
    def move_left(self):
        if self.head.heading()!= R:
            self.head.setheading(L)

    def move_right(self):
        if self.head.heading() != L:
            self.head.setheading(R)
    
    def move_up(self):
        if self.head.heading()!= D:
            self.head.setheading(U)

    def move_down(self):
        if self.head.heading()!=U:
            self.head.setheading(D)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]