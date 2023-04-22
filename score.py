import pygame as pg


class Score:
    '''Класс окна сёта'''

    def __init__(self, gc_game):

        self.se = gc_game.settings

        # Задаём размеры экрана
        self.screen = gc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Построение объектов rect бокса, выравнивание по центру экрана
        self.rect = pg.Rect(0, 0, self.se.w1, self.se.h1)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top + 15

        # Переменная со строкой текста
        self.txt = 'Score: '
        self.score = 0
        self.text = self.txt + str(self.score)

        # Определение цветов и шрифта
        self.color = self.se.COLOR_ACTIVE
        self.txt_surface = self.se.font2.render(self.text, True, self.color)


    def counting(self, task, input):
        if task == input:
            self.score += len(task)
            self.text = self.txt + str(self.score)
            self.txt_surface = self.se.font2.render(self.text, True, self.color)
        else:
            self.score -= len(task)
            self.text = self.txt + str(self.score)
            self.txt_surface = self.se.font2.render(self.text, True, self.color)


    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+6))
        # Blit the rect.
        pg.draw.rect(self.screen, self.color, self.rect, 4)
