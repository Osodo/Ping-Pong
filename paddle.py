from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        self.paddle = Turtle( shape="square")
        self.paddle.penup()
        self.paddle.goto(x=350, y=0)
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5.0, stretch_len=1.0)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
