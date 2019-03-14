import sys

import pygame

from . import Config
from .ui import Scene, Drawer


class Display():
    def __init__(self, config: Config = Config()):
        self.config = config

        pygame.init()
        pygame.display.set_caption(self.config.WINDOW_CAPTION)

        self.screen = pygame.display.set_mode(*self.config.WINDOW_MODE)
        self.font = pygame.font.SysFont(*self.config.FONT_DEFAULT)
        self.clock = pygame.time.Clock()

        self.font_width, self.font_height = self.font.size('a')
        size = (self.config.DISPLAY_COLS * self.font_width,
                self.config.DISPLAY_ROWS * self.font_height)
        self.display = pygame.Surface(size)

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene: Scene, **kwargs):
        self._scene = scene(Drawer(self), **kwargs)

    def _draw_display(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        display_position = (
            (screen_width - self.display.get_width()) // 2,
            (screen_height - self.display.get_height()) // 2)

        self.screen.blit(self.display, display_position)
        pygame.draw.rect(self.display, (0, 0, 0),
                         (0, 0, screen_width, screen_height))

    def handle_events(self):
        self._scene.handle_events()

    def render(self):
        self.screen.fill((15, 15, 15))
        self._draw_display()
        self._scene.draw()

        
        
        label = self.font.render('AAAAAAA', 1, (255, 0, 0))
        self.screen.blit(label, (0, 0))
        pygame.display.flip()
