import pygame as pg


class TaskBox:
    '''Класс с заданием для переписывания'''

    def __init__(self, gc_game, x, y, w, h, text=''):
        
        self.settings = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(x, y, w, h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 50

        # Определение цветов и шрифта
        self.color = self.settings.COLOR_INACTIVE
        self.txt_surface = self.settings.FONT.render(text, True, self.color)

        # Переменная со строкой текста
        self.text = text

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 4)

    