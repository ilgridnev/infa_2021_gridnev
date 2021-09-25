import turtle

target = list(str(input()))

turtle.shape('turtle')
turtle.color('black', 'black')




def draw(turn, step, pen):
    if pen == 1:
        turtle.penup()
        turtle.left(turn)
        turtle.forward(step)
        turtle.pendown()
    else:
        turtle.left(turn)
        turtle.forward(step)


for i in target:
    with open("numpath.txt") as f:
        path = f.readlines()[int(i)]
    path = path.replace("(", "")
    path = path.replace(")", "")
    path = path.replace("\n", "")
    path = path.split(", ")
    for j in range(len(path) // 3):
        draw(float(path[j * 3]), float(path[j * 3 + 1]), float(path[j * 3 + 2]))

turtle.done()

