from turtle import Turtle

WINDOW_WIDTH: int = 480
WINDOW_HEIGHT: int = 480
HEADINGS: dict = {
    "up": 90,
    "down": 270,
}


class Paddle(Turtle):
    def __init__(self, orientation: str, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.orientation = orientation.lower()
        self.segments = 5
        self.y_offset = 40
        self.size = 20
        self.segment_list = []
        self.build_segment()

    def build_segment(self):
        """
            Creating the paddle
        """

        if self.orientation == "left":
            x_offset = (WINDOW_WIDTH/2 - self.size) * -1
        else:
            x_offset = (WINDOW_WIDTH/2 - self.size)

        for _ in range(0, self.segments, 1):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.speed("fastest")
            new_segment.shape("square")
            new_segment.setposition(x_offset, self.y_offset)
            self.segment_list.append(new_segment)
            self.y_offset -= 20

    def move_up(self):
        """
            Moves the paddle up
        """
        if self.segment_list[0].distance(self.segment_list[0].xcor(), int(WINDOW_HEIGHT/2)-self.size) >= self.size:
            for index in range(len(self.segment_list)-1, 0, -1):
                goto_pos = self.segment_list[index-1].pos()
                self.segment_list[index].setpos(goto_pos)
            self.segment_list[0].setheading(HEADINGS["up"])
            self.segment_list[0].forward(self.size)

    def move_down(self):
        """
            Moves the paddle up
        """
        if self.segment_list[-1].distance(self.segment_list[-1].xcor(), (int(WINDOW_HEIGHT/2)-self.size)*-1) >= self.size:
            for index in range(0, len(self.segment_list), 1):
                if index != len(self.segment_list)-1:
                    goto_pos = self.segment_list[index+1].pos()
                    self.segment_list[index].setpos(goto_pos)
            self.segment_list[-1].setheading(HEADINGS["down"])
            self.segment_list[-1].forward(self.size)
