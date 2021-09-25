import turtle

turtle.shape('turtle')
turtle.color('black', 'black')
x = 0
y = 0
Vx = 5
Vy = 25
ay = -2
dt = 0.2
for i in range(1000):
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    turtle.goto(x, y)
    if y <= 0:
        Vy = -Vy

turtle.done()
