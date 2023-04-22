import pygame as pg


class Score:
    '''Класс окна сёта'''

    def __init__(self, gc_game):

        self.se = gc_game.se

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.w1, self.se.h1)
        self.rect.left = self.screen_rect.left + 10
        self.rect.top = self.screen_rect.top + 10

        # Переменная со строкой текста
        self.txt = 'Score: '
        self.score = 0
        self.text = self.txt + str(self.score)

        # Определение цветов и шрифта
        self.color = self.se.lgreen
        self.txt_surface = self.se.FONT.render(self.text, True, self.color)


    def counting(self, task, input):
        if task == input:
            self.score += len(task)
            self.text = self.txt + str(self.score)
            self.txt_surface = self.se.font2.render(self.text, True, self.color)
        else:
            self.score -= len(task)
            self.text = self.txt + str(self.score)
            self.txt_surface = self.se.FONT.render(self.text, True, self.color)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+9))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 3, border_radius=10)

    def update(self):
        # Увеличение ширины бокса, если ширина текста его превысит
        if self.rect.right < self.screen_rect.right - 50:
            width = max(200, self.txt_surface.get_width()+17)
            self.rect.w = width
