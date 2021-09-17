import turtle

turtle.shape('turtle')
turtle.color('black', 'black')


def drawl(x):
    i = 1
    while i < 73:
        i = i + 1
        turtle.left(5)
        turtle.forward(x)


def drawr(x):
    i = 1
    while i < 73:
        i = i + 1
        turtle.right(5)
        turtle.forward(x)


drawl(5)
drawr(5)
turtle.left(60)
drawl(5)
drawr(5)
turtle.left(60)
drawl(5)
drawr(5)
turtle.done()