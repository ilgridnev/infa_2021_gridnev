import math
import pygame.font
from random import choice
from random import randint

FPS = 30

pygame.init()
pygame.font.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREY = (70, 70, 70)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

font = pygame.font.SysFont('gothic', 30)


def distance(coord1, coord2):
    """
    Находит расстояние между двумя точками.
    coord1 координаты первой точки.
    coord2 координаты второй точки.
    возвращает расстояние между точками
    """
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5


class Ball:
    """
    Класс мячей, вылетающих из пушки.
    """

    def __init__(self, screen: pygame.Surface, x, y):
        """
        Конструктор класса Ball.
        screen экран
        x - начальная x-координата мяча, вылетающего из пушки.
        y - начальная y-координата мяча, вылетающего из пушки.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30  # Параметр отвечает за время жизни мяча после остановки (30 кадров = 1 с)

    def ball_repulse(self):
        """
        Отражает мячи от стенок с уменьшением скорости
        """
        if self.x <= self.r or self.x >= 800 - self.r:
            self.vx = -0.65 * self.vx
        if self.x <= self.r:
            self.x = self.r
        elif self.x >= 800 - self.r:
            self.x = 800 - self.r
        if self.y >= 520 - self.r:
            self.vy = -0.65 * self.vy
            self.vx = 0.65 * self.vx
            self.y = 520 - self.r

        if self.vx ** 2 < 1:
            self.vx = 0

        if self.vy ** 2 < 1:
            self.vy = 0

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. (в соответствии с скоростями мяча по х и по у)
        """
        self.vy += 1.5
        self.x += self.vx
        self.y += self.vy
        self.ball_repulse()
        if self.vx == self.vy == 0:
            self.live -= 1

    def draw(self):
        """
        Метод вырисовывает объект этого класса на экране.
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            1
        )

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли мяч с целью (здесь называем obj).

        возвращает True, если произошло поражение цели (иначе - False).
        """
        if distance((self.x, self.y), (obj.x, obj.y)) <= self.r + obj.r:
            return True
        else:
            return False


class Gun:
    """
    Класс пушки.
    """

    def __init__(self, screen):
        """
        Конструктор класса Ball.
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 0
        self.color = GREY

    def fire2_start(self):
        """
        Начало "вытягивания" пушки.
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Начальные значения компонент скорости мяча vx и vy определяются координатами курсора
        event - событие отпускания кнопки мыши.
        """
        new_ball = Ball(self.screen, (11 + 8 / 9 * self.f2_power) * math.cos(self.angle) + 20,
                        (11 + 8 / 9 * self.f2_power) * math.sin(self.angle) + 450)
        self.angle = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = (8 / 10 * self.f2_power) * math.cos(self.angle) * 0.7
        new_ball.vy = (8 / 10 * self.f2_power) * math.sin(self.angle) * 0.7
        self.f2_on = 0
        self.f2_power = 10
        return new_ball

    def targetting(self, event):
        """
        Движение ствола пушки за курсором
        event - событие движения мыши.
        """
        if event:
            self.angle = math.atan2((event.pos[1] - 450), (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        Метод вырисовывает объект этого класса на экране.
        """
        coords = ((3 * math.sin(self.angle) + 20, -3 * math.cos(self.angle) + 450),
                  ((11 + 8 / 9 * self.f2_power) * math.cos(self.angle) + 3 * math.sin(self.angle) + 20,
                   (11 + 8 / 9 * self.f2_power) * math.sin(self.angle) - 3 * math.cos(self.angle) + 450),
                  ((11 + 8 / 9 * self.f2_power) * math.cos(self.angle) - 3 * math.sin(self.angle) + 20,
                   (11 + 8 / 9 * self.f2_power) * math.sin(self.angle) + 3 * math.cos(self.angle) + 450),
                  (-3 * math.sin(self.angle) + 20, 3 * math.cos(self.angle) + 450))
        pygame.draw.polygon(
            self.screen,
            self.color,
            coords
        )
        pygame.draw.aalines(
            self.screen,
            self.color,
            True,
            coords
        )

    def power_up(self):
        """
        Процесс заряжания пушки.
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = BLACK
        else:
            self.color = GREY


class Target:
    """
    Класс мишеней.
    """

    def __init__(self, screen: pygame.Surface):
        """
        Конструктор класса Target.
        """
        self.screen = screen
        self.points = 0
        self.x = randint(400, 780)
        self.y = randint(200, 520)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.r = randint(5, 35)
        self.color = choice([RED, BLUE, YELLOW])

    def target_repulse(self):
        """
        Отражает мишени от границ на экране
        """
        if self.x <= 300 or self.x >= 800 - self.r:
            self.vx = -self.vx
        if self.x <= 300:
            self.x = 300
        elif self.x >= 800 - self.r:
            self.x = 800 - self.r

        if self.y <= self.r or self.y >= 520:
            self.vy = -self.vy
        if self.y <= self.r:
            self.y = self.r
        elif self.y >= 520:
            self.y = 520

    def move(self):
        """
        Переместить мишень по прошествии единицы времени.
        """
        self.x += self.vx
        self.y += self.vy
        self.target_repulse()

    def hit(self, points=1):
        """
        Попадание шарика в мишень.
        """
        self.points += points

    def draw(self):
        """
        Метод вырисовывает объект этого класса на экране.
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Game:
    """
    Класс игры.
    """

    def __init__(self):
        """
        Конструктор класса Game.
        """
        self.points = 0
        self.finish = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bullet = 0
        self.balls = []
        self.targets = []
        self.gun = Gun(self.screen)

    def main(self):
        """
        Основной метод программы.
        Состоит из двух циклов:
        1) процесса игры с возможностью выстрелов, попаданий и т.п.
        2) выведения результата на экран и приостановки активной части игры

        """
        for _ in range(3 - len(self.targets)):
            self.targets.append(Target(self.screen))

        main_finished = False

        while not main_finished and not self.finish:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.balls.append(self.gun.fire2_end(event))
                    self.bullet += 1
                elif event.type == pygame.MOUSEMOTION:
                    self.gun.targetting(event)

            for t in self.targets:
                t.move()
            for b in self.balls:
                b.move()
                for t in self.targets[:]:
                    if b.hittest(t):
                        t.points = self.points
                        t.hit()
                        self.points = t.points
                        self.targets.remove(t)
                        main_finished = True

            self.gun.power_up()

            self.screen.fill(WHITE)
            self.gun.draw()
            for t in self.targets:
                if t != 0:
                    t.draw()
            for b in self.balls[:]:
                if b.live > 0:
                    b.draw()
                else:
                    self.balls.remove(b)

            surf = font.render("Score:" + str(self.points), True, BLACK)
            self.screen.blit(surf, (0, 0))
            pygame.display.update()

        i = 0
        while not self.finish and i < 70:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.gun.f2_on = 0
                    self.gun.f2_power = 10
                elif event.type == pygame.MOUSEMOTION:
                    self.gun.targetting(event)

            for t in self.targets:
                t.move()
            for b in self.balls:
                b.move()

            self.gun.power_up()

            self.screen.fill(WHITE)
            self.gun.draw()
            for t in self.targets:
                if t != 0:
                    t.draw()
            for b in self.balls[:]:
                if b.live > 0:
                    b.draw()
                else:
                    self.balls.remove(b)

            surf = font.render("Score:" + str(self.points), True, BLACK)
            self.screen.blit(surf, (0, 0))
            surf = font.render('Вы уничтожили цель за ' + str(self.bullet) + ' выстрелов', True, BLACK)
            self.screen.blit(surf, (115, 280))
            pygame.display.update()

            i += 1


clock = pygame.time.Clock()
game = Game()
score = 0
while not game.finish:
    game.balls = []
    game.bullet = 0
    game.main()

pygame.quit()
