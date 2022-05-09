from turtle import Turtle, Screen
import time
from ball import Ball
from brick import Brick
from paddle import Paddle


def lay_bricks():
    colors = ["firebrick", "blue", "green", "orange"]
    bricks = []
    y = 95
    for _ in range(4):
        x = -455
        for z in range(11):
            brick = Brick(x, y, colors[_])
            bricks.append(brick)
            x += 90
        y += 50
    return bricks


def game():
    screen = Screen()
    screen.setup(height=800, width=1000)
    screen.bgcolor("black")
    screen.title("Breakout!")
    screen.listen()
    screen.tracer(0)
    bricks = lay_bricks()
    paddle = Paddle(0, -325)
    ball = Ball()

    game_on = True
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

    # detect collision with wall
        if ball.xcor() > 480 or ball.xcor() < -480:
            ball.bounce_x()

    # detect collision with ceiling
        if ball.ycor() > 380:
            ball.bounce_y()

    # detect collision with paddle:
        if ball.distance(paddle) < 100 and ball.ycor() < -310:
            ball.bounce_y()

    # detect collision with brick
        for brick in bricks:
            if ball.distance(brick) < 45 and ball.ycor() <= brick.ycor():
                if ball.y_move > 0:
                    ball.bounce_y()
                else:
                    ball.bounce_x()
                bricks.remove(brick)

                brick.smash()
                ball.increase_speed()

    # detect if ball lost or there are no more bricks
        if len(bricks) == 0:
            winner = Turtle()
            winner.color("green")
            winner.hideturtle()
            winner.penup()
            winner.write("You Win!", align="center", font=("Courier", 80, 'bold'))
            time.sleep(5)
            screen.clearscreen()
            game()
        elif ball.ycor() < -375:
            screen.clearscreen()
            loser = Turtle()
            loser.hideturtle()
            loser.color("purple")
            loser.write("You Lose", align="center", font=("Courier", 80, 'bold'))
            time.sleep(5)
            screen.clearscreen()
            game()
    screen.exitonclick()
game()

