import numpy as np
import turtle

turtle.shape('turtle')
turtle.color('black', 'black')
def draw(x,u):
    g = 1
    while g < (x+1):
        turtle.left(360 / x)
        g = g + 1
        turtle.forward(u)
    turtle.right(90-(180/x))

i = 3
u = 100
while i < 13:

    turtle.penup()
    t=25
    turtle.forward(t)
    turtle.left(90 - (180 / i))
    turtle.pendown()

    draw(i,u)
    u = 2*(t+(u / 2 / np.sin(np.pi / i))) * np.sin(np.pi / (1+i))
    if i == 13:
        break

    i = i + 1
turtle.done()
