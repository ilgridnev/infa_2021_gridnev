# запрос данных об игроке, вывод правил игры на экран
print("Hello player! \n"
      "Remember, you have only 6 shots, use them carefully\n"
      "please, enter your name ...")

username = str(input())  # переменная для имени игрока

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

global shots  # переменная отвечающая за количество выстрелов игрока
shots = 6

balllist = [0] * 6  # массив, отвечающий за наличие/отсутствие шаров на экране (1/0 соответственно)
r = [0] * 6  # массив, отвечающий за хранение радиусов шаров
x = [0] * 6  # массив, отвечающий за хранение х координаты шаров
y = [0] * 6  # массив, отвечающий за хранение у коордирнаты шаров
speedX = [0] * 6  # массив, отвечающий за хранение скорости по х координате шаров
speedY = [0] * 6  # массив, отвечающий за хранение скорости по у координате шаров
color = [0] * 6  # массив, отвечающий за хранение цветов шаров


def existence(number, status):
    '''
    функция явно показывает изменение статуса существования шара
    на вход принимает две переменные number, status
    number номер шара
    status новый статус
    '''

    balllist[number] = status


def new_ball(number):
    '''
    функция создает новый шар на экране
    на вход принимает переменную number
    number номер шара
    '''
    existence(number, 1)  # объявляем существование
    x[number] = randint(50, 350)  # случайная х координата
    y[number] = randint(50, 350)  # случайная у координата
    r[number] = randint(30, 50)  # случайный радиус
    speedX[number] = randint(-10, 10)  # случайная скорость по х
    speedY[number] = randint(-10, 10)  # случайная скорость по у
    color[number] = (randint(10, 255), randint(10, 255), randint(10, 255))  # случайный цвет, без черного
    pygame.draw.circle(screen, color[number], (x[number], y[number]), r[number])  # отрисовка шара

def reflection(number):
    '''
    функция изменяет направления и значения скоростей при ударе шаров о стенку
    на вход принимает переменную number
    number номер шара
    '''
    if x[number] > 400 - r[number]:
        speedX[number] = randint(-10, 0)
    elif x[number] < r[number]:
        speedX[number] = randint(0, 10)
    if y[number] > 400 - r[number]:
        speedY[number] = randint(-10, 0)
    elif y[number] < r[number]:
        speedY[number] = randint(0, 10)

def move(number):
    '''
    функция двигает (перерисовывает) шар на экране в соответствии с его скоростью
    на вход принимает переменную number
    number номер шара
    '''
    x[number] = x[number] + speedX[number]
    y[number] = y[number] + speedY[number]
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

        reflection(number)

        move(number)

    font = pygame.font.Font(None, 20)  # настраиваем шрифт для выведения надписей на экран

    text1 = font.render("score", True, [255, 255, 255])  # выводим надпись score на экран
    text1pos = (160, 10)
    screen.blit(text1, text1pos)

    text2 = font.render(str(score), True, [255, 255, 255])  # выводим счет на экран, справа от надписи score
    text2pos = (200, 10)
    screen.blit(text2, text2pos)

    text3 = font.render("shots", True, [255, 255, 255])  # выводим надпись shots на экран
    text3pos = (160, 23)
    screen.blit(text3, text3pos)

    text4 = font.render(str(shots), True, [255, 255, 255])  # выводим количество оставшихся выстрелов на экран
    text4pos = (200, 23)
    screen.blit(text4, text4pos)

    pygame.display.update()

pygame.quit()
