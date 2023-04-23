import pygame as pg
import os


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
        self.filenames = os.listdir('text_files')


    def read_txt(self):
        for file, value in self.se.files_dict.items():
            if value[0]:
                with open(f'text_files/{file}') as self.file:
                    self.text = self.file.read()
        
        self.txt_surface = self.se.FONT.render(self.text, True, self.color)

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+9))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)

    
class TaskBar:
    '''Класс окна заданий'''

    def __init__(self, screen, se):

        self.se = se

        # Задаём размеры экрана
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, 400, 610)
        self.rect.right = self.screen_rect.right - 10
        self.rect.top = self.screen_rect.top + 80

        self.active = False

        # Определение цветов и шрифта
        self.color = self.se.white
        self.color1 = self.se.gray


        self.text = os.listdir('text_files')

        self.x = 0


    def draw(self):
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, border_radius=10)
        pg.draw.rect(self.screen, self.color1, self.rect, 5, border_radius=10)

        for file, value in self.se.files_dict.items():
            self.txt_surface = self.se.FONT0.render(file, True, value[1])
            self.txt_rect = self.txt_surface.get_rect()
            self.txt_rect.left = self.rect.left + 15
            self.txt_rect.top = self.rect.top + 10 + self.x
            self.x += 30
            # Blit the text.
            self.screen.blit(self.txt_surface, self.txt_rect)
        self.x = 0
    

    def task_event(self, event):
        '''Выбирает один из нескольких файлов нажатием мыши'''

        for file, value in self.se.files_dict.items():
            self.txt_surface = self.se.FONT0.render(file, True, value[1])
            self.txt_rect = self.txt_surface.get_rect()
            self.txt_rect.left = self.rect.left + 15
            self.txt_rect.top = self.rect.top + 10 + self.x
            self.x += 30

            if event.type == pg.MOUSEBUTTONDOWN:
                # Если пользователь кликнет на файл, активируется флаг
                if self.txt_rect.collidepoint(event.pos):
                    self.active = not self.active
                    value[0] = not value[0]
                    value[1], value[2] = value[2], value[1]
                    self.se.task_act = not self.se.task_act
                # else:
                #     self.active = False
                #     value[0] = False
                #     value[1], value[2] = value[2], value[1]
        self.x = 0

        print(self.se.files_dict)



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

        self.task_bar = TaskBar(self.screen, self.se)


    def menu_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Если пользователь кликнет на menu, активируется флаг
            if self.rect.collidepoint(event.pos):
                self.active = not self.active

            # Изменение цвета выбранной рамки
        if self.active:
            self.color = self.se.dgreen
            self.task_bar.task_event(event)
        else:
            self.color = self.se.lgreen


        self.txt_surface = self.se.FONT2.render(self.txt, True, self.color)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, self.char_rect)
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)

        if self.active:
            self.task_bar.draw()