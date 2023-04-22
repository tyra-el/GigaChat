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
        self.cl = Button(self.screen, 100, 'CpsL')
        self.cl.rect.left = self.rect.left + 10
        self.cl.rect.top = self.tab.rect.bottom + 5
        self.cl.char_rect.center = self.cl.rect.center

        # Enter
        self.enter = Button(self.screen, 105, 'Entr')
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
        self.space = Button(self.screen, 390, '')
        self.space.rect.left = self.rect.left + 230
        self.space.rect.top = self.lshift.rect.bottom + 5
        self.space.char_rect.center = self.space.rect.center


        self.keys = {
            'K_BACKQUOTE':['`', self.se.button_color_2, self.rect.left + 10, self.rect.top + 10],
            'K_1':['1', self.se.button_color_2, self.rect.left + 75, self.rect.top + 10],
            'K_2':['2', self.se.button_color_2, self.rect.left + 75 + 65, self.rect.top + 10],
            'K_3':['3', self.se.button_color_2, self.rect.left + 75 + 130, self.rect.top + 10],
            'K_4':['4', self.se.button_color_2, self.rect.left + 75 + 195, self.rect.top + 10],
            'K_5':['5', self.se.button_color_2, self.rect.left + 75 + 260, self.rect.top + 10],
            'K_6':['6', self.se.button_color_2, self.rect.left + 75 + 325, self.rect.top + 10],
            'K_7':['7', self.se.button_color_2, self.rect.left + 75 + 390, self.rect.top + 10],
            'K_8':['8', self.se.button_color_2, self.rect.left + 75 + 455, self.rect.top + 10],
            'K_9':['9', self.se.button_color_2, self.rect.left + 75 + 520, self.rect.top + 10],
            'K_0':['0', self.se.button_color_2, self.rect.left + 75 + 585, self.rect.top + 10],
            'K_MINUS':['-', self.se.button_color_2, self.rect.left + 75 + 650, self.rect.top + 10],
            'K_EQUALS':['=', self.se.button_color_2, self.rect.left + 75 + 715, self.rect.top + 10],
            'K_q':['Q', self.se.button_color_2, self.rect.left + 95, self.rect.top + 75],
            'K_w':['W', self.se.button_color_2, self.rect.left + 95 + 65, self.rect.top + 75],
            'K_e':['E', self.se.button_color_2, self.rect.left + 95 + 130, self.rect.top + 75],
            'K_r':['R', self.se.button_color_2, self.rect.left + 95 + 195, self.rect.top + 75],
            'K_t':['T', self.se.button_color_2, self.rect.left + 95 + 260, self.rect.top + 75],
            'K_y':['Y', self.se.button_color_2, self.rect.left + 95 + 325, self.rect.top + 75],
            'K_u':['U', self.se.button_color_2, self.rect.left + 95 + 390, self.rect.top + 75],
            'K_i':['I', self.se.button_color_2, self.rect.left + 95 + 455, self.rect.top + 75],
            'K_o':['O', self.se.button_color_2, self.rect.left + 95 + 520, self.rect.top + 75],
            'K_p':['P', self.se.button_color_2, self.rect.left + 95 + 585, self.rect.top + 75],
            'K_LEFTBRACKET':['[', self.se.button_color_2, self.rect.left + 95 + 650, self.rect.top + 75],
            'K_RIGHTBRACKET':[']', self.se.button_color_2, self.rect.left + 95 + 715, self.rect.top + 75],
            'K_BACKSLASH':['\\', self.se.button_color_2, self.rect.left + 95 + 780, self.rect.top + 75],
            'K_a':['A', self.se.button_color_2, self.rect.left + 115, self.rect.top + 140],
            'K_s':['S', self.se.button_color_2, self.rect.left + 115 + 65, self.rect.top + 140],
            'K_d':['D', self.se.button_color_2, self.rect.left + 115 + 130, self.rect.top + 140],
            'K_f':['F', self.se.button_color_2, self.rect.left + 115 + 195, self.rect.top + 140],
            'K_g':['G', self.se.button_color_2, self.rect.left + 115 + 260, self.rect.top + 140],
            'K_h':['H', self.se.button_color_2, self.rect.left + 115 + 325, self.rect.top + 140],
            'K_j':['J', self.se.button_color_2, self.rect.left + 115 + 390, self.rect.top + 140],
            'K_k':['K', self.se.button_color_2, self.rect.left + 115 + 455, self.rect.top + 140],
            'K_l':['L', self.se.button_color_2, self.rect.left + 115 + 520, self.rect.top + 140],
            'K_SEMICOLON':[';', self.se.button_color_2, self.rect.left + 115 + 585, self.rect.top + 140],
            'K_QUOTE':["'", self.se.button_color_2, self.rect.left + 115 + 650, self.rect.top + 140],
            'K_z':['Z', self.se.button_color_2, self.rect.left + 135, self.rect.top + 205],
            'K_x':['X', self.se.button_color_2, self.rect.left + 135 + 65, self.rect.top + 205],
            'K_c':['C', self.se.button_color_2, self.rect.left + 135 + 130, self.rect.top + 205],
            'K_v':['V', self.se.button_color_2, self.rect.left + 135 + 195, self.rect.top + 205],
            'K_b':['B', self.se.button_color_2, self.rect.left + 135 + 260, self.rect.top + 205],
            'K_n':['N', self.se.button_color_2, self.rect.left + 135 + 325, self.rect.top + 205],
            'K_m':['M', self.se.button_color_2, self.rect.left + 135 + 390, self.rect.top + 205],
            'K_COMMA':[',', self.se.button_color_2, self.rect.left + 135 + 455, self.rect.top + 205],
            'K_PERIOD':['.', self.se.button_color_2, self.rect.left + 135 + 520, self.rect.top + 205],
            'K_SLASH':['/', self.se.button_color_2, self.rect.left + 135 + 585, self.rect.top + 205],
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

        for key in self.keys.values():
            self.button = Button(self.screen, 60, key[0])
            self.button.rect.left = key[2]
            self.button.rect.top = key[3]
            self.button.char_rect.center = self.button.rect.center

            self.button.draw()