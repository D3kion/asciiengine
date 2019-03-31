import pygame

from . import Config, Scene


class Display():
    def __init__(self, window, config: Config):
        self._config = config
        self._window = window

        self._font = pygame.font.SysFont(*self._config.FONT_DEFAULT)

        self._font_width, self._font_height = self._font.size('a')
        size = (self._config.DISPLAY_COLS * self._font_width,
                self._config.DISPLAY_ROWS * self._font_height)
        self._display = pygame.Surface(size)

    def _draw_display(self):
        window_width, window_height = self._window.get_size()
        display_position = (
            (window_width - self._display.get_width()) // 2,
            (window_height - self._display.get_height()) // 2
        )

        self._window.blit(self._display, display_position)
        pygame.draw.rect(self._display, (15, 15, 15),
                         (0, 0, window_width, window_height))

    def render(self, scene: Scene):
        self._draw_display()

    def _get_xy(self, colrow: tuple):
        col, row = colrow
        return (col * self._font_width, row * self._font_height)

    def draw(self, xy: tuple, text: str, color: tuple = (255, 255, 255)):
        label = self._font.render(text, 1, color)
        self._display.blit(label, self._get_xy(xy))
