import time
from turtle import Turtle, Screen

dist = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(dist[i])
    segments.append(new_turtle)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.exitonclick()

game_is_on = True

while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
        time.sleep(1)

