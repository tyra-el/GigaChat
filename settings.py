import pygame as pg
import os

class Settings:
    '''Класс для хранения настроек игры'''

    def __init__(self):
        '''Инициализирует статичечкие настройки игры'''
        # Параметры экрана
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (70, 70, 70)

        # Цвета клавиш
        self.white = (230, 255, 230)
        self.lgreen = (190, 255, 190)
        self.dgreen = (110, 210, 110)
        self.red = (210, 170, 170)
        self.gray = (105, 105, 105)
        self.lgray = (150, 150, 150)
        self.dgray = (130, 150, 130)

        # Клавиатура
        self.k_w = 945
        self.k_h = 340

        # Настройки окон ввода текста, заданий
        self.w = self.screen_width - 100
        self.h = 51

        self.task_act = False

        # Создание словаря со списком файлов из папки
        self.files_list = os.listdir('text_files')
        self.files_dict = {}
        for filename in self.files_list:
            self.files_dict[filename] = [False, self.gray, self.dgreen]


        # Настройки счёта
        self.w1 = 175
        self.h1 = 51

        # Шрифт
        self.FONT0 = pg.font.SysFont('isocpeur', 30)
        self.FONT = pg.font.SysFont('isocpeur', 48)
        self.FONT2 = pg.font.SysFont('isocpeur', 60)

