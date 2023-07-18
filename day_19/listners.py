from turtle import Turtle, Screen

for i in range(0, 4):
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color("red")
    turtle1.goto(-230, -100)

sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win enter the color: ")
sc.exitonclick()
