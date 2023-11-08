from turtle import Turtle

WINDOW_HEIGHT: int = 600
WINDOW_WIDTH: int = 800
PADDLE_COLOR: str = "white"
PADDLE_HEIGHT: float = 5
PADDLE_WIDTH: float = 1
PADDLE_PACE: int = 15  # Setting the movement speed of the paddles
PADDLE_PADDING: int = 15  # Setting the padding to the wall
PADDLE_SHAPE: str = "square"
PADDLE_SPEED: int = "fastest"  # Setting the animation speed of the paddles
PADDLE_X_POS: int = int(WINDOW_WIDTH/2-PADDLE_PADDING)
PADDLE_MAX_Y_POS: int = int(WINDOW_HEIGHT/2-PADDLE_PADDING)
HEADINGS: dict = {
    "up": 90,
    "down": 270,
}


class Paddle(Turtle):
    def __init__(self, orientation: str, paddle_wall_offset: int, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.orientation = orientation.lower()
        self.paddle_wall_offset = paddle_wall_offset
        self.turtlesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.speed(PADDLE_SPEED)
        self.place_paddle()

    def place_paddle(self):
        if self.orientation == "left":
            self.setposition(PADDLE_X_POS*-1 + self.paddle_wall_offset, 0)
        elif self.orientation == "right":
            self.setposition(PADDLE_X_POS - self.paddle_wall_offset, 0)

    def move_up(self):
        """
            Moves the paddle up
        """
        current_y = self.ycor()
        new_y = current_y + PADDLE_PACE
        if self.distance(self.xcor(), PADDLE_MAX_Y_POS) >= PADDLE_WIDTH:
            self.setposition(self.xcor(), new_y)

    def move_down(self):
        """
            Moves the paddle up
        """
        current_y = self.ycor()
        new_y = current_y - PADDLE_PACE
        if self.distance(self.xcor(), PADDLE_MAX_Y_POS*-1) >= PADDLE_WIDTH:
            self.setposition(self.xcor(), new_y)
