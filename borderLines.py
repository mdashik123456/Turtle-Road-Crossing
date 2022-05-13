from turtle import Turtle

class BorderLine(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        
        self.shape("square")
        self.penup()
        self.color("green")
        self.shapesize(0.1, 35)
        self.goto(x_pos, y_pos)