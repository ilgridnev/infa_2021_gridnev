import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def ghost(a, b, c, d, side):  # призрак side выбирает направление взгляда 1 налево, 2 направо
    i = c / 6
    j = d / 10
    place = pygame.Surface((c, d), pygame.SRCALPHA)
    pygame.draw.ellipse(place, (0, 200, 100, 160), (i, 0, 4 * i, 6 * j))
    pygame.draw.polygon(place, (0, 200, 100, 160),
                        [[i, 3 * j], [0, 9 * j], [i, 8 * j],
                         [2 * i, 10 * j], [2 * i, 7 * j], [3 * i, 9 * j], [3 * i, 8 * j], [4 * i, 10 * j],
                         [4 * i, 8 * j], [5 * i, 9 * j], [5 * i, 8 * j], [6 * i, 10 * j], [5 * i, 3 * j]])
    if side == 1:
        pygame.draw.ellipse(place, (230, 0, 0, 200), (7 * i / 4, 2 * j, i / 2, j))
        pygame.draw.ellipse(place, (0, 0, 0, 200), (7 * i / 4, 2 * j, i / 2, j), 2)
        pygame.draw.ellipse(place, (230, 0, 0, 200), (11 * i / 4, 2 * j, i / 2, j))
        pygame.draw.ellipse(place, (0, 0, 0, 200), (11 * i / 4, 2 * j, i / 2, j), 2)

    screen.blit(place, (a, b))


def cloud(a, b, c, d, e, f, g, ):  # облако
    pygame.draw.ellipse(screen, (a, b, c), (d, e, f, g))


def house(a, b, c, d):  # отрисовка дома
    pygame.draw.rect(screen, (70, 0, 0), (a, b, c, d), 0)  # корпус дома
    pygame.draw.rect(screen, (0, 0, 50), ((a + c / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # левое нижнее окно
    pygame.draw.rect(screen, (0, 0, 50), ((a + (5 * c) / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # среднее нижнее окно
    pygame.draw.rect(screen, (250, 240, 0), ((a + (9 * c) / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # правое нижнее окно
    pygame.draw.line(screen, (70, 0, 0), ((a + c / 13), (b + 3 * d / 7 + d / 6)),
                     ((a + 12 * c / 13), (b + 3 * d / 7 + d / 6)), 3)  # горизонтальный импост для нижних окон
    for i in range(3):  # вертикальные импосты
        pygame.draw.line(screen, (70, 0, 0), ((a + (5 + 8 * i) * c / 26), (b + 3 * d / 7)),
                         ((a + (5 + 8 * i) * c / 26), (b + d / 3 + 3 * d / 7)), 3)  #

    pygame.draw.rect(screen, (250, 240, 0), ((a + c / 5), (b + d / 20), (3 * c / 5), (5 * d / 30)), 0)  # верхнее окно
    pygame.draw.rect(screen, (0, 0, 0), ((a + c / 10), (b + d / 10), (4 * c / 5), (d / 6)), 3)  # кортур балкончика
    for i in range(10):  # перекладины балкончика
        pygame.draw.line(screen, (0, 0, 0), ((a + c / 10 + i * (4 * c / 5) / 10), (b + d / 10)),
                         ((a + c / 10 + i * (4 * c / 5) / 10), (d / 6 + b + d / 10)), 3)
    pygame.draw.polygon(screen, (40, 0, 0),
                        [[a - c / 10, b], [c + a + c / 10, b], [c + a - c / 10, b - d / 10],
                         [a + c / 10, b - d / 10]])  # крыша
    pygame.draw.rect(screen, (40, 0, 0), ((a + c / 5), (b - d / 5), (c / 10), (d / 10)), 0)  # труба 1
    pygame.draw.rect(screen, (40, 0, 0), ((a + 2 * c / 5), (b - d / 5), (c / 10), (d / 10)), 0)  # труба 2


pygame.draw.rect(screen, (130, 130, 130), (0, 0, 400, 250), 0)  # небо
pygame.draw.circle(screen, (255, 255, 255), (350, 50), 35, 0)  # луна
cloud(50, 50, 50, 100, 50, 300, 60)
cloud(40, 40, 40, 50, 100, 250, 50)
cloud(80, 80, 80, 150, 20, 150, 50)
cloud(70, 70, 70, 150, 150, 250, 50)
house(50, 200, 200, 300)
ghost(200, 300, 100, 200, 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
