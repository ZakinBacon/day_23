from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        self.player_speed = 0.1


    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 230)
        self.write(f"Level: {self.level}", align='center', font=('Courier', 24, 'normal'))

    def player_score(self):
        self.level += 1
        self.update_scoreboard()
        self.player_speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Courier', 24, 'normal'))