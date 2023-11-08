from turtle import Turtle

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)

        # setting attributes
        self.left_score = 0
        self.right_score = 0
        self.size = 15
        self.centerline = []

        # calling initializing methods
        self.create_center_line()
        self.counter = {
            "left_counter": self.create_counter("left"),
            "right_counter": self.create_counter("right")
        }

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
        new_counter = Turtle()
        new_counter.hideturtle()
        new_counter.turtlesize(self.size, self.size)
        new_counter.penup()
        new_counter.color("white")
        new_counter.shape("square")
        new_counter.speed("fastest")
        if orientation == "left":
            new_counter.setposition(
                (-45, WINDOW_HEIGHT/2-(self.size*2)))
            new_counter.write(self.left_score, font=(
                "Arial", self.size, "bold"))
        else:
            new_counter.setposition((40, WINDOW_HEIGHT/2-(self.size*2)))
            new_counter.write(self.right_score, font=(
                "Arial", self.size, "bold"))

        return new_counter

    def game_over(self):
        self.hideturtle()
        self.turtlesize(self.size, self.size)
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.setposition(0, 0)
        self.write("Game over!",
                   align="center",
                   font=("Arial", self.size, "bold"))

    def update_score(self, orientation_scored: str):
        if orientation_scored == "left":
            self.left_score += 1
            self.counter["left_counter"].clear()
            self.counter["left_counter"].write(self.left_score, font=(
                "Arial", self.size, "bold"))
        elif orientation_scored == "right":
            self.right_score += 1
            self.counter["right_counter"].clear()
            self.counter["right_counter"].write(self.right_score, font=(
                "Arial", self.size, "bold"))
