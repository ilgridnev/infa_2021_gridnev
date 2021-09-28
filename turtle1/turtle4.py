from turtle import *
color('black', 'black')
shape('turtle')
while True:
    forward(5)
    left(5)
    if abs(pos()) < 1:
        break
done()
