from turtle import Turtle

FONT = ("Courier", 19, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(0, 266)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 266)
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def point(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
