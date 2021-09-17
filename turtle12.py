import turtle

turtle.shape('turtle')
turtle.color('black', 'black')

turtle.left(90)


def draw(x):
    i = 1
    while i < 37:
        i = i + 1
        turtle.right(5)
        turtle.forward(x)



i = 5
while i < 16:
    draw(5)
    draw(2)
    i = i + 2
turtle.done()
