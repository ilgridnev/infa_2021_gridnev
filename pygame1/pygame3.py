import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def cloud(a, b, c, d, e, f, g, ):
    pygame.draw.ellipse(screen, (a, b, c), (d, e, f, g))


color = (130, 130, 130)
pygame.draw.rect(screen, color, (0, 0, 400, 250), 0)
pygame.draw.circle(screen, (255, 255, 255), (350, 50), 35, 0)
cloud(50, 50, 50, 100, 50, 300, 60)
cloud(40, 40, 40, 50, 100, 250, 50)
cloud(80, 80, 80, 150, 20, 150, 50)
cloud(70, 70, 70, 150, 150, 250, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
