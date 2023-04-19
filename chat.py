'''Программа по обучению печати'''

import sys
import pygame

from button import Button
from settings import Settings

class GigaChat:
    '''Класс для управления ресурсами и поведением игры'''

    def __init__(self):
        '''Инициализирует и создаёт игровые ресурсы'''

        pygame.init()
        self.settings = Settings()
            
        if self.settings.fullscreen is False:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("GigaChat")

        self.button = Button(self, 70, 70, 'q')



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


    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''

        self.screen.fill(self.settings.bg_color)

        self.button.draw_button()
        
        pygame.display.flip()





if __name__ == '__main__':
    # Создание экземпляра игры
    ai =GigaChat()
    ai.run_game()


