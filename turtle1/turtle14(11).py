
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

draw(11)
turtle.done()









