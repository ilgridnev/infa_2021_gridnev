import turtle
import random

turtle.shape('turtle')
turtle.color('black', 'black')

i = 0

while i < 50:
    x = random.randint(0, 360)

    turtle.left(x)

    turtle.forward(20)

    i = i + 1

turtle.done()