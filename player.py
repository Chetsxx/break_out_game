from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color("white")
        self.penup()
        self.goto(0, -300)


    def move_left(self):
        self.backward(10)

    def move_right(self):
        self.forward(10)

