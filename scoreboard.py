from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        with open ("/Users/B42/Desktop/highscore.txt") as file1:
            self.highscore = int(file1.read())
        self.color("white")
        self.hideturtle()
        self.goto(-80, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highscore}", move=False, font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        with open ("/Users/B42/Desktop/highscore.txt", mode = "w") as file1:
            file1.write(f"{self.highscore}")

    def increase_score(self):
        self.score += 1
        self.update_score()



