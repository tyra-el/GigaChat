import pygame as pg


class TaskBox:
    '''Класс с заданием для переписывания'''

    def __init__(self, gc_game, text=''):
        
        self.se = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.w, self.se.h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 100

        # Определение цветов и шрифта
        self.color = self.se.COLOR_INACTIVE
        self.txt_surface = self.se.FONT.render(text, True, self.color)

        # Переменная со строкой текста
        self.text = text
        self.file = ''


    def read_txt(self):
        with open('task.txt') as self.file:
            self.text = self.file.read()

        self.txt_surface = self.se.FONT.render(self.text, True, self.color)
        print(self.text)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+9))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 4, border_radius=10)

    

