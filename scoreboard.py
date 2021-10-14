from turtle import Turtle


FONT = ("Courier", 24, "normal")
Alignment = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.penup()
        self.goto(-200,250)
        self.speed("fastest")
        self.color("black")
        self.write(f'Level: {self.level}', move=False, font=FONT, align=Alignment)
        self.hideturtle()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-200, 250)
        self.color("black")
        self.write(f'Level: {self.level}', move=False, font=FONT, align=Alignment)

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("Game Over", move=False, font=FONT, align=Alignment)