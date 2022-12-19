import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title('Ping Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.l_go_up, 'Up')
screen.onkey(l_paddle.l_go_down, 'Down')
screen.onkey(r_paddle.r_go_up, 'w')
screen.onkey(r_paddle.r_go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 30 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()
        ball.x_bounce()

    if ball.xcor() < -400:
        score.r_point()
        ball.reset_position()
        ball.x_bounce()


screen.exitonclick()
