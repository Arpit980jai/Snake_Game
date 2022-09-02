import Food
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"),)
        self.hideturtle()



    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 30, "normal"), )
    def increase_score(self):
        self.score+=1
        print(self.score)
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"), )

