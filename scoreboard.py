from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 290)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 15, "bold"))
        self.goto(300, 290)
        self.write(f"Lives: {self.life}", False, align="center", font=("Arial", 15, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!!\n Final Score: {self.score}", False, align="center", font=("Arial", 16, "normal"))



