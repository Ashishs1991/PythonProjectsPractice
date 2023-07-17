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





def draw_dotted_line():
    for i in range(1, 100):
        turt.pendown()
        turt.forward(10.0)
        turt.penup()
        turt.forward(10.0)


def draw_triangle():
    turt.forward(100.0)
    turt.left(120.0)
    turt.forward(100.0)
    turt.left(120.0)
    turt.forward(100.0)


# //Draws all the shapes
def draw_shape(i):
    turt.color(ran_color())
    angle = 360 / i
    for i in range(1, i + 1):
        turt.forward(100.0)
        turt.left(angle)


def draw_all_shapes():
    for i in range(3, 13):
        draw_shape(i)


draw_all_shapes()


def draw_circle():
    turt.forward(100.0)
    turt.right(90.0)
    turt.forward(100.0)
    turt.right(90.0)
    turt.forward(100.0)
    turt.right(90.0)
    turt.forward(100.0)
    turt.right(90.0)


screen = Screen()
screen.exitonclick()
