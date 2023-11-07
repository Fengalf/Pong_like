# TODO Add logic how to randomise the angle leaving a paddle

from turtle import Turtle
from random import randint

BALL_SHAPE = "circle"
BALL_COLOR = "blue"


class PongBall(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.speed("fast")
        self.move_speed = 5

    def change_heading(self):
        angle: int = int(self.heading())
        angle = 180  # + randint(-20, 20)
        self.left(angle)

    def move(self):
        self.forward(self.move_speed)
