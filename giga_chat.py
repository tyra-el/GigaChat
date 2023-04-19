import sys
import pygame

from button import Button
from settings import Settings
from output import Output
from output import Char



class GigaChat:
    '''Класс для управления ресурсами и поведением игры'''

    def __init__(self):
        '''Инициализирует и создаёт игровые ресурсы'''

        pygame.init()

        # Создание экземпляра класса настроек
        self.settings = Settings()
        
        # Задаём размеры экрана
        if self.settings.fullscreen is False:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # Текст в названии приложения
        pygame.display.set_caption("GigaChat")

        # Создание экземпляров классов
        self.button = Button(self, 60, 60, 'q')
        self.output = Output(self)




    def run_game(self):
        '''Запуск основного цикла игры'''

        while True:

            self._check_events()

            self._update_screen()



    def _check_events(self):
        '''Обрабатывает нажатия клавиш и события мыши'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            self.button.button_color = self.settings.button_color_2


    def _check_keyup_events(self, event):
        if event.key == pygame.K_q:
            self.button.button_color = self.settings.button_color_1



    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''

        self.screen.fill(self.settings.bg_color)

        self.button.draw_button()
        self.output.draw_line()

        
        pygame.display.flip()





if __name__ == '__main__':
    # Создание экземпляра игры
    ai =GigaChat()
    ai.run_game()


