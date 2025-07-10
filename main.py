from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("PingPong by Osodo")
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun = r_paddle.go_up)
screen.onkeypress(key="Down", fun = r_paddle.go_down)

screen.onkeypress(key="w", fun = l_paddle.go_up)
screen.onkeypress(key="s", fun = l_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if -280 < ball.ycor() > 280:
        ball.bounce()


screen.exitonclick()