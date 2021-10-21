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

balls = []


class Ball:
    def __init__(self, number, existence, r, x, y, speedX, speedY, color):
        global balls
        balls.append(self)
        self.number = number
        self.existence = existence
        self.r = r
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.color = color

    def reflection(self):
        '''
        функция изменяет направления и значения скоростей при ударе шаров о стенку
        на вход принимает переменную number
        number номер шара
        '''
        if self.x > 400 - self.r:
            self.speedX = randint(-10, 0)
        elif self.x < self.r:
            self.speedX = randint(0, 10)
        if self.y > 400 - self.r:
            self.speedY = randint(-10, 0)
        elif self.y < self.r:
            self.speedY = randint(0, 10)

    def move(self):
        '''
        функция двигает (перерисовывает) шар на экране в соответствии с его скоростью
        на вход принимает переменную number
        number номер шара
        '''
        self.x += self.speedX
        self.y += self.speedY
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


def generate_balls(n=6):
    for i in range(n):
        ball = Ball(1, 1, randint(30, 50),  # случайный радиус
                    randint(50, 350),  # случайная х координата
                    randint(50, 350),  # случайная y координата
                    randint(-10, 10),  # случайная скорость по х
                    randint(-10, 10),  # случайная скорость по y
                    (randint(10, 255),  # случайный цвет
                     randint(10, 255),
                     randint(10, 255)))


generate_balls()

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
            for ball in balls:
                if (ball.x - shootX) ** 2 + (ball.y - shootY) ** 2 <= ball.r ** 2:
                    ball.existence = 0
                    score = score + 1
    screen.fill(BLACK)
    for i, ball in enumerate(balls):
        if ball.existence == 0:
            del balls[i]
            ball = Ball(1, 1, randint(30, 50),  # случайный радиус
                        randint(50, 350),  # случайная х координата
                        randint(50, 350),  # случайная y координата
                        randint(-10, 10),  # случайная скорость по х
                        randint(-10, 10),  # случайная скорость по y
                        (randint(10, 255),  # случайный цвет
                         randint(10, 255),
                         randint(10, 255)))
            ball.existence = 1

        ball.reflection()

        ball.move()

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


def file_reading():
    """
    функция возвращает из файла два массива с именами игроков и их баллами.
    """
    points = [""] * 5
    names = [""] * 5

    f = open("hall of fame.txt", "r")
    file = f.readlines()
    for i in range(1, 6):
        string = file[i]
        pos = -1
        while string[pos] != " ":
            points[i - 1] = string[pos] + points[i - 1]
            pos -= 1
        pos = 3
        while string[pos] != ",":
            names[i - 1] = names[i - 1] + string[pos]
            pos += 1
    for i in range(5):
        points[i] = points[i].replace("\n", "")

    f.close()

    return points, names


def file_writing(points, names):
    '''
    функция записывает в файл новые результаты.
    points это массив с результатами пяти лучших игроков.
    names это массив с именами пяти лучших игроков.
    '''
    f = open("hall of fame.txt", "w")
    f.write("Top players: \n")

    i = 1
    boolean = True
    while i < 6 and boolean:
        if score > int(points[i - 1]):
            f.write(str(i) + ". " + username + ", score: " + str(score) + "\n")
            boolean = False
        else:
            f.write(str(i) + ". " + names[i - 1] + ", score: " + points[i - 1] + "\n")
        i += 1

    if not boolean:
        for j in range(i, 6):
            f.write(str(j) + ". " + names[j - 2] + ", score: " + points[j - 2] + "\n")

    f.close()


points, names = file_reading()
file_writing(points, names)

pygame.quit()
