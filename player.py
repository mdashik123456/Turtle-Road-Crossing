from turtle import Turtle, xcor

# STARTING_POSITION = (0, -270)

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)
        
    def go_up(self):
        if self.ycor() < 240:
            self.forward(20)
            
    def go_down(self):
        if self.ycor() > -270:
            self.backward(20)
            
    def go_left(self):
        if self.xcor() > -300:
            self.setheading(180)
            self.forward(20)
            self.setheading(90)
            
    def go_right(self):
        if self.xcor() < 280:
            self.setheading(0)
            self.forward(20)
            self.setheading(90)