from turtle import Turtle, Screen
from pydub.playback import play
from pygame import mixer
import time
from snake_move import Snake
from playagain import playagain
from food import Food
from scoreboard import Score
# from Day20_Playagain import playagain


def snakegame():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        sk.move()
        mixer.init()

        mixer.music.set_volume(0.3)
        # eat food
        if sk.head.distance(fd) < 15:

            mixer.music.load("food.mp3")
            mixer.music.play()
            fd.refresh()
            sk.extend()
            s.increase_score()

        # collision with wall
        if sk.head.xcor() > 285 or sk.head.xcor() < -285 or sk.head.ycor() > 285 or sk.head.ycor() < -285:
            mixer.music.set_volume(0.03)
            mixer.music.load("gameover3.mp3")
            mixer.music.play()
            # game_on = False
            # s.game_over()
            s.reset()
            sk.reset()
            

        # collsion with tail
        for segments in sk.snake:
            if segments == sk.head:
                pass
            elif sk.head.distance(segments) < 10:
                # game_on = False
                # s.game_over()
                mixer.music.set_volume(0.03)
                mixer.music.load("gameover3.mp3")
                mixer.music.play()
                s.reset()
                sk.reset()


screen = Screen()
while True:
    screen.clear()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.tracer(0)
    sk = Snake()
    # food for snake
    fd = Food()
    s = Score()

    screen.listen()
    screen.onkey(sk.move_up, "Up")
    screen.onkey(sk.move_down, "Down")
    screen.onkey(sk.move_left, "Left")
    screen.onkey(sk.move_right, "Right")

    pg = playagain()
    snakegame()
    pg.display()
    if pg.choice != "yes":
        break
