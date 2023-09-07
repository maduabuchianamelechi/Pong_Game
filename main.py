from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with the Paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the Paddle_1 misses the ball
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect when the Paddle_2 misses the ball
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
