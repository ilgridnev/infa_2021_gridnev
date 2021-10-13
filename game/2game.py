print("Hello player! please, enter your name ...")
username = str(input())

# инициализация экрана, настройка частоты обновления, подключение библиотек
import pygame
from random import randint

pygame.init()

FPS = 25
screen = pygame.display.set_mode((400, 400))

# явное перечисление используемых цветов, присваивание им соответствующих названий
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# создаем массив цветов, чтобы была возможность вызывать их по номеру
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global score  # создаем переменную отвечающую за счет игрока, присваиваем ей изначальное значение 0
score = 0

global shots
shots = 3

balllist = [0, 0, 0, 0, 0, 0]
r = [0, 0, 0, 0, 0, 0]
x = [0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0]
speedX = [0, 0, 0, 0, 0, 0]
speedY = [0, 0, 0, 0, 0, 0]
color = [0, 0, 0, 0, 0, 0]


def existence(number, status):
    balllist[number] = status


def new_ball(number):
    existence(number, 1)
    x[number] = randint(50, 350)
    y[number] = randint(50, 350)
    r[number] = randint(30, 50)
    speedX[number] = randint(-10, 10)
    speedY[number] = randint(-10, 10)
    color[number] = (randint(10, 255), randint(10, 255), randint(10, 255))
    pygame.draw.circle(screen, color[number], (x[number], y[number]), r[number])


clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shots = shots - 1
            if shots == 0:
                finished = True
            (shootX, shootY) = event.pos
            for number in range(6):
                if ((x[number] - shootX) ** 2 + (y[number] - shootY) ** 2 <= r[number] ** 2):
                    existence(number, 0)
                    score = score + 1
    screen.fill(BLACK)
    for number in range(6):
        if balllist[number] == 0:
            new_ball(number)
            existence(number, 1)

        if x[number] > 400 - r[number]:
            speedX[number] = randint(-10, 0)
        elif x[number] < r[number]:
            speedX[number] = randint(0, 10)
        if y[number] > 400 - r[number]:
            speedY[number] = randint(-10, 0)
        elif y[number] < r[number]:
            speedY[number] = randint(0, 10)

        x[number] = x[number] + speedX[number]
        y[number] = y[number] + speedY[number]
        pygame.draw.circle(screen, color[number], (x[number], y[number]), r[number])

    font = pygame.font.Font(None, 20)  # настраиваем шрифт для выведения надписи на экран

    text1 = font.render("score", True, [255, 255, 255])  # выводим надпись score на экран
    text1pos = (160, 10)
    screen.blit(text1, text1pos)

    text2 = font.render(str(score), True, [255, 255, 255])  # выводим счет на экран, справа от надписи score
    text2pos = (200, 10)
    screen.blit(text2, text2pos)

    text3 = font.render("shots", True, [255, 255, 255])  # выводим счет на экран, справа от надписи score
    text3pos = (160, 23)
    screen.blit(text3, text3pos)

    text4 = font.render(str(shots), True, [255, 255, 255])  # выводим счет на экран, справа от надписи score
    text4pos = (200, 23)
    screen.blit(text4, text4pos)

    pygame.display.update()
scores = [0] * 10
line = str(score) + " " + username
with open("highscores.txt", "w") as f:
    f.write(line + '\n')
    '''
    i = 0
    for line in f:
        helpline = filter(str.isdecimal, line)
        scores[i] = "".join(helpline)
        i = i + 1
    newscores = [0] * 11
    for i in range(10):
        newscores[i] = scores[i]
    newscores[10] = score
    newscores=sorted(newscores, reverse=True)
with open("highscores.txt", "w") as f:
    place = 0
    x = 0
    while scores[x] == newscores[x]:
        x = x + 1
    while (9-place) != x:
        f.write(line + '\n')/
'''
pygame.quit()
