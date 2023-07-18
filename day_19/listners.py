from turtle import Turtle, Screen

# turtle1 = Turtle()
# turtle1.penup()
# turtle1.shape("turtle")
# turtle1.color("red")
# turtle1.goto(-230,-100)
#
# turtle2 = Turtle()
# turtle2.penup()
# turtle2.shape("turtle")
# turtle2.color("green")
# turtle2.goto(-230,-50)
#
# turtle3 = Turtle()
# turtle3.penup()
# turtle3.shape("turtle")
# turtle3.color("yellow")
# turtle3.goto(-230,0)

for i in range(0, 4):
    turtle1 = Turtle(shape="turtle")
    turtle1.penup()
    turtle1.color("red")
    turtle1.goto(-230, -100)

sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win enter the color: ")
sc.exitonclick()
