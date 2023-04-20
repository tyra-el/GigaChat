import sys
import pygame as pg

from button import Button
from settings import Settings
from input import InputBox


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
        self.button = Button(self, 60, 60, 'q')
        self.input = InputBox(self, 0, 0, self.settings.screen_width - 100, 51)
        # self.outscreen = OutScreen(self)



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
        if event.key == pg.K_q:
            self.button.button_color = self.settings.button_color_2
            self.keydown_flag = True


    def _check_keyup_events(self, event):
        if event.key == pg.K_q:
            self.button.button_color = self.settings.button_color_1
            self.keydown_flag = False


    def _printing_chars(self):
        if self.keydown_flag == True:
            print('q')



    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''

        self.screen.fill(self.settings.bg_color)

        self.button.draw_button()

        # self.input.update()
        self.input.draw()

        pg.display.flip()
        self.clock.tick(30)





if __name__ == '__main__':
    # Создание экземпляра игры
    ai =GigaChat()
    ai.run_game()


