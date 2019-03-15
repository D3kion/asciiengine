import pygame

from . import Config, Display


class Engine:
    def __init__(self, config: Config = Config()):
        self._config = config

        pygame.init()
        pygame.display.set_caption(self._config.WINDOW_CAPTION)

        self._window = pygame.display.set_mode(*self._config.WINDOW_MODE)
        self._clock = pygame.time.Clock()

        self._display = Display(self._window, self._config)
        # self.event_handler = EventHandler()

    @property
    def display(self):
        return self._display
