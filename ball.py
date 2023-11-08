# TODO Add logic how to randomize the angle leaving a paddle

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
        self.ball_speed_x = 2
        self.ball_speed_y = 2

    # def change_heading(self):
    #     angle: int = int(self.heading())
    #     angle = 180
    #     self.left(angle)

    def move(self):
        x_move_speed = self.xcor() + self.ball_speed_x
        y_move_speed = self.ycor() + self.ball_speed_y
        move_speed = (x_move_speed, y_move_speed)
        self.goto(move_speed)
