from turtle import Turtle

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        # setting attributes
        self.left_score = 0
        self.right_score = 0

        # calling initializing methods
        self.create_center_line()
        self.left_counter = self.create_counter("left")
        self.right_counter = self.create_counter("right")

    def create_center_line(self):
        for y_cord in range(int(WINDOW_HEIGHT/2)*-1, int(WINDOW_HEIGHT/2), -15):
            self.penup()
            self.color("white")
            self.shape("square")
            self.speed("fastest")
            self.setposition((0, y_cord))

    def create_counter(self, orientation: str):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.shape("square")
        self.speed("fastest")
        if orientation == "left":
            self.setpos((-30, WINDOW_HEIGHT))
            self.write(self.left_score, font=("Arial", 15, "bold"))
        else:
            self.setpos((30, WINDOW_HEIGHT))
            self.write(self.right_score, font=("Arial", 15, "bold"))
