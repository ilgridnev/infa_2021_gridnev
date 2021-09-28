from turtle import *
shape('turtle')
color('black', 'black')
n = 12
i = 1
while True:
    forward(100)
    stamp()
    left(180)
    forward(100)
    left(180)
    left(360/n)
    i = i+1
    if i == (n+1):
        break
done()