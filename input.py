import pygame as pg


class InputBox:
    '''Класс окна ввода текста'''

    def __init__(self, gc_game, x, y, w, h, text=''):

        self.settings = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(x, y, w, h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 50 + 51 + 50

        # Определение цветов и шрифта
        self.color = self.settings.COLOR_INACTIVE
        self.txt_surface = self.settings.FONT.render(text, True, self.color)

        # Переменная со строкой текста
        self.text = text

        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:

            # Если пользователь кликнет на input_box rect
            if self.rect.collidepoint(event.pos):

                # Флаг активируется
                self.active = not self.active
            else:
                self.active = False

            # Изменение цвета выбранной рамки
            if self.active:
                self.color = self.settings.COLOR_ACTIVE
            else:
                self.color = self.settings.COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    # print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Re-render the text.
                self.txt_surface = self.settings.FONT.render(self.text, True, self.color)

    # def update(self):
    #     # Увеличение ширины бокса, если ширина текста его превысит
    #     if self.rect.right < self.screen_rect.right - 50:
    #         width = max(200, self.txt_surface.get_width()+10)
    #         self.rect.w = width

    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 4)


# class Char:
#     '''Класс, отображающий выходной текст'''

#     def __init__(self, gc_game):
#         '''Инициализирует атрибуты выходного текста'''

#         self.output = gc_game.output

#         # Задаём размеры экрана
#         self.screen = gc_game.screen
#         self.screen_rect = self.screen.get_rect()

#         # Вставка текста внутрь строки
#         self.char_color = (200, 240, 200)
#         self.font = pg.font.SysFont('isocpeur', 48)
#         self.char = self.font.render('q', True, self.char_color)
#         self.char_rect = self.char.get_rect()
#         self.char_rect.center = self.output.rect.center

#     def chat(self):
#         if self.chat_act:
#             self.screen.blit(self.char, self.char_rect)






