from turtle import Turtle, Screen

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segmens = []
        self.create_snake()
        self.head = self.segmens[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segmen(position)

    def add_segmen(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.segmens.append(new_square)

    def extend(self):
        self.add_segmen(self.segmens[-1].position())

    def move(self):
        for seg_num in range (len(self.segmens) - 1, 0, -1):
            new_x = self.segmens[seg_num-1].xcor()
            new_y = self.segmens[seg_num - 1].ycor()
            self.segmens[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)