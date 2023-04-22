import pygame as pg


class Button:
    '''Класс для создания кнопки'''

    def __init__(self, screen, x, char):
        '''Инициализирует атрибуты кнопки'''

        # Назначение размеров и свойств кнопки
        self.width, self.height, self.char, self.screen = x, 60, char, screen
        self.b_color = (200, 255, 200)

        # Построение объектов rect кнопки
        self.rect = pg.Rect(0, 0, self.width, self.height)

        # Вставка текста внутрь кнопки
        self.char_color = (50, 50, 50)
        self.font = pg.font.SysFont('isocpeur', 48)
        self.char = self.font.render(char, True, self.char_color)
        self.char_rect = self.char.get_rect()
        
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

        # Создание нестандартных клавиш

        # Backspace
        self.bs = Button(self.screen, 80, '<--')
        self.bs.rect.right = self.rect.right - 10
        self.bs.rect.top = self.rect.top + 10
        self.bs.char_rect.center = self.bs.rect.center

        # Tab
        self.tab = Button(self.screen, 80, 'Tab')
        self.tab.rect.left = self.rect.left + 10
        self.tab.rect.top = self.bs.rect.bottom + 5
        self.tab.char_rect.center = self.tab.rect.center

        # CapsLock
        self.cl = Button(self.screen, 100, 'CL')
        self.cl.rect.left = self.rect.left + 10
        self.cl.rect.top = self.tab.rect.bottom + 5
        self.cl.char_rect.center = self.cl.rect.center

        # Enter
        self.enter = Button(self.screen, 100, 'Entr')
        self.enter.rect.right = self.rect.right - 10
        self.enter.rect.top = self.tab.rect.bottom + 5
        self.enter.char_rect.center = self.enter.rect.center

        # LShift
        self.lshift = Button(self.screen, 120, 'Shift')
        self.lshift.rect.left = self.rect.left + 10
        self.lshift.rect.top = self.cl.rect.bottom + 5
        self.lshift.char_rect.center = self.lshift.rect.center

        # RShift
        self.rshift = Button(self.screen, 150, 'Shift')
        self.rshift.rect.right = self.rect.right - 10
        self.rshift.rect.top = self.cl.rect.bottom + 5
        self.rshift.char_rect.center = self.rshift.rect.center

        # Space
        self.space = Button(self.screen, 360, '')
        self.space.rect.left = self.rect.left + 200
        self.space.rect.top = self.lshift.rect.bottom + 5
        self.space.char_rect.center = self.space.rect.center


        self.keys = {
            'K_BACKQUOTE': ''
        }
        



    def draw(self):
        # Blit the rect
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)
        
        self.tab.draw()
        self.cl.draw()
        self.enter.draw()
        self.lshift.draw()
        self.rshift.draw()
        self.space.draw()
        self.bs.draw()

        # for i in self.keys:
        #     self.button = Button(self.screen, 60, i)
        #     self.button.rect.top = self.rect.top + 10
        #     self.button.rect.left = self.left
        #     self.button.char_rect.center = self.button.rect.center

        #     self.button.draw()