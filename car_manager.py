from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars= []
        self.hideturtle()
        self.y_position = random.randint(-250, 275)
        self.x_position = random.randint(300, 375)

    def create_car(self):
        self.count=0
        car= Turtle(shape="square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.y_position = random.randint(-250, 275)
        car.x_position = random.randint(300, 675)
        car.goto(car.x_position, car.y_position)
        self.count += 1
        self.cars.append(car)
        return self.cars


    def move(self,cars,speed):
        self.on= True
        for car in cars:
            self.move_speed = speed
            car.forward(self.move_speed)

            if car.xcor() < -280:
                car.goto(310,random.randint(-250, 275))

