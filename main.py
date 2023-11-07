# TODO Change the behavior if the ball hits the wall. The ball needs to reset unless the score was reached

from character import Paddle
from scoreboard import Scoreboard
from ball import PongBall
from turtle import Screen
from time import sleep

WINDOW_BG_COLOR = "grey"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
REFRESH_RATE = 0.01
BALL_SIZE = 15.0
MAX_SCORE = 10

TESTING = False


def pong_game():

    # Creating class instances
    window = Screen()
    scoreboard = Scoreboard()
    paddle_left = Paddle(orientation="left")
    paddle_right = Paddle(orientation="right")
    pong_ball = PongBall()

    # Modifying the screen
    window.title("Pingu Pongo")
    window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    window.bgcolor(WINDOW_BG_COLOR)
    window.tracer(0)
    window.listen()

    # Setting up left paddle controls
    window.onkeypress(key="w", fun=paddle_left.move_up)
    window.onkeypress(key="s", fun=paddle_left.move_down)

    # Setting up right paddle controls
    window.onkeypress(key="Up", fun=paddle_right.move_up)
    window.onkeypress(key="Down", fun=paddle_right.move_down)

    # Setting game options
    window.onkeypress(key="Escape", fun=window.bye)
    game_is_on: bool = True

    while TESTING or game_is_on:
        sleep(REFRESH_RATE)
        window.update()
        # Handling collisions
        # Paddle collision
        if paddle_left.distance(pong_ball.position()) <= BALL_SIZE or paddle_right.distance(pong_ball.position()) <= BALL_SIZE:
            pong_ball.change_heading()

        pong_ball.move()

        if pong_ball.distance(WINDOW_WIDTH/2*-1, pong_ball.ycor()) <= BALL_SIZE:
            # Change to incrementing a point for right player and resetting the ball
            pass
        elif pong_ball.distance(WINDOW_WIDTH/2, pong_ball.ycor()) <= BALL_SIZE:
            # Change to incrementing a point for left player and resetting the ball
            pass

        # Game ending condition
        if MAX_SCORE == scoreboard.left_score or MAX_SCORE == scoreboard.right_score:
            game_is_on = False

    scoreboard.game_over()
    window.exitonclick()


if __name__ == "__main__":
    pong_game()
