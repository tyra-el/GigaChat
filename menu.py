import pygame as pg


class TaskBox:
    '''Класс с заданием для переписывания'''

    def __init__(self, gc_game, text=''):
        
        self.se = gc_game.se

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.w, self.se.h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 100

        # Определение цветов и шрифта
        self.color = self.se.lgreen
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
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)

    
class TaskBar:
    '''Класс окна заданий'''

    pass


class Menu:
    '''Значёк меню'''

    def __init__(self, gc_game):

        self.se = gc_game.se

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.h1, self.se.h1)
        self.rect.right = self.screen_rect.right - 10
        self.rect.top = self.screen_rect.top + 10

        # Переменная со строкой текста
        self.txt = '≡'

        # Определение цветов и шрифта
        self.color = self.se.lgreen
        self.txt_surface = self.se.FONT2.render(self.txt, True, self.color)
        self.char_rect = self.txt_surface.get_rect()
        self.char_rect.center = self.rect.center

        self.active = False


    def menu_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Если пользователь кликнет на menu, активируется флаг
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

            # Изменение цвета выбранной рамки
        if self.active:
            self.color = self.se.dgreen
        else:
            self.color = self.se.lgreen

        self.txt_surface = self.se.FONT2.render(self.txt, True, self.color)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, self.char_rect)
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)
