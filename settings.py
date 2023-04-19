class Settings:
    '''Класс для хранения настроек игры'''

    def __init__(self):
        '''Инициализирует статичечкие настройки игры'''
        # Параметры экрана
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 70)

        # Цвет кнопки
        self.button_color_1 = (110, 210, 110)
        self.button_color_2 = (210, 110, 110)