from character import Paddle
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

WINDOW_BG_COLOR = "black"
REFRESH_RATE = 0.5


def pong_game():

    # Creating class instances
    window = Screen()
    scoreboard = Scoreboard()
    paddle_left = Paddle(orientation="left")
    paddle_right = Paddle(orientation="right")

    # Modifying the screen
    window.title("Pingu Pongo")
    window.bgcolor(WINDOW_BG_COLOR)
    window.exitonclick()

    # Setting up left paddle controls
    window.onkeypress(key="w", fun=paddle_left.move_up)
    window.onkeypress(key="S", fun=paddle_left.move_down)

    # Setting up right paddle controls
    window.onkeypress(key="Up", fun=paddle_right.move_up)
    window.onkeypress(key="Down", fun=paddle_right.move_down)

    while True:
        sleep(REFRESH_RATE)
        window.update()


if __name__ == "__main__":
    pong_game()
