import pygame as pg
from settings import Settings


class InputBox:
    '''Класс окна ввода текста'''

    def __init__(self, gc_game, x, y, w, h, text=''):

        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = Settings()

        self.rect = pg.Rect(x, y, w, h)
        self.color = self.settings.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.settings.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:

            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):

                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

            # Change the current color of the input box.
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

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

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






