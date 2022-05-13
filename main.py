from turtle import Screen
from player import Player
from borderLines import BorderLine
from car_manager import CarManagement
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("sky blue")
screen.setup(600, 600)
screen.tracer(0)

turtle = Player()

top_border = BorderLine(0, 250)
bottom_border = BorderLine(0, -250)

screen.listen()
screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")
screen.onkey(turtle.go_left, "Left")
screen.onkey(turtle.go_right, "Right")

car = CarManagement()
score = ScoreBoard()

# Mian game loop
isGameOn = True
while isGameOn:
    screen.update()
    time.sleep(0.03)
    car.CreateCar()
    car.Move()
    
    # Detect collision with car
    for c in car.all_car:
        if c.distance(turtle) < 20:
            score.GameOver()
            isGameOn = False
    
    # Detect last line with level up
    if turtle.ycor() >= 250:
        score.UpdateScore()
        car.LevelUp()
        turtle.goto(0, -270)
        
    score.ScorePrint()

screen.exitonclick()
