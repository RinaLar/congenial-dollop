import turtle
import random

turtle.pensize(1)

for x in range(0,12):
        turtle.color(random.choice( ["red", "blue", "yellow", "green", "pink", "orange",'mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'limegreen', 'darkgreen', 'yellow', 'darkorange']))
        for i in range(0,12):
            turtle.forward(61-5*i+20*x)
            turtle.right(90)
        turtle.right(60)
turtle.hideturtle()

