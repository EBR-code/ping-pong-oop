from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = ScoreBoard((300, 250))
l_scoreboard = ScoreBoard((-300, 250))


screen.title("Edson's Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect if right paddle misses
    if ball.xcor() > 340:
        ball.serve_other()
        l_scoreboard.increase_score()
    #Detect if left paddle misses
    if ball.xcor() < -340:
        ball.serve_other()
        r_scoreboard.increase_score()
    # Detect collision with Y ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
