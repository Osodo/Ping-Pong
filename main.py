from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("PingPong by Osodo")
screen.bgcolor("black")
screen.tracer(0)
right_paddle = Paddle()

screen.listen()
screen.onkeypress(key="Up", fun = right_paddle.go_up)
screen.onkeypress(key="Down", fun = right_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()