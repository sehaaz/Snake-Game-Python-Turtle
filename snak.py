from turtle import Turtle, Screen

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snak:

    def __init__(self):
        self.snakes = []
        self.create()
        self.head = self.snakes[0]

    def create(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        newSnake = Turtle("square")
        newSnake.penup()
        newSnake.goto(position)
        self.snakes.append(newSnake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):

        for snake in range(len(self.snakes)-1, 0, -1):
            newX = self.snakes[snake-1].xcor()
            newY = self.snakes[snake-1].ycor()
            self.snakes[snake].goto(newX, newY)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)