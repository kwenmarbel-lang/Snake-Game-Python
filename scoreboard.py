from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 359)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center" , font=("Arial",24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
        self.write(f"------------ Game Over ------------\n\nFinal Score: {self.score}\n\nHigh Score: {self.highscore}", align="center", font=("Arial",26, "normal"))