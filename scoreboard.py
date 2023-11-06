from turtle import Turtle

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        # setting attributes
        self.left_score = 0
        self.right_score = 0
        self.size = 15
        self.centerline = []

        # calling initializing methods
        self.create_center_line()
        self.left_counter = self.create_counter("left")
        self.right_counter = self.create_counter("right")

    def create_center_line(self):
        for y_cord in range(int(WINDOW_HEIGHT/2)-(self.size*2), (int(WINDOW_HEIGHT/2)-self.size)*-1, self.size*-2):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.turtlesize(stretch_wid=1.05, stretch_len=0.25)
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.speed("fastest")
            new_segment.setposition((0, y_cord))
            self.centerline.append(new_segment)

    def create_counter(self, orientation: str):
        self.hideturtle()
        self.turtlesize(self.size, self.size)
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        if orientation == "left":
            self.setposition((-45, WINDOW_HEIGHT/2-(self.size*2)))
            self.write(self.left_score, font=("Arial", self.size, "bold"))
        else:
            self.setposition((40, WINDOW_HEIGHT/2-(self.size*2)))
            self.write(self.right_score, font=("Arial", self.size, "bold"))
