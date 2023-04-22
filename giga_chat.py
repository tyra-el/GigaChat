import sys
import pygame as pg


from keyboard import Keyboard
from keyboard import Button
from settings import Settings
from input import InputBox
from task import TaskBox
from score import Score


class GigaChat:
    '''Класс для управления ресурсами и поведением игры'''

    def __init__(self):
        '''Инициализирует и создаёт игровые ресурсы'''

        pg.init()
        self.clock = pg.time.Clock()

        # Создание экземпляра класса настроек
        self.settings = Settings()
        
        # Задаём размеры экрана
        if self.settings.fullscreen is False:
            self.screen = pg.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # Текст в названии приложения
        pg.display.set_caption("GigaChat")

        # Создание экземпляров классов
        self.score = Score(self)
        self.task = TaskBox(self)
        self.input = InputBox(self)

        self.kb = Keyboard(self)
        

        self.task.read_txt()


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
                print(self.input.text)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            
            self.input.handle_event(event)


    def _check_keydown_events(self, event):
        for i in self.kb.keys.items():
            if event.key == pg.K_q:
                pass

    def _check_keyup_events(self, event):
        if event.key == pg.K_q:
            pass

    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''

        self.screen.fill(self.settings.bg_color)

        # Отображение клавиатуры и клавиш
        self.kb.draw()

        # Отображение рамки и входного текста
        self.input.draw()

        # Отображение рамки и заданного текста
        self.task.draw()

        # Отображение рамки и счёта
        self.score.draw()

        pg.display.flip()
        self.clock.tick(30)





if __name__ == '__main__':
    # Создание экземпляра игры
    ai =GigaChat()
    ai.run_game()


