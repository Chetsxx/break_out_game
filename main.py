from turtle import Screen, Turtle
from player import Paddle
from wall import Wall
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(700, 650)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
paddle = Paddle()
wall = Wall()
wall.create_wall()
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

def hit():
    for brick in wall.bricks:
        if ball.distance(brick) < 20:
            brick.hideturtle()
            ball.y_bounce()
            brick.goto(0, 700)
            return True


game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.xcor() > 320 or ball.xcor() < -320:
        ball.x_bounce()

    if ball.ycor() > 300:
        ball.y_bounce()

    if ball.distance(paddle) < 100 and ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(paddle) > 100 and ball.ycor() < -280:
        ball.y_bounce()
        scoreboard.life -= 1
        scoreboard.update_scoreboard()

    if scoreboard.life == 0 or scoreboard.score == len(wall.bricks):
        game_on = False
        scoreboard.game_over()

    if hit():
        scoreboard.point()


screen.exitonclick()