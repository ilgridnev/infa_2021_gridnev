# импортирование и переобозначение pygame
import pygame as pog

pog.init()

# инициализация экрана
FPS = 30
screen = pog.display.set_mode((550, 750))

# настройка цветов для быстрого вызова
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (55, 200, 113)
blue = (95, 188, 211)
red = (255, 0, 0)
brown = (200, 171, 55)
bulldog_color = (108, 103, 83)  # ВАЖНО! цвет отрисовываемых бульдогов (можно менять)


# функция отрисовки забора
def fence(
        fence_start_x,
        fence_start_y,
        fence_alfa
):
    '''
    Функция рисует забор на экране.
    sсreen - объект, соответсвующий отображаемому дисплею
    fence_start_x, fence_start_y, - координаты левого верхнего угла изображения
    fence_alfa - параметр пропорционального увеличения/уменьшения размера
    выбран стандартный для забора цвет standart, его можно изменить в следующей после документации строчке
    '''
    standart = (200, 171, 55)
    pog.draw.rect(
        screen,
        standart,
        (fence_start_x, fence_start_y,
         45 * fence_alfa, 30 * fence_alfa)
    )
    pog.draw.line(
        screen,
        black,
        (fence_start_x,
         fence_start_y + 30 * fence_alfa),
        (fence_start_x + 45 * fence_alfa,
         fence_start_y + 30 * fence_alfa)
    )
    h = 4 * fence_alfa
    x = fence_start_x + 4 * fence_alfa

    while x < fence_start_x + 45 * fence_alfa:
        pog.draw.line(
            screen,
            (0, 0, 0),
            (x, fence_start_y),
            (x, fence_start_y + 30 * fence_alfa)
        )
        x += h


def body(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient,
        bull
):
    '''
    Функция рисует тело бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 30 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         8 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - 16 * bull_size * bull_orient,
         bull_start_y + 4 * bull_size,
         16 * bull_size,
         6 * bull_size)
    )


def face(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient,
        bull
):
    '''
    Функция рисует лицо бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    pog.draw.ellipse(
        screen,
        white,
        (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 1.5 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 2 * bull_size - 5 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        white,
        (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 4.5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         2 * bull_size, bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 5 * bull_size - 11 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         bull_size, bull_size)
    )
    pog.draw.arc(
        screen,
        black,
        (bull_start_x + bull_size - 8 * bull_size * bull_orient,
         bull_start_y + 6 * bull_size,
         6 * bull_size, 4 * bull_size),
        0.4, 2.75
    )
    pog.draw.polygon(
        screen,
        white,
        [
            (bull_start_x + 2.3 * bull_size - 4.6 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ]
    )
    pog.draw.polygon(
        screen,
        white,
        [
            (bull_start_x + 5.7 * bull_size - 11.4 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ]
    )
    pog.draw.polygon(
        screen,
        black,
        [
            (bull_start_x + 2.3 * bull_size - 4.6 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 1.7 * bull_size - 3.4 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ],
        1
    )
    pog.draw.polygon(
        screen,
        black,
        [
            (bull_start_x + 5.7 * bull_size - 11.4 * bull_size * bull_orient,
             bull_start_y + 6.2 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 6.6 * bull_size),
            (bull_start_x + 6.3 * bull_size - 12.6 * bull_size * bull_orient,
             bull_start_y + 5.3 * bull_size)
        ],
        1
    )


def head(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient,
        bull
):
    '''
    Функция рисует голову бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    pog.draw.rect(
        screen,
        bull,
        (bull_start_x - 8 * bull_size * bull_orient,
         bull_start_y,
         8 * bull_size,
         8 * bull_size)
    )
    pog.draw.rect(
        screen,
        black,
        (bull_start_x - 8 * bull_size * bull_orient,
         bull_start_y,
         8 * bull_size, 8 * bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x - bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size),
        1
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 7 * bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        black,
        (bull_start_x + 7 * bull_size - 8 * bull_size * bull_orient,
         bull_start_y,
         2 * bull_size, 3 * bull_size),
        1
    )
    face(bull_start_x,
         bull_start_y,
         bull_size,
         bull_orient,
         bull)


def legs(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient,
        bull
):
    '''
    Функция рисует ноги бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - bull_size - 2 * bull_size * bull_orient,
         bull_start_y + 6 * bull_size,
         4 * bull_size,
         9 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 6 * bull_size - 15 * bull_size * bull_orient,
         bull_start_y + 8 * bull_size,
         4 * bull_size, 9 * bull_size)
    )

    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 26 * bull_size * bull_orient,
         bull_start_y + 3 * bull_size,
         4 * bull_size, 4 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 16 * bull_size - 36 * bull_size * bull_orient,
         bull_start_y + 5 * bull_size,
         4 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 18 * bull_size - 38 * bull_size * bull_orient,
         bull_start_y + 9 * bull_size,
         2 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 13 * bull_size - 28 * bull_size * bull_orient,
         bull_start_y + 7 * bull_size,
         2 * bull_size, 5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 16 * bull_size - 35 * bull_size * bull_orient,
         bull_start_y + 13 * bull_size,
         3 * bull_size, 1.5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 11 * bull_size - 25 * bull_size * bull_orient,
         bull_start_y + 11 * bull_size,
         3 * bull_size, 1.5 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x - 3 * bull_size + bull_size * bull_orient,
         bull_start_y + 14 * bull_size,
         5 * bull_size, 2 * bull_size)
    )
    pog.draw.ellipse(
        screen,
        bull,
        (bull_start_x + 4 * bull_size - 12 * bull_size * bull_orient,
         bull_start_y + 16 * bull_size,
         5 * bull_size, 2 * bull_size)
    )


def bulldog(
        bull_start_x,
        bull_start_y,
        bull_size,
        bull_orient,
        bull
):
    '''
    Функция рисует бульдога на экране.
    bull_start_x - х координата вернего дальнего угла головы, где "дальний" означает противоположный от тела
    bull_start_y - у координата верхней грани головы
    bull_size - параметр пропорционального увеличения размера
    bull_orient - переменная, принимающая значения 0 или 1, для того чтобы пес смотрел влево и вправо соответственно
    '''
    body(bull_start_x,
         bull_start_y,
         bull_size,
         bull_orient,
         bull)
    legs(bull_start_x,
         bull_start_y,
         bull_size,
         bull_orient,
         bull)
    head(bull_start_x,
         bull_start_y,
         bull_size,
         bull_orient,
         bull)


def chain(x, y, l, h):
    '''
    Функция рисует звено цепи будки в форме эллипса.
    x, y - координаты вернего левого угла описанного около цвена цепи четырехугольника
    х, у - горизонтальная и вертикальная координаты соответственно
    l - длина этого четырехугольника по х
    h - высота четырехугольника по у
    '''
    pog.draw.ellipse(
        screen,
        black,
        (x, y, l, h),
        1
    )


# отрисовка неба
pog.draw.rect(
    screen,
    blue,
    (0, 0, 600, 600)
)

# отрисовка газона
pog.draw.rect(
    screen,
    green,
    (0, 250, 550, 600)
)

# отрисовка заборов
fence(100, 10, 12)
fence(0, 200, 7)
fence(300, 300, 6)
fence(0, 320, 6)

bulldog(550, 450, 4, 1, bulldog_color)

# здесь начало отрисовки будки
# крыша (боковой скат)
pog.draw.polygon(
    screen,
    brown,
    [(460, 360), (420, 380),
     (470, 460), (510, 440)
     ]
)

# крыша (треугольный торец)
pog.draw.polygon(
    screen,
    brown,
    [(420, 380), (470, 460),
     (360, 440)
     ]
)

# стена (боковая)
pog.draw.polygon(
    screen,
    brown,
    [(470, 460), (510, 440),
     (510, 530), (470, 590)
     ]
)

# передняя стена (со стороны входа)
pog.draw.polygon(
    screen,
    brown,
    [(360, 440), (470, 460),
     (470, 590), (360, 550)
     ]
)

# контур боковой стены
pog.draw.polygon(
    screen,
    black,
    [(470, 460), (510, 440),
     (510, 530), (470, 590)
     ],
    2
)

# контур бокового ската крыши
pog.draw.polygon(
    screen,
    black,
    [(460, 360), (420, 380),
     (470, 460), (510, 440)
     ],
    1
)

# контур треугольного торца крыши
pog.draw.polygon(
    screen,
    black,
    [(420, 380), (470, 460),
     (360, 440)
     ],
    1
)

# контур передней стены
pog.draw.polygon(
    screen,
    black,
    [(360, 440), (470, 460),
     (470, 590), (360, 550)
     ],
    2
)

# вход в будку
pog.draw.ellipse(
    screen,
    black,
    (385, 475, 55, 70)
)

# рисуем звенья цепи будки
chain(375, 530, 20, 10)
chain(360, 545, 20, 15)
chain(370, 535, 15, 20)
chain(350, 555, 20, 10)
chain(350, 560, 10, 10)
chain(330, 565, 25, 10)
chain(315, 568, 20, 10)
chain(295, 570, 25, 5)
chain(290, 565, 10, 15)
chain(275, 575, 20, 5)
chain(265, 575, 20, 10)

# последовательный вызов функций отрисовки бульдогов
bulldog(50, 400, 10, 0, bulldog_color)
bulldog(300, 550, 8, 1, bulldog_color)
bulldog(330, 530, 25, 0, bulldog_color)

# формальное завершение программы для корректной работы
pog.display.update()
clock = pog.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pog.event.get():
        if event.type == pog.QUIT:
            finished = True

pog.quit()
