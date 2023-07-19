from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __int__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for POSITIONS in STARTING_POSITIONS:
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(POSITIONS)
            self.segments.append(new_snake)

    def move(self):
        for seg in self.segments:
            new_x=seg
