from character import Paddle
from scoreboard import Scoreboard
from ball import PongBall
from turtle import Screen
from time import sleep

WINDOW_BG_COLOR = "grey"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
REFRESH_RATE = 0.01
BALL_SIZE = 25.0
BALL_START_CORDS = (0, 0)
PADDLE_WALL_OFFSET = 20
BALL_BOUNCE_OFFSET = BALL_SIZE + PADDLE_WALL_OFFSET
MAX_SCORE = 10

TESTING = False


def pong_game():

    # Creating class instances
    window = Screen()
    scoreboard = Scoreboard()
    paddle_left = Paddle(orientation="left",
                         paddle_wall_offset=PADDLE_WALL_OFFSET)
    paddle_right = Paddle(orientation="right",
                          paddle_wall_offset=PADDLE_WALL_OFFSET)
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
        if paddle_left.distance(pong_ball.position()) <= BALL_BOUNCE_OFFSET \
                and pong_ball.xcor() <= WINDOW_WIDTH/2*-1 + BALL_BOUNCE_OFFSET \
                or paddle_right.distance(pong_ball.position()) <= BALL_BOUNCE_OFFSET \
                and pong_ball.xcor() >= WINDOW_WIDTH/2 - BALL_BOUNCE_OFFSET:
            pong_ball.ball_speed_x *= -1

        # Ceil and floor collision
        if pong_ball.distance(pong_ball.xcor(), WINDOW_HEIGHT/2) <= BALL_SIZE \
                or pong_ball.distance(pong_ball.xcor(), WINDOW_HEIGHT/2*-1) <= BALL_SIZE:
            pong_ball.ball_speed_y *= -1

        # Left and right wall collisions
        if pong_ball.distance(WINDOW_WIDTH/2*-1, pong_ball.ycor()) <= BALL_SIZE:
            scoreboard.update_score("right")
            pong_ball.setposition(BALL_START_CORDS)
            pong_ball.ball_speed_x *= -1
            sleep(1)

        elif pong_ball.distance(WINDOW_WIDTH/2, pong_ball.ycor()) <= BALL_SIZE:
            scoreboard.update_score("left")
            pong_ball.setposition(BALL_START_CORDS)
            pong_ball.ball_speed_x *= -1
            sleep(1)

        # Game ending condition
        if MAX_SCORE == scoreboard.left_score or MAX_SCORE == scoreboard.right_score:
            game_is_on = False

        pong_ball.move()

    scoreboard.game_over()
    window.exitonclick()


if __name__ == "__main__":
    pong_game()
