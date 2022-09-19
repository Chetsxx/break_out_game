from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.02

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move

        self.goto(newx, newy)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed *= 0.9

    def reset_speed(self):
        self.move_speed = 0.02
        self.goto(0, -270)
        self.x_move *= -1

