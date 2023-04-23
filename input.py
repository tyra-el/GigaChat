import pygame as pg


class InputBox:
    '''Класс окна ввода текста'''

    def __init__(self, gc_game, text=''):

        self.se = gc_game.se
        self.score = gc_game.score
        self.task = gc_game.task

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.w, self.se.h)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 190

        # Определение цветов и шрифта
        self.color = self.se.lgreen
        self.txt_surface = self.se.FONT.render(text, True, self.color)

        # Переменная со строкой текста
        self.text = text

        self.active = False
        self.dbl1 = False
        self.dbl2 = False

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
            self.color = self.se.dgreen
        else:
            self.color = self.se.lgreen

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.dbl1 = True
                elif event.key == pg.K_RETURN:
                    self.score.counting(self.task.text, self.text)
                elif event.key == pg.K_ESCAPE:
                    self.active = False
                else:
                    self.text += event.unicode
                if event.key == pg.K_RCTRL:
                    self.dbl2 = True

                if self.dbl1 and self.dbl2:
                    # print(self.text)
                    self.text = ''
                    self.dbl1, self.dbl2 = False, False


                # Re-render the text.
                self.txt_surface = self.se.FONT.render(self.text, True, self.color)


    # def update(self):
    #     # Увеличение ширины бокса, если ширина текста его превысит
    #     if self.rect.right < self.screen_rect.right - 50:
    #         width = max(200, self.txt_surface.get_width()+10)
    #         self.rect.w = width


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+9))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)


