from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)

        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def add_segment(self, position):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snake_body.append(body)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            x_pos = self.snake_body[seg_num - 1].xcor()
            y_pos = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x_pos, y_pos)
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


