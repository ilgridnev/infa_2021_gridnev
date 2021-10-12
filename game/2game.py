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

# создаем массив цветов, чтобы можно было рандомно их генерировать через их номера в массиве
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global score
score = 0


def new_ball():
    global x, y, r, color, speedX, speedY, existence
    existence = 1
    x = randint(50, 350)
    y = randint(50, 350)
    r = randint(30, 50)
    speedX = randint(-10, 10)
    speedY = randint(-10, 10)
    color = (randint(10, 255), randint(10, 255), randint(10, 255))
    pygame.draw.circle(screen, color, (x, y), r)


clock = pygame.time.Clock()
finished = False
new_ball()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (shootX, shootY) = event.pos
            if ((x - shootX) ** 2 + (y - shootY) ** 2 <= r ** 2):
                existence = 0
                score = score + 1
    if existence == 0:
        screen.fill(BLACK)
        new_ball()
    else:
        screen.fill(BLACK)
        if x > 400 - r:
            speedX = randint(-10, 0)
        elif x < r:
            speedX = randint(0, 10)
        if y > 400 - r:
            speedY = randint(-10, 0)
        elif y < r:
            speedY = randint(0, 10)

        x = x + speedX
        y = y + speedY
        pygame.draw.circle(screen, color, (x, y), r)

    font = pygame.font.Font(None, 20)
    text1 = font.render("score", True, [255, 255, 255])
    text1pos = (160, 10)
    text2 = font.render(str(score), True, [255, 255, 255])
    text2pos = (200, 10)
    screen.blit(text1, text1pos)
    screen.blit(text2, text2pos)

    pygame.display.update()

pygame.quit()
