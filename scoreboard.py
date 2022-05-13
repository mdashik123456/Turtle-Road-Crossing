from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 1
        
    def ScorePrint(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Level : {self.Level}", False, "center", ("courier", 16, "normal"))
        
    def UpdateScore(self):
        self.clear()
        self.Level += 1
    
    def GameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("courier", 16, "bold"))