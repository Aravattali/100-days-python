import turtle
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_start()
        self.setheading(90)

## go up functionality for the turtle.

    def go_up(self):
        self.forward(MOVE_DISTANCE)

## when the turtle reaches the top line, it restarts from the bottom.
    def go_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False


