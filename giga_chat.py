import sys
import pygame as pg


from keyboard import Keyboard
from settings import Settings
from input import InputBox
from menu import TaskBox
from menu import Menu
from score import Score


class GigaChat:
    '''Класс для управления ресурсами и поведением игры'''

    def __init__(self):
        '''Инициализирует и создаёт игровые ресурсы'''

        pg.init()
        self.clock = pg.time.Clock()

        # Создание экземпляра класса настроек
        self.se = Settings()
        
        # Задаём размеры экрана
        if self.se.fullscreen is False:
            self.screen = pg.display.set_mode(
                (self.se.screen_width, self.se.screen_height))
        else:
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.se.screen_width = self.screen.get_rect().width
            self.se.screen_height = self.screen.get_rect().height

        # Текст в названии приложения
        pg.display.set_caption("GigaChat")

        # Создание экземпляров классов
        self.score = Score(self)
        self.menu = Menu(self)

        self.task = TaskBox(self)
        self.input = InputBox(self)

        self.kb = Keyboard(self)



    def run_game(self):
        '''Запуск основного цикла игры'''

        while True:

            self._check_events()

            self._update_screen()


    def _check_events(self):
        '''Обрабатывает нажатия клавиш и события мыши'''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
                print(self.input.text)

            self.score.score_event(event)
            self.menu.menu_event(event)
            if (self.menu.active or self.score.active) == False:
                self.input.handle_event(event)


    def _check_keydown_events(self, event):
        for button, value in self.kb.keys.items():
            if event.key == button:
                value[2], value[3] = value[3], value[2]
            if event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                value[0], value[1] = value[1], value[0]


    def _check_keyup_events(self, event):
        for button, value in self.kb.keys.items():
            if event.key == button:
                value[2], value[3] = value[3], value[2]
            if event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                value[0], value[1] = value[1], value[0]
        if event.key == pg.K_LSHIFT:
            self.kb.color1 = self.se.white



    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''

        self.screen.fill(self.se.bg_color)

        # Отображение клавиатуры и клавиш
        self.kb.draw()

        # Отображение рамки и входного текста
        self.input.draw()

        # Отображение рамки и заданного текста
        self.task.draw()

        if self.se.task_act:
            self.task.read_txt()

        # Отображение счёта аналитики
        self.score.draw()
        self.score.update()

        # Отображение меню и выбор заданий
        self.menu.draw()


        pg.display.flip()
        self.clock.tick(30)





if __name__ == '__main__':
    # Создание экземпляра игры
    ai =GigaChat()
    ai.run_game()


