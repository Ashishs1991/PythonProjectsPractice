from turtle import Turtle, Screen
import random

colorOfTurtle = ["red", "yellow", "green", "blue", "purple", "orange"]
distance1 = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for i in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colorOfTurtle[i])
    newTurtle.goto(-230, distance1[i])
    all_turtles.append(newTurtle)

sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win enter the color: ")

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you Won and {winning_color} color turtle wins")
            else:
                print(f"you Lost and {winning_color} color turtle wins")
        rand_=random.randint(0,10)
        turtle.forward(rand_)

sc.exitonclick()
