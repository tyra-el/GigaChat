import pygame as pg

class Settings:
    '''Класс для хранения настроек игры'''

    def __init__(self):
        '''Инициализирует статичечкие настройки игры'''
        # Параметры экрана
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (70, 70, 70)

        # Цвет клавиш и клавиатуры
        self.white = (230, 255, 230)
        self.lgreen = (190, 255, 190)
        self.dgreen = (110, 210, 110)
        self.red = (210, 170, 170)

        self.k_w = 945
        self.k_h = 340

        # Настройки окна ввода текста, заданий
        self.COLOR_INACTIVE = (200, 240, 200)
        self.COLOR_ACTIVE = (110, 210, 110)
        self.FONT = pg.font.SysFont('isocpeur', 48)

        self.w = self.screen_width - 100
        self.h = 51

        # Настройки счёта
        self.w1 = 200
        self.h1 = 35
        self.font2 = pg.font.SysFont('isocpeur', 34)
