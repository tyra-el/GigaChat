import pygame.font


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
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Вставка текста внутрь кнопки
        self.char_color = (50, 50, 50)
        self.font = pygame.font.SysFont('isocpeur', 48)
        self.char = self.font.render(char, True, self.char_color)
        self.char_rect = self.char.get_rect()
        self.char_rect.center = self.rect.center

    def draw_button(self):
        # Отображение кнопки
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.char, self.char_rect)
