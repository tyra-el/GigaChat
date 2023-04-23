import pygame as pg


class Button:
    '''Класс для создания кнопки'''

    def __init__(self, screen, x, clr, char):
        '''Инициализирует атрибуты кнопки'''

        # Назначение размеров и свойств кнопки
        self.width, self.height = x, 60
        self.char, self.screen, self.b_color = char, screen, clr

        # Построение объектов rect кнопки
        self.rect = pg.Rect(0, 0, self.width, self.height)

        # Вставка текста внутрь кнопки
        self.char_color = (70, 70, 70)
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
        
        self.se = gc_game.se

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.k_w, self.se.k_h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 300

        # Определение цветов
        self.color = self.se.gray
        self.color1 = self.se.white

        # Создание нестандартных клавиш

        # Backspace
        self.bs = Button(self.screen, 80, self.color1, '<--')
        self.bs.rect.right = self.rect.right - 10
        self.bs.rect.top = self.rect.top + 10
        self.bs.char_rect.center = self.bs.rect.center

        # Tab
        self.tab = Button(self.screen, 80, self.color1, 'Tab')
        self.tab.rect.left = self.rect.left + 10
        self.tab.rect.top = self.bs.rect.bottom + 5
        self.tab.char_rect.center = self.tab.rect.center

        # CapsLock
        self.cl = Button(self.screen, 100, self.color1, 'CpsL')
        self.cl.rect.left = self.rect.left + 10
        self.cl.rect.top = self.tab.rect.bottom + 5
        self.cl.char_rect.center = self.cl.rect.center

        # Enter
        self.enter = Button(self.screen, 105, self.color1, 'Entr')
        self.enter.rect.right = self.rect.right - 10
        self.enter.rect.top = self.tab.rect.bottom + 5
        self.enter.char_rect.center = self.enter.rect.center

        # LShift
        self.lshift = Button(self.screen, 120, self.color1, 'Shift')
        self.lshift.rect.left = self.rect.left + 10
        self.lshift.rect.top = self.cl.rect.bottom + 5
        self.lshift.char_rect.center = self.lshift.rect.center

        # RShift
        self.rshift = Button(self.screen, 150, self.color1, 'Shift')
        self.rshift.rect.right = self.rect.right - 10
        self.rshift.rect.top = self.cl.rect.bottom + 5
        self.rshift.char_rect.center = self.rshift.rect.center

        # Space
        self.space = Button(self.screen, 390, self.color1, '')
        self.space.rect.left = self.rect.left + 230
        self.space.rect.top = self.lshift.rect.bottom + 5
        self.space.char_rect.center = self.space.rect.center


        self.keys = {
            pg.K_BACKQUOTE:['`', '~', self.se.lgreen, self.se.dgreen, self.rect.left + 10, self.rect.top + 10],
            pg.K_1:['1', '!', self.se.lgreen, self.se.dgreen, self.rect.left + 75, self.rect.top + 10],
            pg.K_2:['2', '@', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 65, self.rect.top + 10],
            pg.K_3:['3', '#', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 130, self.rect.top + 10],
            pg.K_4:['4', '$', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 195, self.rect.top + 10],
            pg.K_5:['5', '%', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 260, self.rect.top + 10],
            pg.K_6:['6', '^', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 325, self.rect.top + 10],
            pg.K_7:['7', '&', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 390, self.rect.top + 10],
            pg.K_8:['8', '*', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 455, self.rect.top + 10],
            pg.K_9:['9', '(', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 520, self.rect.top + 10],
            pg.K_0:['0', ')', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 585, self.rect.top + 10],
            pg.K_MINUS:['-', '_', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 650, self.rect.top + 10],
            pg.K_EQUALS:['=', '+', self.se.lgreen, self.se.dgreen, self.rect.left + 75 + 715, self.rect.top + 10],
            pg.K_q:['q', 'Q', self.se.lgreen, self.se.dgreen, self.rect.left + 95, self.rect.top + 75],
            pg.K_w:['w', 'W', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 65, self.rect.top + 75],
            pg.K_e:['e', 'E', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 130, self.rect.top + 75],
            pg.K_r:['r', 'R', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 195, self.rect.top + 75],
            pg.K_t:['t', 'T', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 260, self.rect.top + 75],
            pg.K_y:['y', 'Y', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 325, self.rect.top + 75],
            pg.K_u:['u', 'U', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 390, self.rect.top + 75],
            pg.K_i:['i', 'I', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 455, self.rect.top + 75],
            pg.K_o:['o', 'O', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 520, self.rect.top + 75],
            pg.K_p:['p', 'P', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 585, self.rect.top + 75],
            pg.K_LEFTBRACKET:['[', '{', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 650, self.rect.top + 75],
            pg.K_RIGHTBRACKET:[']', '}', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 715, self.rect.top + 75],
            pg.K_BACKSLASH:['\\', '|', self.se.lgreen, self.se.dgreen, self.rect.left + 95 + 780, self.rect.top + 75],
            pg.K_a:['a', 'A', self.se.lgreen, self.se.dgreen, self.rect.left + 115, self.rect.top + 140],
            pg.K_s:['s', 'S', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 65, self.rect.top + 140],
            pg.K_d:['d', 'D', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 130, self.rect.top + 140],
            pg.K_f:['f', 'F', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 195, self.rect.top + 140],
            pg.K_g:['g', 'G', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 260, self.rect.top + 140],
            pg.K_h:['h', 'H', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 325, self.rect.top + 140],
            pg.K_j:['j', 'J', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 390, self.rect.top + 140],
            pg.K_k:['k', 'K', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 455, self.rect.top + 140],
            pg.K_l:['l', 'L', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 520, self.rect.top + 140],
            pg.K_SEMICOLON:[';', ':', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 585, self.rect.top + 140],
            pg.K_QUOTE:["'", '"', self.se.lgreen, self.se.dgreen, self.rect.left + 115 + 650, self.rect.top + 140],
            pg.K_z:['z', 'Z', self.se.lgreen, self.se.dgreen, self.rect.left + 135, self.rect.top + 205],
            pg.K_x:['x', 'X', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 65, self.rect.top + 205],
            pg.K_c:['c', 'C', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 130, self.rect.top + 205],
            pg.K_v:['v', 'V', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 195, self.rect.top + 205],
            pg.K_b:['b', 'B', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 260, self.rect.top + 205],
            pg.K_n:['n', 'N', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 325, self.rect.top + 205],
            pg.K_m:['m', 'M', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 390, self.rect.top + 205],
            pg.K_COMMA:[',', '<', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 455, self.rect.top + 205],
            pg.K_PERIOD:['.', '>', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 520, self.rect.top + 205],
            pg.K_SLASH:['/', '?', self.se.lgreen, self.se.dgreen, self.rect.left + 135 + 585, self.rect.top + 205],
        }
        



    def draw(self):
        # Blit the rect
        pg.draw.rect(self.screen, self.color, self.rect, border_radius=20)
        
        self.tab.draw()
        self.cl.draw()
        self.enter.draw()
        self.lshift.draw()
        self.rshift.draw()
        self.space.draw()
        self.bs.draw()

        for button in self.keys.values():
            self.button = Button(self.screen, 60, button[2], button[0])
            self.button.rect.left = button[4]
            self.button.rect.top = button[5]
            self.button.char_rect.center = self.button.rect.center

            self.button.draw()