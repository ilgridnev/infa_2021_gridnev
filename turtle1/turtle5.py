import turtle
turtle.shape('turtle')
i = 10
while i < 101:
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.right(45)
    turtle.penup()
    turtle.forward(5*1.41)
    turtle.pendown()
    turtle.left(135)
    i = i + 10