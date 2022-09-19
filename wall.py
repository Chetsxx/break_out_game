from turtle import Turtle

class Wall:
    def __init__(self):
        self.bricks = []
        self.x = -310

    def create_wall(self):
        for w in range(12):
            wall = Turtle()
            wall.penup()
            wall.color("white")
            wall.shape('square')
            wall.shapesize(stretch_wid=1, stretch_len=2.5)
            wall.goto(self.x, 230)
            self.x += 55
            self.bricks.append(wall)

        self.x = -310

        for w in range(12):
            wall = Turtle()
            wall.penup()
            wall.color("white")
            wall.shape('square')
            wall.shapesize(stretch_wid=1, stretch_len=2.5)
            wall.goto(self.x, 200)
            self.x += 55
            self.bricks.append(wall)

        self.x = -310

        for w in range(12):
            wall = Turtle()
            wall.penup()
            wall.color("white")
            wall.shape('square')
            wall.shapesize(stretch_wid=1, stretch_len=2.5)
            wall.goto(self.x, 170)
            self.x += 55
            self.bricks.append(wall)