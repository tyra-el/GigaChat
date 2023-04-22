import pygame as pg


class Button:
    '''Класс для создания кнопки'''

    def __init__(self, gc_game, width, height, char):
        '''Инициализирует атрибуты кнопки'''

        self.settings = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопки
        self.width, self.height, self.char = width, height, char
        self.button_color = self.settings.button_color_1

        # Построение объектов rect кнопки и выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Вставка текста внутрь кнопки
        self.char_color = (50, 50, 50)
        self.font = self.settings.FONT
        self.char = self.font.render(char, True, self.char_color)
        self.char_rect = self.char.get_rect()
        self.char_rect.center = self.rect.center

    def draw(self):
        # Отображение кнопки
        # self.screen.fill(self.button_color, self.rect)
        pg.draw.rect(self.screen, self.button_color, self.rect, border_radius=10)
        self.screen.blit(self.char, self.char_rect)



class Keyboard:
    '''Класс с боксом для клавиатуры'''

    def __init__(self, gc_game, text=''):
        
        self.se = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.k_w, self.se.k_h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 50 + 51 + 100 + 50 + 51

        # Определение цветов и шрифта
        self.color = self.se.button_color_2
        self.txt_surface = self.se.FONT.render(text, True, self.color)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+9))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 4, border_radius=10)