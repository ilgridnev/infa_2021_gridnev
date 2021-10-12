# инициализация экрана, подключение библиотек
import pygame
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((400, 400))

# явное перечисление используемых цветов, присваивание им соответствующих названий
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def click(event):
    print(x, y, r)


def new_ball():
    global x, y, r
    x = randint(50, 350)
    y = randint(50, 350)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
