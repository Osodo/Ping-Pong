from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if self.ycor()  > 290 or self.ycor() < -290:
            new_y = self.ycor() - 20
            self.goto(new_x, new_y) 

    def bounce(self):
        self.y_move *= -1


