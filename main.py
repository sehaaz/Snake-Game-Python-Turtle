from turtle import Turtle, Screen
from snak import Snak
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snak = Snak()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snak.up, "Up")
screen.onkey(snak.down, "Down")
screen.onkey(snak.right, "Right")
screen.onkey(snak.left, "Left")

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snak.move()

    if snak.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.increase_score()
        snak.extend()

    if snak.head.xcor() < -300 or snak.head.xcor() > 300 or snak.head.ycor() < -300 or snak.head.ycor() > 300:
        gameIsOn = False
        scoreboard.game_over()

    for snake in snak.snakes:
        if snak.head == snake:
            pass
        elif snak.head.distance(snake) < 10:
            gameIsOn = False
            scoreboard.game_over()



screen.exitonclick()