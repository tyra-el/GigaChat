import pygame as pg


class Button:
    '''Класс для создания кнопки'''

    def __init__(self, screen, char):
        '''Инициализирует атрибуты кнопки'''

        # Назначение размеров и свойств кнопки
        self.width, self.height, self.char, self.screen = 60, 60, char, screen
        self.b_color = (200, 255, 200)

        # Построение объектов rect кнопки
        self.rect = pg.Rect(0, 0, self.width, self.height)

        # Вставка текста внутрь кнопки
        self.char_color = (50, 50, 50)
        self.font = pg.font.SysFont('isocpeur', 48)
        self.char = self.font.render(char, True, self.char_color)
        self.char_rect = self.char.get_rect()
        self.char_rect.center = self.rect.center

    def draw(self):
        # Отображение кнопки
        pg.draw.rect(self.screen, self.b_color, self.rect, border_radius=10)
        self.screen.blit(self.char, self.char_rect)



class Keyboard:
    '''Класс с боксом для клавиатуры'''

    def __init__(self, gc_game):
        
        self.se = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.k_w, self.se.k_h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 50 + 51 + 100 + 50 + 51

        # Определение цветов
        self.color = self.se.button_color_2

        # Создание клавиш клавиатуры
        self.left = self.rect.left
        self.keys = '`1234567890-='



    def draw(self):
        # Blit the rect
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)
        
        
        for i in self.keys:
            self.button = Button(self.screen, i)
            self.button.draw()