from turtle import *
import random

turt = Turtle()
turt.shape("turtle")
cmode = colormode(255)


def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


turt.speed("fastest")


def draw_circle():
    for i in range(100):
        turt.color(ran_color())
        turt.circle(100)
        turt.setheading(turt.heading() + 5)


draw_circle()

screen = Screen()
screen.exitonclick()
