from turtle import Turtle

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
        heading = self.heading()
        if heading > 90 and heading < 270:
            heading += 90
            if heading >= 360:
                heading -= 360
            self.heading(heading)

    def move(self):
        self.forward(self.move_speed)
