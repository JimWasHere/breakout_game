from turtle import Turtle


class Paddle(Turtle):
    """
    Creates the paddle to bounce the ball
    """
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color("grey43")
        self.penup()
        self.goto(x, y)
        self.ondrag(self.drag)

    def drag(self, x, y):
        self.ondrag(None)
        self.goto(x, (y-y-325))
        self.ondrag(self.drag)