import pygame

from .config import Config
from .display import Display
from .scene import Scene


class Engine:
    def __init__(self, config: Config = Config()):
        self._config = config

        pygame.init()
        pygame.display.set_caption(self._config.WINDOW_CAPTION)

        self._window = pygame.display.set_mode(*self._config.WINDOW_MODE)
        self._clock = pygame.time.Clock()

        self._scene = None
        self._display = Display(self._window, self._config)
        # self.event_handler = EventHandler()

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene: Scene, **kwargs):
        self._scene = scene(**kwargs)

    def handle_events(self):
        pass  # TODO

    def render(self):
        if self._scene is None:
            raise ValueError

        self._display.render(self._scene)
        pygame.display.flip()
