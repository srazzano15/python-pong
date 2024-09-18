from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from pong_ball import PongBall
import time

player1 = Player(1)
player2 = Player(2)
scoreboard = Scoreboard()
ball = PongBall()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


screen.onkeypress(player1.move_up, player1.controls['up'])
screen.onkeypress(player1.move_down, player1.controls['down'])
screen.onkeypress(player2.move_up, player2.controls['up'])
screen.onkeypress(player2.move_down, player2.controls['down'])
screen.listen()
game_is_on = True
ball_speed = 0.1


while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(player2) < 54 and ball.xcor() > 320 and ball.xcor() < 350) or (ball.distance(player1) < 54 and ball.xcor() < -320 and ball.xcor() > -350):
        ball.bounce_x()
        if ball_speed > 0.01:
            ball_speed -= 0.01
    # detect player 1 paddle miss
    if ball.xcor() < -390:
        ball_speed = 0.1
        ball.reset_position()
        scoreboard.l_point()

    # detect player 2 paddle miss
    if ball.xcor() > 390:
        ball_speed = 0.1
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()