import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def cloud(a, b, c, d, e, f, g, ):
    pygame.draw.ellipse(screen, (a, b, c), (d, e, f, g))


def house(a, b, c, d):
    pygame.draw.rect(screen, (70, 0, 0), (a, b, c, d), 0)
    pygame.draw.rect(screen, (0, 0, 50), ((a + c / 13), (b + d / 3), ((3 * c) / 13), (d / 3)), 0)
    pygame.draw.rect(screen, (0, 0, 50), ((a + (5 * c) / 13), (b + d / 3), ((3 * c) / 13), (d / 3)), 0)
    pygame.draw.rect(screen, (250, 240, 0), ((a + (9 * c) / 13), (b + d / 3), ((3 * c) / 13), (d / 3)), 0)
    pygame.draw.rect(screen, (250, 240, 0), ((a + c / 5), (b + d / 20), (3 * c / 5), (5 * d / 30)), 0)
    pygame.draw.rect(screen, (0, 0, 0), ((a + c / 10), (b + d / 10), (4 * c / 5), (d / 6)), 3)
    for i in range(10):
        pygame.draw.line(screen, (0, 0, 0), ((a + c / 10 + i * (4 * c / 5) / 10), (b + d / 10)),
                         ((a + c / 10 + i * (4 * c / 5) / 10), (d / 6 + b + d / 10)), 3)
    pygame.draw.polygon(screen, (40, 0, 0),
                        [[a - c / 10, b], [c + a + c / 10, b], [c + a - c / 10, b - d / 10], [a + c / 10, b - d / 10]])
    pygame.draw.rect(screen, (40, 0, 0), ((a + c / 5), (b - d / 5), (c / 10), (d / 10)), 0)
    pygame.draw.rect(screen, (40, 0, 0), ((a + 2*c / 5), (b - d / 5), (c / 10), (d / 10)), 0)


pygame.draw.rect(screen, (130, 130, 130), (0, 0, 400, 250), 0)
pygame.draw.circle(screen, (255, 255, 255), (350, 50), 35, 0)
cloud(50, 50, 50, 100, 50, 300, 60)
cloud(40, 40, 40, 50, 100, 250, 50)
cloud(80, 80, 80, 150, 20, 150, 50)
cloud(70, 70, 70, 150, 150, 250, 50)
house(50, 200, 200, 300)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
