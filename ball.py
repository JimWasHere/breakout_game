import random
from turtle import Turtle


class Ball(Turtle):
    """
    Creates a ball to break the bricks and sets it in motion
    """
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.goto(0, -304)
        self.x_move = random.choice([-8, 8])
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        print(self.y_move)

    def bounce_x(self):
        self.x_move *= -1
        print(self.x_move)

    def reset(self):
        self.goto(0, -304)
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.93