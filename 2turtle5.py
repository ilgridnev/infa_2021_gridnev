from random import randint
import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(211, 211)
turtle.pendown()
turtle.goto(211, -211)
turtle.goto(-211, -211)
turtle.goto(-211, 211)
turtle.goto(211, 211)

number_of_turtles = 16
steps_of_time_number = 1000

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(0, 360))

for i in range(steps_of_time_number):
    for unit in pool:

        unit.forward(2)
        if unit.xcor() > 200:
            unit.setheading(randint(90, 270))
        if unit.xcor() < -200:
            unit.setheading(randint(270, 450))
        if unit.ycor() > 200:
            unit.setheading(randint(180, 360))
        if unit.ycor() < -200:
            unit.setheading(randint(0, 180))
