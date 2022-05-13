from turtle import Turtle
import random

color_list = ["blue", "red", "green", "cyan", "magenta", "yellow"]

class CarManagement():
    
    def __init__(self):
        self.all_car = []
        self.CarSpeed = 2
        
    def CreateCar(self):
        car_create_time = random.randint(1, 10)
        if car_create_time == 3:
            car = Turtle("square")
            car.penup()
            car.shapesize(1, 2)
            car.color(random.choice(color_list))
            car.goto(300, random.randint(-230, 230))
            self.all_car.append(car)
    
    def Move(self):
        for car in self.all_car:
            car.backward(self.CarSpeed)
            
    def LevelUp(self):
        self.CarSpeed *= 2