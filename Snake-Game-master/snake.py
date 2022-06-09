from turtle import Turtle,Screen
import time


screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)

snake=[]
coordinates=[(0,0),(-20,0),(-40,0)]
# append 3 squares
for positions in coordinates:
    tur=Turtle("square")
    tur.color("white")
    tur.penup()
    tur.goto(positions)
    snake.append(tur)


game_on=True
# find x and y coordinates of 3 segments and move them to segmentposition-1 position
# i.e 3 segment on 2 position and so on
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake)-1,0,-1):
        x_cor=snake[seg_num-1].xcor()
        y_cor=snake[seg_num-1].ycor()
        snake[seg_num].goto(x_cor,y_cor)
    snake[0].forward(20)

        

screen.exitonclick()