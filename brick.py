from turtle import Turtle


class Brick(Turtle):
    """
    Makes the bricks
    """
    def __init__(self, x, y, color):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.penup()
        self.goto(x, y)
        self.x = x
        self.y = y

    def smash(self):
        self.reset()