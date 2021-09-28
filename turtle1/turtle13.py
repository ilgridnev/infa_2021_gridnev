
import turtle

turtle.color('black', 'blue')

def circle(x):
        i = 1
        while i < 73:
            i = i + 1
            turtle.left(5)
            turtle.forward(x)


def hcircle(x):
    i = 1
    while i < 37:
        i = i + 1
        turtle.left(5)
        turtle.forward(x)


turtle.begin_fill()
circle(5)
turtle.end_fill()



turtle.penup()
turtle.goto(15,70)
turtle.color('black')
turtle.pendown()
turtle.begin_fill()
circle(0.6)
turtle.end_fill()
turtle.penup()
turtle.goto(-15, 70)
turtle.color('black')
turtle.pendown()
turtle.begin_fill()
circle(0.6)
turtle.end_fill()


turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.width(3.5)
turtle.goto(0, 40)
turtle.penup()
turtle.goto(-20, 25)
turtle.color("red")
turtle.width(3.5)
turtle.pendown()
turtle.goto(20, 25)
turtle.done()


#№13(5)

import turtle

turtle.shape('turtle')
turtle.color('black', 'black')

turtle.left(90)


def draw(x):
    i = 0
    while i<x:
        i=i+1
        turtle.forward(200)
        turtle.left(180-(180/x))

draw(5)
turtle.done()