import pygame.font


class Output:
    '''Класс, отображающий экран выходного текста'''

    def __init__(self, gc_game):
        '''Инициализирует атрибуты экрана выходного текста'''

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств окна вывода текста
        self.width, self.height = 250, 50
        self.line_color = (110, 210, 110)

        # Построение объектов rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 100

    def draw_line(self):
        self.screen.fill(self.line_color, self.rect)


class Char:
    '''Класс, отображающий выходной текст'''

    def __init__(self, gc_game):
        '''Инициализирует атрибуты выходного текста'''

        self.output = gc_game.output

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Вставка текста внутрь строки
        self.char_color = (200, 240, 200)
        self.font = pygame.font.SysFont('isocpeur', 48)
        self.char = self.font.render('q', True, self.char_color)
        self.char_rect = self.char.get_rect()
        self.char_rect.center = self.output.rect.center

    def chat(self):
        if self.chat_act:
            self.screen.blit(self.char, self.char_rect)






