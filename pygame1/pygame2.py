import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


circle(screen, (255, 255, 0), (200, 175), 100, 0)
circle(screen, (255, 0, 0), (150, 150), 20, 0)
circle(screen, (255, 0, 0), (250, 150), 15, 0)
circle(screen, (255, 255, 255), (150, 150), 15, 0)
circle(screen, (255, 255, 255), (250, 150), 10, 0)
pygame.draw.rect(screen, (0, 0, 0), (150, 220, 100, 10))
pygame.draw.line(screen, (0, 0, 0), [50, 50], [175, 150], 20)
pygame.draw.line(screen, (0, 0, 0), [350, 15], [225, 160], 20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()