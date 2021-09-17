import turtle

turtle.shape('turtle')
turtle.color('black', 'black')

turtle.left(90)
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
i=5
while i<16:
    drawl(i)
    drawr(i)
    i=i+2
turtle.done()